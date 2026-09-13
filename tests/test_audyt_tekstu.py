import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "piszpoludzku" / "scripts" / "audyt_tekstu.py"


def load_module():
    spec = importlib.util.spec_from_file_location("audyt_tekstu", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


class AuditTextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = load_module()

    def test_detects_serial_patterns_with_neutral_names(self):
        text = "\n".join(
            [
                "Nie chodzi o tempo. Chodzi o sens.",
                "Nie chodzi o widoczność. Chodzi o użyteczność.",
                "Nie chodzi o objętość. Chodzi o decyzję.",
                "To kluczowy, fundamentalny i ważny krok.",
                "### Zrób teraz",
                "### Zrób teraz",
                "### Zrób teraz",
            ]
        )
        report = self.audit.audit_text(text, "sample.md")
        rules = {item["rule_id"] for item in report["findings"]}
        self.assertIn("serial-contrast", rules)
        self.assertIn("empty-emphasis-series", rules)
        self.assertIn("repeated-heading", rules)
        for finding in report["findings"]:
            self.assertNotIn("AI", finding["message"])
            self.assertLessEqual(len(finding["excerpt"]), 160)

    def test_single_contrast_and_legal_triad_are_not_flagged(self):
        text = "\n".join(
            [
                "To nie jest porada prawna. To krótka instrukcja operacyjna.",
                "Warunek jest spełniony, gdy zgłoszenie jest kompletne, podpisane i złożone w terminie.",
            ]
        )
        report = self.audit.audit_text(text)
        rules = {item["rule_id"] for item in report["findings"]}
        self.assertNotIn("serial-contrast", rules)
        self.assertNotIn("empty-emphasis-series", rules)

    def test_ignores_protected_markdown_and_reports_unclosed_fence(self):
        protected = "\n".join(
            [
                "---",
                "title: kluczowy fundamentalny ważny",
                "---",
                "`Nie chodzi o tempo. Chodzi o sens.`",
                "```python",
                "# Nie chodzi o tempo. Chodzi o sens.",
                "# Nie chodzi o tempo. Chodzi o sens.",
                "# Nie chodzi o tempo. Chodzi o sens.",
                "```",
                "| pole | kluczowy fundamentalny ważny |",
                "<!-- Nie chodzi o tempo. Chodzi o sens. -->",
            ]
        )
        report = self.audit.audit_text(protected)
        rules = {item["rule_id"] for item in report["findings"]}
        self.assertNotIn("serial-contrast", rules)
        self.assertNotIn("empty-emphasis-series", rules)

        unclosed = self.audit.audit_text("```\nniezamknięty blok\n")
        error = next(item for item in unclosed["findings"] if item["rule_id"] == "markdown-unclosed-fence")
        self.assertEqual("error", error["severity"])

    def test_handles_bom_crlf_and_unicode_with_original_line_numbers(self):
        text = "\ufeffPierwsza linia\r\nNie chodzi o tempo. Chodzi o sens.\r\nNie chodzi o zasięg. Chodzi o użyteczność.\r\nNie chodzi o liczbę. Chodzi o decyzję.\r\n"
        report = self.audit.audit_text(text)
        finding = next(item for item in report["findings"] if item["rule_id"] == "serial-contrast")
        self.assertEqual(2, finding["line"])
        self.assertGreaterEqual(finding["column"], 1)


class AuditCliTests(unittest.TestCase):
    def test_report_cannot_overwrite_source_or_hard_link(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "tekst.md"
            source.write_text("Ważny tekst autora.\n", encoding="utf-8")
            alias = Path(directory) / "alias.md"
            alias.hardlink_to(source)
            before = source.read_bytes()
            for output in (source, alias):
                with self.subTest(output=output.name):
                    result = subprocess.run(
                        [sys.executable, str(SCRIPT), str(source), "--output", str(output)],
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(1, result.returncode, result.stderr)
                    self.assertEqual(before, source.read_bytes())

    def test_cli_json_preserves_input_and_fail_on_error(self):
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            input_path = directory_path / "Zażółć test.md"
            output_path = directory_path / "report.json"
            input_path.write_text("```\nniezamknięty blok\n", encoding="utf-8")
            before = hashlib.sha256(input_path.read_bytes()).hexdigest()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(input_path), "--format", "json", "--output", str(output_path), "--fail-on", "error"],
                capture_output=True,
                text=True,
                check=False,
            )
            after = hashlib.sha256(input_path.read_bytes()).hexdigest()
            self.assertEqual(3, result.returncode, result.stderr)
            self.assertEqual(before, after)
            report = json.loads(output_path.read_text(encoding="utf-8"))
            self.assertEqual("1.0", report["schema_version"])
            self.assertEqual("markdown-unclosed-fence", report["findings"][0]["rule_id"])

    def test_cli_returns_one_for_missing_file_and_two_for_bad_arguments(self):
        missing = subprocess.run(
            [sys.executable, str(SCRIPT), "nie-istnieje.md"], capture_output=True, text=True, check=False
        )
        bad = subprocess.run(
            [sys.executable, str(SCRIPT), "--format", "nope", "plik.md"], capture_output=True, text=True, check=False
        )
        self.assertEqual(1, missing.returncode)
        self.assertEqual(2, bad.returncode)


if __name__ == "__main__":
    unittest.main()
