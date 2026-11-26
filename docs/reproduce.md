# Build the geometry manuscript

Use a separate [Docxology Template](https://github.com/docxology/template)
checkout with Pandoc, pandoc-crossref, and XeLaTeX installed. From the
IVM checkout:

```bash
template_dir=/absolute/path/to/template
git -C "$template_dir" switch --detach 87704feae0a4490ef7dad9c931d268e8c30273c2
mkdir -p "$template_dir/projects/working"
git worktree add --detach "$template_dir/projects/working/godel_ivm" HEAD
cd "$template_dir"
uv sync --locked --python 3.14 --no-dev
MPLBACKEND=Agg uv run --no-sync python projects/working/godel_ivm/docs/reproduce_geometry.py
uv run --no-sync python scripts/pipeline/stage_03_render.py --project working/godel_ivm
uv run --no-sync python scripts/pipeline/stage_04_validate.py --project working/godel_ivm
```

The figure, local measurement, PDF, HTML and validation receipts are
written to `projects/working/godel_ivm/output/`.
