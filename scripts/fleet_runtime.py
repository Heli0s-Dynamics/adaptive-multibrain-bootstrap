#!/usr/bin/env python3
"""Bounded, deterministic Hermes/XCore learning and pruning runtime."""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config" / "aihub"
STATE_DIR = ROOT / "state" / "aihub"


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    temporary.replace(path)


@dataclass(frozen=True)
class Task:
    cycle: int
    family: str
    difficulty: float


def bounded(value: float) -> float:
    return max(0.0, min(1.0, value))


def choose_agent(state: dict[str, Any], task: Task) -> str:
    hermes = float(state["agents"]["Hermes"]["score"])
    xcore = float(state["agents"]["XCore"]["score"])
    # Hermes owns lightweight exploration; XCore owns harder evaluation work.
    threshold = 0.58 + ((xcore - hermes) * 0.20)
    return "XCore" if task.difficulty >= threshold else "Hermes"


def outcome(rng: random.Random, score: float, difficulty: float) -> float:
    noise = rng.uniform(-0.045, 0.045)
    return bounded(0.58 + (score * 0.34) - (difficulty * 0.16) + noise)


def update_score(previous: float, result: float, rate: float) -> float:
    return bounded(previous + rate * (result - previous))


def prune_memories(memories: list[dict[str, Any]], threshold: float, maximum: int) -> tuple[list[dict[str, Any]], int]:
    retained = [item for item in memories if float(item.get("score", 0.0)) >= threshold]
    retained.sort(key=lambda item: (float(item.get("score", 0.0)), int(item.get("cycle", 0))), reverse=True)
    retained = retained[:maximum]
    return retained, len(memories) - len(retained)


def run(cycles: int, seed: int) -> dict[str, Any]:
    fleet = load_json(CONFIG_DIR / "fleet.json", {})
    policy = load_json(CONFIG_DIR / "policy.json", {})
    maximum_cycles = int(policy["maxCycles"])
    if cycles < 1 or cycles > maximum_cycles:
        raise ValueError(f"cycles must be between 1 and {maximum_cycles}")

    state = load_json(STATE_DIR / "learning-state.json", {})
    memories = load_json(STATE_DIR / "curated-memory.json", [])
    rng = random.Random(seed)
    rate = float(policy["learningRate"])
    families = list(fleet["taskFamilies"])
    results: list[dict[str, Any]] = []

    for cycle in range(1, cycles + 1):
        task = Task(cycle=cycle, family=families[(cycle - 1) % len(families)], difficulty=rng.uniform(0.25, 0.92))
        agent = choose_agent(state, task)
        previous = float(state["agents"][agent]["score"])
        result = outcome(rng, previous, task.difficulty)
        updated = update_score(previous, result, rate)
        state["agents"][agent]["score"] = round(updated, 6)
        state["agents"][agent]["samples"] = int(state["agents"][agent].get("samples", 0)) + 1
        record = {
            "cycle": cycle,
            "family": task.family,
            "difficulty": round(task.difficulty, 6),
            "agent": agent,
            "score": round(result, 6),
            "learnedScore": round(updated, 6)
        }
        results.append(record)
        memories.append(record)

    memories, pruned = prune_memories(memories, float(policy["pruneBelow"]), int(policy["maximumMemories"]))
    state["runCount"] = int(state.get("runCount", 0)) + 1
    state["lastSeed"] = seed
    state["lastCycles"] = cycles
    state["updatedAt"] = datetime.now(timezone.utc).isoformat()

    scores = [float(item["score"]) for item in results]
    mean_score = sum(scores) / len(scores)
    evaluation = {
        "passed": mean_score >= float(policy["minimumScore"]),
        "meanScore": round(mean_score, 6),
        "minimumScore": round(min(scores), 6),
        "maximumScore": round(max(scores), 6),
        "cycles": cycles,
        "forbiddenCapabilities": policy["forbiddenCapabilities"]
    }
    report = {"seed": seed, "cycles": cycles, "results": results, "meanScore": round(mean_score, 6)}
    pruning = {"before": len(memories) + pruned, "after": len(memories), "pruned": pruned, "threshold": policy["pruneBelow"]}

    write_json(STATE_DIR / "learning-state.json", state)
    write_json(STATE_DIR / "curated-memory.json", memories)
    write_json(STATE_DIR / "learning-report.json", report)
    write_json(STATE_DIR / "evaluation-report.json", evaluation)
    write_json(STATE_DIR / "pruning-report.json", pruning)
    return evaluation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cycles", type=int, default=8)
    parser.add_argument("--seed", type=int, default=64)
    args = parser.parse_args()
    evaluation = run(args.cycles, args.seed)
    print(json.dumps(evaluation, indent=2, sort_keys=True))
    return 0 if evaluation["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
