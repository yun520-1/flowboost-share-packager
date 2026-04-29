# FlowBoost Share Packager

A compact skill for turning FlowBoost into a shareable skill package.

## What it does

- describes FlowBoost in public-friendly language
- keeps only the files needed for sharing
- removes internal docs, logs, caches, and private material
- validates file count and package size before release

## Use cases

- publish FlowBoost as a reusable skill
- package FlowBoost for sharing with other agents or users
- prepare a ZIP for skill marketplaces

## Output

The package normally includes:
- `SKILL.md`
- `references/`
- `scripts/`

## Safety

Do not include:
- API keys
- personal notes
- logs
- caches
- private config
