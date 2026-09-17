import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "rehearse.py"
SPEC = importlib.util.spec_from_file_location("rehearse", SCRIPT)
rehearse = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rehearse)


class PacketTests(unittest.TestCase):
    def test_role_packets_do_not_reveal_other_evidence_or_answers(self):
        for name in rehearse.scenarios():
            data = rehearse.scenario_data(name)
            start = rehearse.render_start(name)
            for object_id, evidence in data["packets"].items():
                self.assertNotIn(evidence, start)
                packet = rehearse.render_packet(name, object_id)
                self.assertIn(evidence, packet)
                for other, other_evidence in data["packets"].items():
                    if other != object_id:
                        self.assertNotIn(other_evidence, packet)
                for expected in data["evaluation"]["must_establish"]:
                    self.assertNotIn(expected, packet)
                    self.assertNotIn(expected, start)

    def test_fixture_coverage(self):
        self.assertEqual(len(rehearse.scenarios()), 3)
        for name in rehearse.scenarios():
            data = rehearse.scenario_data(name)
            self.assertEqual(set(data["packets"]), set(rehearse.DIRECTORY))
            self.assertTrue(data["evaluation"]["must_not_claim"])

    def test_unknown_identifiers_cannot_be_used_as_paths(self):
        with self.assertRaises(ValueError):
            rehearse.scenario_data("../../README")
        with self.assertRaises(ValueError):
            rehearse.render_packet("topic-mismatch", "../../README")


if __name__ == "__main__":
    unittest.main()
