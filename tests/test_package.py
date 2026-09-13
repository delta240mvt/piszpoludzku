import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_zip_contains_complete_skill_and_license_without_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "piszpoludzku.zip"
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/package_skill.py"), "--output", str(output)],
                capture_output=True, text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
                self.assertIn("piszpoludzku/SKILL.md", names)
                self.assertIn("piszpoludzku/LICENSE", names)
                self.assertIn("piszpoludzku/VERSION", names)
                self.assertFalse(any("__pycache__" in name or name.endswith(".pyc") for name in names))
                for path in (ROOT / "skills/piszpoludzku").rglob("*"):
                    if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                        name = "piszpoludzku/" + path.relative_to(ROOT / "skills/piszpoludzku").as_posix()
                        self.assertEqual(path.read_bytes().replace(b"\r\n", b"\n"), archive.read(name))


if __name__ == "__main__":
    unittest.main()
