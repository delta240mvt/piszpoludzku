import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POWERSHELL = shutil.which("pwsh") or shutil.which("powershell")
GIT_BASH = Path(r"C:\Program Files\Git\bin\bash.exe")
BASH = shutil.which("bash") or (str(GIT_BASH) if GIT_BASH.is_file() else None)


@unittest.skipUnless(POWERSHELL, "PowerShell is not available")
class PowerShellInstallerTests(unittest.TestCase):
    def run_installer(self, destination: Path, target: str = "Both", force: bool = False):
        command = [POWERSHELL, "-NoProfile", "-File", str(ROOT / "install.ps1"), "-Target", target, "-DestinationRoot", str(destination)]
        if force:
            command.append("-Force")
        return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)

    def test_installs_claude_codex_and_handles_existing_skill_safely(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "Zażółć folder with spaces"
            first = self.run_installer(destination, "Both")
            self.assertEqual(0, first.returncode, first.stderr)
            claude_skill = destination / ".claude" / "skills" / "piszpoludzku"
            codex_skill = destination / ".agents" / "skills" / "piszpoludzku"
            self.assertTrue((claude_skill / "SKILL.md").is_file())
            self.assertTrue((codex_skill / "SKILL.md").is_file())

            marker = claude_skill / "marker.txt"
            marker.write_text("local change", encoding="utf-8")
            second = self.run_installer(destination, "Claude")
            self.assertNotEqual(0, second.returncode)
            self.assertTrue(marker.exists())

            forced = self.run_installer(destination, "Claude", force=True)
            self.assertEqual(0, forced.returncode, forced.stderr)
            self.assertFalse(marker.exists())
            backups = list((destination / ".claude" / "skills").glob("piszpoludzku.bak-*"))
            self.assertEqual(1, len(backups))
            self.assertTrue((backups[0] / "marker.txt").is_file())

    def test_installer_has_no_python_dependency(self):
        content = (ROOT / "install.ps1").read_text(encoding="utf-8")
        self.assertNotIn("python", content.lower())


@unittest.skipUnless(BASH, "Bash is not available")
class BashInstallerTests(unittest.TestCase):
    def test_claude_only_reports_success(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [BASH, str(ROOT / "install.sh"), "--target", "claude", "--destination-root", directory],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue((Path(directory) / ".claude/skills/piszpoludzku/SKILL.md").is_file())

    def test_installs_codex(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "folder with spaces"
            result = subprocess.run(
                [BASH, str(ROOT / "install.sh"), "--target", "codex", "--destination-root", str(destination)],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertTrue((destination / ".agents" / "skills" / "piszpoludzku" / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
