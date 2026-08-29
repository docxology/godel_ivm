# Agent guide — docs/ (godel_ivm)

## Layout

- `README.md` — entry point; links the interactive interface, coordinate data, and source tree.
- `api/` — module API reference (`config.md`, `coordinates.md`, `system.md`).
- `generated/` — generated reference pages (`api_reference.md`, `test_coverage.md`,
  `mathematical_foundation.md`) plus this tree's own `README.md`.
- `guides/` — user guides (`installation.md`, `troubleshooting.md`).
- Coordinate guides at the top level (`cube_`, `tetrahedron_`, `octahedron_`,
  `cuboctahedron_`, `tetrakaidecahedron_`, `truncated_tetrahedron_coordinates.md`,
  `coordinates_index.md`).
- `original/` — preserved source material.

## Conventions

- Generated pages describe produced outputs; regenerate them rather than hand-editing.
- Links from `docs/` into repo-level trees (`src/`, `tests/`, `configs/`, `outputs/`)
  must be repo-root-relative from the *linking file's* directory (i.e. `../` prefixes).

## Maintenance

- Keep this guide and `docs/README.md` consistent with the actual tree; every
  factual claim must be checkable against a file in the repo.
