# Troubleshooting local runs

- Run `run.py` from the repository root with the interpreter from the
  [installation guide](quickstart-current.md). This lets the loader
  find the `configs/` directory and the local `src/` package.
- Run `python run.py list` to confirm the shape and its numeric
  frequency. Check that the requested output file exists after plotting.
- For file-only output, set `MPLBACKEND=Agg` and pass an explicit
  `--output` path whose parent directory exists.
- For manuscript issues, use the [pinned reproduction](../reproduce.md)
  and inspect its validation report. Its figure and evidence JSON are
  produced together by the local fixture check.

Keep the repository's tracked coordinate files available. Use a
separate checkout for alternative input configurations.
