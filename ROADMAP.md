# Roadmap

Tied to the three research questions of the proposal.

## v0.1 — 2026-11 (this release)

- [x] Canon schema draft (`canon/schema.json`): entity types as machine-checkable propositions
- [x] Late-Tang rule set v0.1: 10 enforced forbidden-term rules, 4 defined-not-yet-enforced
- [x] Stdlib-only checker + demo assets + recorded report

## v0.2 — 2026-12 (RQ1 hardening)

- [ ] Re-encode canon schema in SHACL over RDF (semantic-web constraint validation) and compare against the current JSON approach
- [ ] CIDOC-CRM alignment for the heritage entities
- [ ] Rule authoring guide so non-programmers can add rules

## v0.3 — 2027-01 (RQ3 benchmark seed)

- [ ] 50+ labelled generated-asset descriptions across categories (materials, technology, institutions, architecture)
- [ ] Inter-annotator agreement protocol on the labels
- [ ] Precision/recall metrics for the checker; first failure-mode taxonomy

## v0.4 — 2027-02 (RQ2 measurement)

- [ ] Pipe a real generative pipeline (image/video captioning or text-to-3D asset descriptions) into the checker
- [ ] Measure semantic-constraint propagation: which generation stages introduce violations

## v1.0 — 2027-03 (public benchmark)

- [ ] Public benchmark release with licence-cleared data
- [ ] Leaderboard format + baselines (CLIP-based zero-shot checker as baseline)
- [ ] Provenance ledger: record which canon clauses + human decisions each accepted output relied on
