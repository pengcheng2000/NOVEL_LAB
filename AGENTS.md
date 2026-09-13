# Repository Guidelines

## Project Structure & Module Organization

NOVEL_LAB is a documentation-first research repository, not an application. Read `00_system/ACTIVE_TASKS.md` and `00_system/PROJECT_STATUS.md` before starting work.

- `00_system/`: canonical workflow, schema, copyright rules, and project state.
- `01_reference/`: acquisition metadata, manifests, and per-book source registration; copyrighted source texts (txt/epub/pdf/mobi) are Git-ignored and stay local (see `01_reference/README.md`).
- `02_analysis/<region>/<book-slug>/`: per-book reports and `NOVEL_DNA.yaml` files. Regions are `global`, `china_print`, and `china_web`.
- `03_story_dna/`: regional syntheses and the master mechanism libraries.
- `04_original_project/`: design rules, candidates, finalists, and stress tests.
- `05_originality_review/`: originality-risk indexes and reviews.
- `99_logs/claude/`: durable work logs; older agent logs are historical.
- `.claude/skills/`: task-specific analysis and review procedures.

## Development & Validation Commands

There is no build system or automated test suite. Use lightweight repository checks:

```sh
rg --files                         # inventory tracked/workspace files
rg 'MISSING_SOURCE|PARTIAL_SOURCE' 00_system 02_analysis
ruby -e 'require "yaml"; ARGV.each { |f| YAML.load_file(f) }' \
  $(find 02_analysis 03_story_dna -name '*.yaml')
```

The Ruby command exits nonzero on malformed YAML. Also inspect Markdown for broken paths, inconsistent status labels, and unsupported full-book claims.

## Writing Style & Naming Conventions

Write concise, evidence-led Markdown. Avoid generic judgments such as “tight pacing”; identify the mechanism, story position, reader expectation, and payoff. Use status vocabulary exactly: `TODO`, `IN_PROGRESS`, `COMPLETED`, `BLOCKED`, and `PARTIAL_SOURCE`.

Use lowercase kebab-case for book directories, uppercase descriptive filenames for major artifacts (`STORY_DNA_REPORT.md`), and two-space YAML indentation. Preserve the A–Q schema in `00_system/ANALYSIS_SCHEMA.md`; write `not_applicable` instead of deleting fields. Do not overwrite completed work without documenting why it is insufficient.

## Testing & Review Guidelines

Validate every YAML edit and spot-check evidence against the declared source coverage. Follow progressive compression for long works: source index, 5–15 chapter batches, arc notes, novel-level DNA, then synthesis. Update `PROJECT_STATUS.md`, `ACTIVE_TASKS.md`, and a dated log after a major phase.

## Commit & Pull Request Guidelines

GitHub (`https://github.com/pengcheng2000/NOVEL_LAB.git`) is the central source of truth — pull before starting work, and update status files plus push after completing significant work (see `00_system/AGENT_PROTOCOL.md` and `00_system/HANDOFF.md`). Use imperative scoped subjects, for example `analysis: add C06 stress-test evidence`. Never force-push. Pull requests should summarize artifacts, source coverage, validation, originality implications, and status updates.

## Copyright & Source Safety

Never download pirated texts or commit protected source files. Cite chapters, titles, locations, or brief summaries; any necessary quotation must be at most one sentence. Extract reusable abstract mechanisms, while marking distinctive names, settings, dialogue, and plot chains as RED/protected elements.
