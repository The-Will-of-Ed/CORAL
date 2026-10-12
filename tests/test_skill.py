"""Dependency-free checks of the portable skill and its installer."""

import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "coral" / "SKILL.md"

spec = importlib.util.spec_from_file_location("coral_installer", ROOT / "scripts" / "install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class ManifestTests(unittest.TestCase):
    def test_skill_manifest_and_links(self):
        content = SKILL.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        self.assertIsNotNone(match)
        front = match.group(1)
        self.assertRegex(front, r"(?m)^name: coral$")
        self.assertRegex(front, r"(?m)^description: .{20,1024}$")
        for link in re.findall(r"\]\((references/[^)]+)\)", content):
            self.assertTrue((SKILL.parent / link).is_file(), link)

    def test_contains_critical_contracts(self):
        content = SKILL.read_text(encoding="utf-8").lower()
        for phrase in ("objective + ownership", "result + reasoning", "learning",
                       "before the step-by-step actions", "one fact record",
                       "estimated", "confirmed", "unknown", "same record",
                       "at most three", "fast mode", "star", "coral"):
            self.assertIn(phrase, content, phrase)

    def test_image_and_license(self):
        self.assertTrue((ROOT / "assets" / "star-vs-coral.png").is_file())
        self.assertTrue((ROOT / "LICENSE").is_file())


class InstallerTests(unittest.TestCase):
    def test_each_agent_installs_in_project_without_modifying_source(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            for agent, hidden in installer.AGENT_FOLDERS.items():
                path = installer.install(agent, "project", project)
                self.assertEqual(path, project / hidden / "skills" / "coral")
                self.assertEqual((path / "SKILL.md").read_bytes(), SKILL.read_bytes())
                self.assertEqual(installer.install(agent, "project", project), path)

    def test_existing_skill_is_not_overwritten_without_force(self):
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            destination = installer.install("cursor", "project", project)
            (destination / "SKILL.md").write_text("local changes", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install("cursor", "project", project)
            self.assertEqual((destination / "SKILL.md").read_text(), "local changes")
            installer.install("cursor", "project", project, force=True)
            self.assertEqual((destination / "SKILL.md").read_bytes(), SKILL.read_bytes())

    def test_reject_project_flag_for_user_scope(self):
        with self.assertRaises(ValueError):
            installer.install("codex", "user", Path("."))


if __name__ == "__main__":
    unittest.main()
