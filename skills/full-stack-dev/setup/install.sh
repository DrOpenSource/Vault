#!/usr/bin/env bash
# Install the full-stack-dev skill.
#
#   ./install.sh --global [--link]          # for every project: ~/.claude/skills/full-stack-dev
#   ./install.sh --project <dir> [--link] [--with-settings]
#                                           # one project: <dir>/.claude/skills/full-stack-dev,
#                                           # plus CLAUDE.md block and docs/fsd/lanes.md
#
#   --link           symlink instead of copy, so `git pull` in your vault updates the skill
#                    (global installs only make sense this way if the vault stays put)
#   --with-settings  merge setup/settings.example.json into <dir>/.claude/settings.json
#                    (asks-before-destructive-commands rules; backs up any existing file)
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODE=""; TARGET_PROJECT=""; LINK=0; WITH_SETTINGS=0

usage() { sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'; exit 1; }

while [ $# -gt 0 ]; do
  case "$1" in
    --global) MODE=global ;;
    --project) MODE=project; TARGET_PROJECT="${2:-}"; shift ;;
    --link) LINK=1 ;;
    --with-settings) WITH_SETTINGS=1 ;;
    -h|--help) usage ;;
    *) echo "Unknown option: $1"; usage ;;
  esac
  shift
done
[ -n "$MODE" ] || usage

place_skill() {  # $1 = destination directory
  local dest="$1"
  mkdir -p "$(dirname "$dest")"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ -L "$dest" ] || [ -f "$dest/.fsd-installed" ]; then
      rm -rf "$dest"
    else
      echo "Refusing to overwrite $dest (not installed by this script). Move it and re-run."; exit 1
    fi
  fi
  if [ "$LINK" = 1 ]; then
    ln -s "$SKILL_DIR" "$dest"
  else
    mkdir -p "$dest"
    cp -R "$SKILL_DIR/." "$dest/"
    touch "$dest/.fsd-installed"
  fi
  echo "Skill installed at $dest$([ "$LINK" = 1 ] && echo ' (symlink)')"
}

if [ "$MODE" = global ]; then
  place_skill "$HOME/.claude/skills/full-stack-dev"
  echo "Done. In any project, run /full-stack-dev (or just describe the task)."
  echo "Tip: run with --project <dir> once per repo to add the CLAUDE.md block."
  exit 0
fi

[ -n "$TARGET_PROJECT" ] && [ -d "$TARGET_PROJECT" ] || { echo "Project dir not found: $TARGET_PROJECT"; exit 1; }
PROJ="$(cd "$TARGET_PROJECT" && pwd)"

place_skill "$PROJ/.claude/skills/full-stack-dev"

# CLAUDE.md block (idempotent: skipped if the marker is already there)
CLAUDE_MD="$PROJ/CLAUDE.md"
if [ -f "$CLAUDE_MD" ] && grep -q "full-stack-dev: start" "$CLAUDE_MD"; then
  echo "CLAUDE.md already has the Full-Stack Dev block; left unchanged."
else
  { [ -f "$CLAUDE_MD" ] && printf '\n'; cat "$SKILL_DIR/templates/project-CLAUDE.md"; } >> "$CLAUDE_MD"
  echo "Added Full-Stack Dev block to $CLAUDE_MD. Fill in the <placeholders> (verify command, clinical rules)."
fi

# Lane board
mkdir -p "$PROJ/docs/fsd"
if [ ! -f "$PROJ/docs/fsd/lanes.md" ]; then
  cp "$SKILL_DIR/templates/lanes.md" "$PROJ/docs/fsd/lanes.md"
  echo "Created docs/fsd/lanes.md"
fi

# Optional safety settings merge
if [ "$WITH_SETTINGS" = 1 ]; then
  SETTINGS="$PROJ/.claude/settings.json"
  if [ -f "$SETTINGS" ]; then cp "$SETTINGS" "$SETTINGS.bak.$(date +%Y%m%d%H%M%S)"; fi
  python3 - "$SKILL_DIR/setup/settings.example.json" "$SETTINGS" <<'PY'
import json, sys, os
src, dst = sys.argv[1], sys.argv[2]
new = json.load(open(src))
cur = json.load(open(dst)) if os.path.exists(dst) else {}
perms = cur.setdefault("permissions", {})
for key, rules in new["permissions"].items():
    existing = perms.setdefault(key, [])
    for r in rules:
        if r not in existing:
            existing.append(r)
json.dump(cur, open(dst, "w"), indent=2)
open(dst, "a").write("\n")
print(f"Merged safety rules into {dst}")
PY
fi

echo "Done. Open Claude Code in $PROJ and run /full-stack-dev status."
