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
The public snapshot is manually refreshed, not a scheduled or automatic live feed.

Public source: SLU SOS WFS / Artportalen. Exact Åstorp municipality, birds, positive
observations, 2025 and 2026 to 29 October. All three count checks agree per year;
this does not imply an atomic database snapshot. Protected records are unavailable.
Person statistics and all-time municipal firsts remain blocked by missing identity
and historical coverage. Taxonomy follows AviList v2026 (20 October 2026), with the existing feral-pigeon inclusion within Columba livia. Artfakta identifiers are retained only as source identifiers. See the visible scope notice for remaining limitations.
