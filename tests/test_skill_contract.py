from pathlib import Path
import unittest


SKILL_PATH = Path(__file__).parents[1] / "skills" / "piszpoludzku" / "SKILL.md"


class SkillContractTests(unittest.TestCase):
    def test_deep_rewrite_does_not_introduce_ornamental_dashes(self):
        skill = SKILL_PATH.read_text(encoding="utf-8")

        self.assertIn("Nie wprowadzaj półpauz", skill)
        self.assertIn("kropkami, przecinkami lub dwukropkami", skill)


if __name__ == "__main__":
    unittest.main()
