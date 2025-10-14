#!/usr/bin/env python3
"""
IVM Polyhedron Coordinate Data
Organized coordinate data for all polyhedrons in the Isotropic Vector Matrix
Based on xyz_clean.md specifications
"""

from typing import Dict, List, Tuple
from dataclasses import dataclass
import json

@dataclass
class PolyhedronData:
    """Data structure for a polyhedron at a specific frequency"""
    frequency: int
    sphere_count: int
    coordinates: List[Tuple[float, float, float]]
    polyhedron_type: str
    orientation: str

class IVMCoordinates:
    """Container for all IVM polyhedron coordinate data"""

    def __init__(self):
        self.polyhedrons: Dict[str, Dict[int, PolyhedronData]] = {
            'tetrahedron': {},
            'octahedron': {},
            'cube': {},
            'cuboctahedron': {},
            'truncated_tetrahedron': {},
            'tetrakaidecahedron': {}
        }

        self.constants = {
            'golden_ratio': 1.414213562,
            'sqrt_2': 1.414213562,
            'sqrt_3': 1.732050808,
            'sqrt_1_2': 0.707106781,
            'sqrt_1_8': 0.353553391
        }

        self._load_coordinates()

    def _load_coordinates(self):
        """Load all coordinate data from organized structures"""

        # ========================================
        # TETRAHEDRON COORDINATES
        # ========================================

        # Section B: First Orientation
        self.polyhedrons['tetrahedron'][0] = PolyhedronData(
            frequency=0,
            sphere_count=1,
            coordinates=[(0, 0, 0)],
            polyhedron_type='tetrahedron',
            orientation='first'
        )

        self.polyhedrons['tetrahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=4,
            coordinates=[
                (0.5, 0, 0.35355339), (-0.5, 0, 0.35355339),
                (0, 0.5, -0.35355339), (0, -0.5, -0.35355339)
            ],
            polyhedron_type='tetrahedron',
            orientation='first'
        )

        self.polyhedrons['tetrahedron'][2] = PolyhedronData(
            frequency=2,
            sphere_count=10,
            coordinates=[
                # 4 vertices
                (1, 0, 0.7071067), (-1, 0, 0.7071067),
                (0, 1, -0.7071067), (0, -1, -0.7071067),
                # 6 octahedron vertices
                (0.5, 0.5, 0), (0.5, -0.5, 0), (-0.5, 0.5, 0),
                (-0.5, -0.5, 0), (0, 0, 0.7071067), (0, 0, -0.7071067)
            ],
            polyhedron_type='tetrahedron',
            orientation='first'
        )

        self.polyhedrons['tetrahedron'][3] = PolyhedronData(
            frequency=3,
            sphere_count=20,
            coordinates=[
                # 4 vertices
                (1.5, 0, 1.06066), (-1.5, 0, 1.06066),
                (0, 1.5, -1.06066), (0, -1.5, 1.06066),
                # 4 inverted tetrahedron vertices
                (0, 0.5, 0.35355), (0, -0.5, 0.35355),
                (0.5, 0, -0.35355), (-0.5, 0, -0.35355),
                # 12 truncated tetrahedron vertices
                (0.5, 0, 1.06066), (-0.5, 0, 1.06066),
                (1, -0.5, 0.35355), (-1, -0.5, 0.35355),
                (1, 0.5, 0.35355), (-1, 0.5, 0.35355),
                (0.5, -1, -0.35355), (-0.5, -1, -0.35355),
                (0.5, 1, 0.35355), (-0.5, 1, 0.35355),
                (0, 0.5, -1.06066), (0, -0.5, -1.06066)
            ],
            polyhedron_type='tetrahedron',
            orientation='first'
        )

        self.polyhedrons['tetrahedron'][4] = PolyhedronData(
            frequency=4,
            sphere_count=35,
            coordinates=[
                # 1 center sphere
                (0, 0, 0),
                # 12 cuboctahedron vertices
                (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
                (0.5, -0.5, 0.7071067), (-0.5, -0.5, 0.7071067),
                (0.5, 0.5, 0.7071067), (-0.5, 0.5, 0.707106),
                (0.5, -0.5, -0.707106), (-0.5, -0.5, -0.707106),
                (0.5, 0.5, -0.707106), (-0.5, 0.5, -0.707106),
                # 6 octahedron vertices
                (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0),
                (0, 0, 1.414214), (0, 0, -1.414214),
                # 16 tetrahedron vertices
                (1, 1.5, 0.707106), (1.5, -0.5, 0.707106),
                (-1.5, 0.5, 0.707106), (-1.5, -0.5, 0.707106),
                (1, 0, 1.41421), (2, 0, 1.41421), (-1, 0, 1.41421), (-2, 0, 1.41421),
                (0.5, 1.5, -0.707106), (-0.5, 1.5, -0.707106),
                (0.5, -1.5, -0.707106), (-0.5, -1.5, -0.707106),
                (0, 1, -1.41421), (0, 2, -1.41421), (0, -1, -1.41421), (0, -2, -1.41421)
            ],
            polyhedron_type='tetrahedron',
            orientation='first'
        )

        # Section C: Correct Orientation - All frequencies use correct orientation
        # Frequency 1
        self.polyhedrons['tetrahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=4,
            coordinates=[
                (0.353553, 0.353553, 0.353553), (-0.353553, -0.353553, 0.353553),
                (0.353553, -0.353553, -0.353553), (-0.353553, 0.353553, -0.353553)
            ],
            polyhedron_type='tetrahedron',
            orientation='correct'
        )

        # Frequency 2
        self.polyhedrons['tetrahedron'][2] = PolyhedronData(
            frequency=2,
            sphere_count=10,
            coordinates=[
                (0.7071067, 0.7071067, 0.7071067), (-0.7071067, -0.7071067, 0.7071067),
                (0.7071067, -0.7071067, -0.7071067), (-0.7071067, 0.7071067, -0.7071067),
                (0.7071067, 0, 0), (-0.7071067, 0, 0),
                (0, 0.7071067, 0), (0, -0.7071067, 0),
                (0, 0, 0.7071067), (0, 0, -0.7071067)
            ],
            polyhedron_type='tetrahedron',
            orientation='correct'
        )

        # Frequency 3
        self.polyhedrons['tetrahedron'][3] = PolyhedronData(
            frequency=3,
            sphere_count=20,
            coordinates=[
                (1.06066, 1.06066, 1.06066), (-1.06066, -1.06066, 1.06066),
                (1.06066, -1.06066, -1.06066), (-1.06066, 1.06066, -1.06066),
                (-0.353553, -0.353553, -0.353553), (0.353553, 0.353553, -0.353553),
                (-0.353553, 0.353553, 0.353553), (0.353553, -0.353553, 0.353553),
                (0.353553, 0.353553, 1.06066), (-0.353553, -0.353553, 1.06066),
                (-0.353553, 0.353553, -1.06066), (0.353553, -0.353553, -1.06066),
                (1.06066, 0.353553, 0.353553), (0.353553, 1.06066, 0.353553),
                (-1.06066, -0.353553, 0.353553), (-0.353553, -1.06066, 0.353553),
                (1.06066, -0.353553, -0.353553), (0.353553, -1.06066, -0.353553),
                (-0.353553, 1.06066, -0.353553), (-1.06066, 0.353553, -0.353553)
            ],
            polyhedron_type='tetrahedron',
            orientation='correct'
        )

        # Frequency 4
        self.polyhedrons['tetrahedron'][4] = PolyhedronData(
            frequency=4,
            sphere_count=35,
            coordinates=[
                (0, 0, 0), (0.7071067, 0.7071067, 0), (0.7071067, -0.7071067, 0),
                (-0.7071067, 0.7071067, 0), (-0.7071067, -0.7071067, 0),
                (0.7071067, 0, 0.7071067), (0, 0.7071067, 0.7071067),
                (-0.7071067, 0, 0.7071067), (0, -0.7071067, 0.7071067),
                (0.7071067, 0, -0.7071067), (0, 0.7071067, -0.7071067),
                (-0.7071067, 0, -0.7071067), (0, -0.7071067, -0.7071067),
                (0, 0, 1.41421), (0, 0, -1.41421), (1.41421, 0, 0), (-1.41421, 0, 0),
                (0, 1.41421, 0), (0, -1.41421, 0), (1.41421, 1.41421, 1.41421),
                (-1.41421, -1.41421, 1.41421), (1.41421, -1.41421, -1.41421),
                (-1.41421, 1.41421, -1.41421), (0.707, 0.707, 1.414),
                (-0.707, -0.707, 1.414), (0.707, -0.707, -1.414),
                (-0.707, 0.707, -1.414), (1.414, 0.707, 0.707),
                (0.707, 1.414, 0.707), (-1.414, -0.707, 0.707),
                (-0.707, -1.414, 0.707), (0.707, -1.414, -0.707),
                (1.414, -0.707, -0.707), (-0.707, 1.414, -0.707),
                (-1.414, 0.707, -0.707)
            ],
            polyhedron_type='tetrahedron',
            orientation='correct'
        )

        # ========================================
        # OCTAHEDRON COORDINATES
        # ========================================

        self.polyhedrons['octahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=6,
            coordinates=[
                (0.7071067, 0, 0), (-0.7071067, 0, 0),
                (0, 0.7071067, 0), (0, -0.7071067, 0),
                (0, 0, 0.7071067), (0, 0, -0.7071067)
            ],
            polyhedron_type='octahedron',
            orientation='correct'
        )

        # ========================================
        # CUBE COORDINATES
        # ========================================

        self.polyhedrons['cube'][1] = PolyhedronData(
            frequency=1,
            sphere_count=14,
            coordinates=[
                (-0.7071067, 0.7071067, 0.7071067), (-0.7071067, -0.7071067, -0.7071067),
                (0.7071067, 0.7071067, -0.7071067), (0.7071067, -0.7071067, 0.7071067),
                (1, 0, 0.7071067), (-1, 0, 0.7071067),
                (0, 1, -0.7071067), (0, -1, -0.7071067),
                (0.7071067, 0, 0), (-0.7071067, 0, 0),
                (0, 0.7071067, 0), (0, -0.7071067, 0),
                (0, 0, 0.7071067), (0, 0, -0.7071067)
            ],
            polyhedron_type='cube',
            orientation='correct'
        )

        # ========================================
        # CUBOCTAHEDRON COORDINATES
        # ========================================

        self.polyhedrons['cuboctahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=13,
            coordinates=[
                (0, 0, 0), (0.7071067, 0.7071067, 0), (0.7071067, -0.7071067, 0),
                (-0.7071067, 0.7071067, 0), (-0.7071067, -0.7071067, 0),
                (0.7071067, 0, 0.7071067), (0, 0.7071067, 0.7071067),
                (-0.7071067, 0, 0.7071067), (0, -0.7071067, 0.7071067),
                (0.7071067, 0, -0.7071067), (0, 0.7071067, -0.7071067),
                (-0.7071067, 0, -0.7071067), (0, -0.7071067, -0.7071067)
            ],
            polyhedron_type='cuboctahedron',
            orientation='correct'
        )

        # ========================================
        # TRUNCATED TETRAHEDRON COORDINATES
        # ========================================

        self.polyhedrons['truncated_tetrahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=12,
            coordinates=[
                (0.353553, 0.353553, 1.06066), (-0.353553, -0.353553, 1.06066),
                (-0.353553, 0.353553, -1.06066), (0.353553, -0.353553, -1.06066),
                (1.06066, 0.353553, 0.353553), (0.353553, 1.06066, 0.353553),
                (-1.06066, -0.353553, 0.353553), (-0.353553, -1.06066, 0.353553),
                (1.06066, -0.353553, -0.353553), (0.353553, -1.06066, -0.353553),
                (-0.353553, 1.06066, -0.353553), (-1.06066, 0.353553, -0.353553)
            ],
            polyhedron_type='truncated_tetrahedron',
            orientation='correct'
        )

        # ========================================
        # TETRAKAIDECAHEDRON COORDINATES
        # ========================================

        self.polyhedrons['tetrakaidecahedron'][1] = PolyhedronData(
            frequency=1,
            sphere_count=38,
            coordinates=[
                (0.707, 0, 1.414), (-0.707, 0, 1.414), (0, 0.707, 1.414), (0, -0.707, 1.414),
                (0.707, 0, -1.414), (-0.707, 0, -1.414), (0, 0.707, -1.414), (0, -0.707, -1.414),
                (1.414, 0, 0.707), (-1.414, 0, 0.707), (0, 1.414, 0.707), (0, -1.414, 0.707),
                (1.414, 0, -0.707), (-1.414, 0, -0.707), (0, 1.414, -0.707), (0, -1.414, -0.707),
                (1.414, 0.707, 0), (0.707, 1.414, 0), (1.414, -0.707, 0), (0.707, -1.414, 0),
                (-0.707, 1.414, 0), (-1.414, 0.707, 0), (-0.707, -1.414, 0), (-1.414, -0.707, 0),
                (-0.7071067, 0.7071067, 0.7071067), (-0.7071067, -0.7071067, -0.7071067),
                (0.7071067, 0.7071067, -0.7071067), (0.7071067, -0.7071067, 0.7071067),
                (1, 0, 0.7071067), (-1, 0, 0.7071067), (0, 1, -0.7071067), (0, -1, -0.7071067),
                (0.7071067, 0, 0), (-0.7071067, 0, 0), (0, 0.7071067, 0), (0, -0.7071067, 0),
                (0, 0, 0.7071067), (0, 0, -0.7071067)
            ],
            polyhedron_type='tetrakaidecahedron',
            orientation='correct'
        )

    def get_polyhedron(self, polyhedron_type: str, frequency: int, orientation: str = 'correct') -> PolyhedronData:
        """Get coordinate data for a specific polyhedron"""
        if polyhedron_type not in self.polyhedrons:
            raise ValueError(f"Unknown polyhedron type: {polyhedron_type}")

        if frequency not in self.polyhedrons[polyhedron_type]:
            raise ValueError(f"Unknown frequency {frequency} for {polyhedron_type}")

        return self.polyhedrons[polyhedron_type][frequency]

    def list_polyhedrons(self) -> List[str]:
        """List all available polyhedron types"""
        return list(self.polyhedrons.keys())

    def list_frequencies(self, polyhedron_type: str) -> List[int]:
        """List all available frequencies for a polyhedron type"""
        if polyhedron_type not in self.polyhedrons:
            raise ValueError(f"Unknown polyhedron type: {polyhedron_type}")
        return list(self.polyhedrons[polyhedron_type].keys())

    def save_to_json(self, filename: str):
        """Save coordinate data to JSON file"""
        data = {}
        for poly_type, frequencies in self.polyhedrons.items():
            data[poly_type] = {}
            for freq, poly_data in frequencies.items():
                data[poly_type][freq] = {
                    'frequency': poly_data.frequency,
                    'sphere_count': poly_data.sphere_count,
                    'coordinates': poly_data.coordinates,
                    'polyhedron_type': poly_data.polyhedron_type,
                    'orientation': poly_data.orientation
                }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

# Create global instance
ivm_coords = IVMCoordinates()

if __name__ == "__main__":
    # Save organized data
    ivm_coords.save_to_json('ivm_coordinates_organized.json')

    # Print summary
    print("IVM Coordinate Data Summary:")
    print("=" * 50)
    for poly_type in ivm_coords.list_polyhedrons():
        print(f"\n{poly_type.title()}:")
        for freq in ivm_coords.list_frequencies(poly_type):
            data = ivm_coords.get_polyhedron(poly_type, freq)
            print(f"  Frequency {freq}: {data.sphere_count} spheres ({data.orientation} orientation)")
