"""Run the local coordinate and plotting checks for the manuscript."""

from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from ivm_package.coordinates import IVMCoordinates


def main() -> None:
    tetrahedron = IVMCoordinates().get_polyhedron("tetrahedron", 1)
    points = np.asarray(tetrahedron.coordinates)
    distances = np.array([np.linalg.norm(a - b) for a, b in combinations(points, 2)])
    centroid = points.mean(axis=0)
    if points.shape != (4, 3) or tetrahedron.sphere_count != 4:
        raise ValueError("The frequency-one tetrahedron should have four 3D points.")
    if not np.allclose(centroid, 0.0, rtol=0.0, atol=1e-9):
        raise ValueError(f"The tetrahedron centroid is {centroid}, outside the expected tolerance.")
    if not np.allclose(distances, 1.0, rtol=0.0, atol=2e-6):
        raise ValueError(f"The tetrahedron edge lengths differ from unit length: {distances}.")

    figures = ROOT / "output" / "figures"
    figures.mkdir(parents=True, exist_ok=True)
    image_path = figures / "tetrahedron-f1.png"
    subprocess.run(
        [sys.executable, "run.py", "plot", "tetrahedron", "1", "--output", str(image_path)],
        check=True,
        cwd=ROOT,
    )
    with Image.open(image_path) as image:
        if image.format != "PNG":
            raise ValueError("The native plot should be a PNG.")
        image.verify()

    data = ROOT / "output" / "data"
    data.mkdir(exist_ok=True)
    evidence = {
        "shape": "tetrahedron",
        "frequency": tetrahedron.frequency,
        "points": len(points),
        "edges": len(distances),
        "centroid": centroid.tolist(),
        "edge_length_rounded": round(float(distances.mean()), 5),
    }
    registry = {
        "figures": [{
            "label": "fig:tetrahedron-fixture",
            "filename": image_path.name,
            "caption": "Native visualization of the frequency-one tetrahedron.",
            "alt_text": "Four plotted points form a tetrahedron about the origin on three Cartesian axes.",
            "generated_by": "run.py plot tetrahedron 1",
        }],
    }
    (data / "geometry-evidence.json").write_text(json.dumps(evidence, indent=2) + "\n")
    (figures / "figure_registry.json").write_text(json.dumps(registry, indent=2) + "\n")
    print("Verified the tetrahedron coordinates, six distances, and decoded native PNG.")


if __name__ == "__main__":
    main()
