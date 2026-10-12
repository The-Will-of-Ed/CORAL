#!/usr/bin/env python3
"""Copy the portable CORAL skill into a supported agent's skill directory.

Standard library only. No network access, external commands, or telemetry.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


AGENT_FOLDERS = {
    "codex": ".agents",
    "claude": ".claude",
    "cursor": ".cursor",
}


def install(agent: str, scope: str, project: Path | None = None, force: bool = False) -> Path:
    source = Path(__file__).resolve().parents[1] / "skills" / "coral"
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError("The source skill is missing SKILL.md")

    if scope == "user":
        if project is not None:
            raise ValueError("--project is valid only with --scope project")
        base = Path.home()
    else:
        base = (project or Path.cwd()).expanduser().resolve()
        if not base.is_dir():
            raise FileNotFoundError(f"Project directory not found: {base}")

    destination = base / AGENT_FOLDERS[agent] / "skills" / "coral"
    if destination.exists():
        if destination.is_symlink():
            raise FileExistsError(f"Refusing to replace a symlink: {destination}")
        if not destination.is_dir():
            raise FileExistsError(f"Refusing to replace a non-directory: {destination}")
        if _same_tree(source, destination):
            return destination
        if not force:
            raise FileExistsError(
                f"Already exists: {destination}. Review it before re-running with --force."
            )
        shutil.rmtree(destination)

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    return destination


def _same_tree(a: Path, b: Path) -> bool:
    left = {p.relative_to(a): p.read_bytes() for p in a.rglob("*") if p.is_file()}
    right = {p.relative_to(b): p.read_bytes() for p in b.rglob("*") if p.is_file()}
    return left == right


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", required=True, choices=sorted(AGENT_FOLDERS))
    parser.add_argument("--scope", default="user", choices=["user", "project"])
    parser.add_argument("--project", type=Path, help="Existing project directory; project scope only")
    parser.add_argument("--force", action="store_true", help="Replace a previously installed CORAL folder")
    args = parser.parse_args()
    try:
        destination = install(args.agent, args.scope, args.project, args.force)
    except (OSError, ValueError) as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        return 1
    print(f"CORAL installed: {destination}")
    print("Restart or refresh your agent, then ask it to use CORAL.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
