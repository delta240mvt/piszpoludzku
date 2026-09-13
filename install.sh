#!/usr/bin/env sh
set -eu

target="both"
destination_root="${HOME}"
force=0

usage() {
  printf '%s\n' 'Usage: ./install.sh [--target claude|codex|both] [--destination-root PATH] [--force]'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target) [ "$#" -ge 2 ] || { usage >&2; exit 2; }; target="$2"; shift 2 ;;
    --destination-root) [ "$#" -ge 2 ] || { usage >&2; exit 2; }; destination_root="$2"; shift 2 ;;
    --force) force=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
done

case "$target" in claude|codex|both) ;; *) usage >&2; exit 2 ;; esac

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
source_dir="$script_dir/skills/piszpoludzku"
[ -f "$source_dir/SKILL.md" ] || { printf '%s\n' "Missing skill source: $source_dir" >&2; exit 1; }

install_skill() {
  runtime="$1"
  directory="$2"
  skills_dir="$destination_root/$directory/skills"
  destination="$skills_dir/piszpoludzku"
  if [ -e "$destination" ]; then
    if [ "$force" -ne 1 ]; then
      printf '%s\n' "Skill already exists: $destination. Re-run with --force to back it up and reinstall." >&2
      exit 1
    fi
    timestamp=$(date +%Y%m%d-%H%M%S)
    backup="$destination.bak-$timestamp"
    suffix=0
    while [ -e "$backup" ]; do
      suffix=$((suffix + 1))
      backup="$destination.bak-$timestamp-$suffix"
    done
    mv "$destination" "$backup"
    printf '%s\n' "Backup ($runtime): $backup"
  fi
  mkdir -p "$destination"
  cp -R "$source_dir"/. "$destination"
  printf '%s\n' "Installed $runtime: $destination"
}

if [ "$target" = "claude" ] || [ "$target" = "both" ]; then
  install_skill "Claude Code" ".claude"
fi
if [ "$target" = "codex" ] || [ "$target" = "both" ]; then
  install_skill "Codex" ".agents"
fi
