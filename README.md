# FlowBoost Share Packager

This skill turns FlowBoost into a shareable, public-friendly package.

## What it does

- rewrites internal plugin language into a reusable skill description
- keeps the minimum files needed for sharing
- removes logs, caches, private notes, and other internal material
- validates the final package before publishing

## Skill capabilities

- package FlowBoost as a compact skill bundle
- extract public-facing capability wording
- recommend what to keep and what to delete
- generate a publishable ZIP structure
- check file count, archive size, and sensitive content
- convert private implementation details into user-facing language

## Good public description

FlowBoost is a terminal output optimizer that reduces noise from long logs by compressing repeated lines, merging similar output, extracting error context, and shortening large outputs while keeping the useful signal.

## Typical use cases

- build logs with repeated warnings
- command output that grows too large
- debug sessions with redundant messages
- release packaging for sharing with others

## What to keep in the share package

- `SKILL.md`
- `README.md`
- `references/`
- `scripts/`

## What to remove before sharing

- `.git/`
- `__pycache__/`
- `.pyc`
- logs and caches
- private config files
- chat logs and personal notes
- API keys and secrets

## Packaging checklist

- [ ] package contains a clear `SKILL.md`
- [ ] internal files are removed
- [ ] package stays within platform limits
- [ ] the description reads like a public skill, not a private note
- [ ] sensitive values are not included anywhere

## Tone guidance

Write the published skill like a small product: clear purpose, clear abilities, clear output. Avoid making it sound like a dev notebook or an internal migration note.
