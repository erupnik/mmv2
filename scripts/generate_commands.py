#!/usr/bin/env python3
"""
Auto-generate the MMVII commands reference page (docs/commands.md)
by parsing cSpecMMVII_Appli registrations in the C++ source code.

Usage:
    python scripts/generate_commands.py [--src-dir ../src]

The script searches for command registration patterns like:

    cSpecMMVII_Appli  TheSpecXXX
    (
         "CommandName",
          Alloc_XXX,
          "Description of the command",
          {eApF::Category1, eApF::Category2},
          {eApDT::Input},
          {eApDT::Output},
          __FILE__
    );

and groups commands by their eApF feature category.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# Human-readable names for eApF categories, in display order
CATEGORY_NAMES = {
    "Ori":          "Orientation & Bundle Adjustment",
    "Match":        "Dense Matching",
    "CodedTarget":  "Coded Targets",
    "Cloud":        "Point Clouds & Mesh",
    "GCP":          "Ground Control Points",
    "TieP":         "Tie Points",
    "Lines":        "Lines",
    "SysCo":        "Coordinate Systems",
    "Radiometry":   "Radiometry",
    "Topo":         "Topography",
    "BlockInstr":   "Block Instruments",
    "Clino":        "Clinometers",
    "ImProc":       "Image Processing",
    "Project":      "Project Management",
    "ManMMVII":     "MMVII Management",
    "Test":         "Testing",
    "Simul":        "Simulation",
    "TiePLearn":    "Tie Point Learning",
    "Perso":        "Personal / Experimental",
    "NoGui":        "Utilities",
}

# Display order for categories
CATEGORY_ORDER = list(CATEGORY_NAMES.keys())


def find_command_specs(src_dir: Path):
    """
    Parse all .cpp files under src_dir for cSpecMMVII_Appli registrations.
    Returns a list of dicts with keys: name, comment, features, source_file.
    """
    # Pattern matches multi-line cSpecMMVII_Appli constructor calls.
    # We read entire files and use a regex that spans the constructor.
    pattern = re.compile(
        r'cSpecMMVII_Appli\s+\w+\s*'       # cSpecMMVII_Appli TheSpecXXX
        r'\(\s*'                             # opening paren
        r'"([^"]+)"\s*,'                     # group 1: command name
        r'\s*\w+\s*,'                        # allocator function
        r'\s*"([^"]*(?:"\s*"[^"]*)*)"\s*,'   # group 2: comment (may be split across string literals)
        r'\s*\{([^}]*)\}\s*,'               # group 3: features {eApF::...}
        r'\s*\{([^}]*)\}\s*,'               # group 4: inputs {eApDT::...}
        r'\s*\{([^}]*)\}\s*,'               # group 5: outputs {eApDT::...}
        r'\s*__FILE__\s*'                    # __FILE__
        r'\)',                               # closing paren
        re.DOTALL
    )

    commands = []

    for cpp_file in sorted(src_dir.rglob("*.cpp")):
        try:
            text = cpp_file.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        for m in pattern.finditer(text):
            name = m.group(1).strip()
            # Merge split string literals: "foo" "bar" -> "foobar"
            comment = re.sub(r'"\s*"', '', m.group(2)).strip()
            features_raw = m.group(3).strip()

            # Extract eApF enum values
            features = re.findall(r'eApF::(\w+)', features_raw)

            rel_path = str(cpp_file.relative_to(src_dir))

            commands.append({
                "name": name,
                "comment": comment,
                "features": features,
                "source_file": rel_path,
            })

    # Sort by command name (case-insensitive)
    commands.sort(key=lambda c: c["name"].lower())
    return commands


def group_by_category(commands):
    """Group commands by their primary (first) eApF feature."""
    groups = defaultdict(list)
    for cmd in commands:
        if cmd["features"]:
            primary = cmd["features"][0]
        else:
            primary = "ManMMVII"
        groups[primary].append(cmd)
    return groups


def generate_markdown(commands):
    """Generate the full commands.md content."""
    lines = []
    lines.append("# Command Reference")
    lines.append("")
    lines.append(f"MMVII provides **{len(commands)} commands** organized by domain. "
                 f"Run `MMVII help` for a complete list.")
    lines.append("")
    lines.append("Every MMVII command follows the same pattern:")
    lines.append("")
    lines.append("```")
    lines.append("MMVII CommandName MandatoryArg1 MandatoryArg2 [OptArg1=value] [OptArg2=value]")
    lines.append("```")
    lines.append("")
    lines.append("Get help on any command with: `MMVII CommandName help`")
    lines.append("")
    lines.append("!!! note \"Auto-generated\"")
    lines.append("    This page is auto-generated from the source code by "
                 "`scripts/generate_commands.py`.")
    lines.append("")

    groups = group_by_category(commands)

    for cat_key in CATEGORY_ORDER:
        if cat_key not in groups:
            continue
        cat_name = CATEGORY_NAMES.get(cat_key, cat_key)
        cat_cmds = groups[cat_key]

        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append("| Command | Description |")
        lines.append("|---------|-------------|")
        for cmd in cat_cmds:
            # Escape pipe characters in description
            desc = cmd["comment"].replace("|", "\\|")
            lines.append(f"| `{cmd['name']}` | {desc} |")
        lines.append("")

    # Any categories not in CATEGORY_ORDER
    for cat_key, cat_cmds in sorted(groups.items()):
        if cat_key in CATEGORY_ORDER:
            continue
        cat_name = CATEGORY_NAMES.get(cat_key, cat_key)
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append("| Command | Description |")
        lines.append("|---------|-------------|")
        for cmd in cat_cmds:
            desc = cmd["comment"].replace("|", "\\|")
            lines.append(f"| `{cmd['name']}` | {desc} |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate MMVII commands reference page from source code"
    )
    parser.add_argument(
        "--src-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent.parent / "src",
        help="Path to the MMVII src/ directory (default: auto-detected)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file path (default: stdout). Use docs/commands.md to overwrite.",
    )
    args = parser.parse_args()

    if not args.src_dir.is_dir():
        print(f"Error: src directory not found: {args.src_dir}", file=sys.stderr)
        sys.exit(1)

    commands = find_command_specs(args.src_dir)

    if not commands:
        print("Warning: no commands found. Check --src-dir path.", file=sys.stderr)
        sys.exit(1)

    md = generate_markdown(commands)

    if args.output:
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {len(commands)} commands to {args.output}", file=sys.stderr)
    else:
        print(md)


if __name__ == "__main__":
    main()
