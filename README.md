# birds_Astorp-preview
Separate Hugo preview export. Canonical source: hktcr/birds_Astorp at a4b196d. Production astorpsfaglar.se is unchanged.

## Municipal preview, 29 October 2026

The three municipal prototypes are built by `python3 scripts/build-municipal-preview.py`.
Their source is intentionally kept in this separate preview repository; no production
Hugo source or deployment is changed by this experiment.

`node scripts/test-municipal-preview.cjs` checks the public aggregate, date comparisons,
error handling contracts, duplicate IDs, links and absence of private data fields.
`prepare-municipal-snapshot.py` accepts local, verified WFS evidence and publishes only
first-date aggregates, never raw observations. It does not contact an API or deploy.
The static public snapshot is a dated fallback. municipal-preview-live.js now fetches public WFS data on page load (15-minute aggregate-only session cache) or manual refresh, with a frozen upper UTC boundary, before/full/after count checks and disjoint time partitioning at the 5000 cap. It never publishes partial totals. Historical comparison is on-demand. No scheduled job, key, server, or new account was added.

Public source: SLU SOS WFS / Artportalen. Exact Åstorp municipality, birds, positive
observations, 2025 and 2026 to 29 October. All three count checks agree per year;
this does not imply an atomic database snapshot. Protected records are unavailable.
Person statistics and all-time municipal firsts remain blocked by missing identity
and historical coverage. Taxonomy follows AviList v2026 (20 October 2026), with the existing feral-pigeon inclusion within Columba livia. Artfakta identifiers are retained only as source identifiers. See the visible scope notice for remaining limitations.

## API and visual revision, 29 October evening

Run `node scripts/test-municipal-live.cjs`, `node scripts/test-municipal-ui.cjs`,
and `node scripts/test-municipal-preview.cjs`. Live API evidence is a separate
check, not a substitute for these deterministic error/empty/mapping tests.
The visible views reuse the existing logo and font/palette rules.
`data/municipal-taxonomy.json` contains the official AviList v2026 species names
and identifiers, separately verified source-parent mappings and explicit synonyms.
New unmapped taxa block a fresh total rather than being silently discarded.
Only public positive, naturally occurring, non-uncertain bird records in the exact
municipality Åstorp are queried. No geometry or person fields are requested for statistics. The separate on-demand credits request fetches only the public reportedBy/recordedBy strings for exact already-public sighting IDs, displaying their distinct source roles without identity merging. Names are not written to the repository or session cache.
Reporter ranking remains blocked: public strings are not stable identities.
Historical absence is not proof of real-world absence or a first-ever municipal record.
