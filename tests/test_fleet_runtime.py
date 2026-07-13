import importlib.util
import sys
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "fleet_runtime.py"
SPEC = importlib.util.spec_from_file_location("fleet_runtime", MODULE_PATH)
assert SPEC and SPEC.loader
fleet_runtime = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = fleet_runtime
SPEC.loader.exec_module(fleet_runtime)


class FleetRuntimeTests(unittest.TestCase):
    def test_bounded(self):
        self.assertEqual(fleet_runtime.bounded(-1.0), 0.0)
        self.assertEqual(fleet_runtime.bounded(2.0), 1.0)
        self.assertEqual(fleet_runtime.bounded(0.5), 0.5)

    def test_score_update_stays_bounded(self):
        value = fleet_runtime.update_score(0.8, 0.2, 0.18)
        self.assertGreaterEqual(value, 0.0)
        self.assertLessEqual(value, 1.0)

    def test_pruning_removes_low_scores_and_caps_memory(self):
        memories = [
            {"cycle": 1, "score": 0.20},
            {"cycle": 2, "score": 0.80},
            {"cycle": 3, "score": 0.70},
        ]
        retained, pruned = fleet_runtime.prune_memories(memories, 0.42, 1)
        self.assertEqual(len(retained), 1)
        self.assertEqual(retained[0]["score"], 0.80)
        self.assertEqual(pruned, 2)


if __name__ == "__main__":
    unittest.main()
