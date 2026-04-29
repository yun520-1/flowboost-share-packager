# FlowBoost Share Packager

This skill turns FlowBoost into a shareable, public-friendly package.

## What it does

- rewrites internal plugin language into a reusable skill description
- keeps the minimum files needed for sharing
- removes logs, caches, private notes, and other internal material
- validates the final package before publishing

## Skills of this skill

- package FlowBoost as a compact skill bundle
- extract public-facing capability wording
- recommend what to keep and what to delete
- generate a publishable ZIP structure
- check file count, archive size, and sensitive content

## Output format

A good share package usually includes:
- `SKILL.md`
- `README.md`
- `references/`
- `scripts/`

## Good public description

FlowBoost is a terminal output optimizer that reduces noise from long logs by compressing repeated lines, merging similar output, extracting error context, and shortening large outputs while keeping the useful signal.

## Typical use cases

- build logs with repeated warnings
- command output that grows too large
- debug sessions with redundant messages
- release packaging for sharing with others

## Safety

Never include:
- API keys
- private configuration
- chat history
- raw internal memory
- temporary logs or cache files

## Packaging checklist

- [ ] package contains a clear `SKILL.md`
- [ ] internal files are removed
- [ ] package stays within platform limits
- [ ] the description reads like a public skill, not a private note
