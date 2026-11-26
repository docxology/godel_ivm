# Install and plot a model

The project runs directly from a checkout. The verified local
environment used Python 3.14, NumPy 2.5.5, Matplotlib 3.11.2 and
Pillow 13.0.0.

```bash
git clone https://github.com/docxology/godel_ivm.git
cd godel_ivm
python3 -m venv .venv
.venv/bin/python -m pip install numpy==2.5.5 matplotlib==3.11.2 Pillow==13.0.0
.venv/bin/python run.py list
mkdir -p output
MPLBACKEND=Agg .venv/bin/python run.py plot tetrahedron 1 --output output/tetrahedron.png
```

The positional frequency is numeric. The example writes a PNG without
opening a window. Use `python run.py --help` with the installed
interpreter to inspect supported operations.

Run tests from the root with
`MPLBACKEND=Agg .venv/bin/python -m unittest discover -s tests -v`.
Use a disposable checkout for broad visualization and test work
because the native commands can write generated files beneath
`outputs/`. The [manuscript reproduction](../reproduce.md) prepares
its own build artifacts beneath `output/`.
