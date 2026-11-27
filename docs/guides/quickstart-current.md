# Install and plot a model

The project runs directly from a checkout. Have `python3.14` available
with its `venv` module. The commands below install NumPy 2.5.5,
Matplotlib 3.11.2 and Pillow 13.0.0.

```bash
git clone https://github.com/docxology/godel_ivm.git
cd godel_ivm
python3.14 -m venv .venv
.venv/bin/python -m pip install numpy==2.5.5 matplotlib==3.11.2 Pillow==13.0.0
.venv/bin/python run.py list
mkdir -p output
MPLBACKEND=Agg .venv/bin/python run.py plot tetrahedron 1 --output output/tetrahedron.png
```

The positional frequency is numeric. The example writes a PNG without
opening a window. Use `.venv/bin/python run.py --help` to inspect
supported operations.

Run tests from the root with
`MPLBACKEND=Agg .venv/bin/python -m unittest discover -s tests -v`.
Use a disposable checkout for broad visualization and test work
because the native commands can write generated files beneath
`outputs/`. The [manuscript reproduction](../reproduce.md) prepares
its own build artifacts beneath `output/`.
