# canon-forge

Minimal viable prototype for **Verifiable Generative Worldbuilding** — canon representation, 3D-scaffolded consistency, and provenance for long-horizon generative media.

This repository is the working proof-of-concept for a PhD proposal (2027 entry, UKRI track). It implements the first of three claims:

1. A fictional world can be formalised as a **machine-checkable constraint set** (this repo, v0.1);
2. The propagation distance and breaking conditions of semantic constraints in generation are **measurable** (roadmap);
3. Historical accuracy in generated media can be **automatically checked**, and the first public benchmark for this can be released (roadmap).

## What is here (v0.1)

| Path | Content |
|---|---|
| `canon/schema.json` | Canon schema draft: entity types (geography, timeline, factions, design rules) encoded as automatically checkable propositional constraints |
| `canon/rules/late-tang.json` | 14 design rules for a late-Tang (9th century) warlord-city world: 10 enforced forbidden-term rules + 4 defined-not-yet-enforced rules |
| `checker/checker.py` | Minimal constraint validator (Python standard library only, zero dependencies). Compares a generated-asset description against the rule set and reports violations |
| `examples/` | One deliberately anachronistic asset, one clean asset, and a recorded demo report |

## Motivation in one paragraph

Text generation has an industrialised "rules → constraints → verification → audit" layer (controlled decoding, guardrails, compliance-as-code). Visual generation only constrains *geometry* (camera pose, layout) and is evaluated for perceptual quality. There is no mechanism forcing a generative model to obey *propositional* rules ("this dynasty had no suspension bridges"), and no benchmark measuring rule compliance. Historical and cultural rules are the hardest instance of that gap — so this project starts where the rules are hardest. See `ROADMAP.md` for where this goes.

## Run the demo

```bash
python3 checker/checker.py examples/asset-anachronistic.json
python3 checker/checker.py examples/asset-clean.json
```

Expected: the first call reports 11 anachronism violations (chilli peppers, maize, tobacco, eyeglasses, matches, matchlocks, movable type, cement, a suspension bridge, paper money); the second reports zero.

## Status & roadmap

v0.1 (2026-11): schema + rule set + stdlib checker + demo. Next steps in `ROADMAP.md` — SHACL encoding of the canon schema, a small labelled benchmark, and integration with an actual generative pipeline.

## License

MIT (see `LICENSE`).
