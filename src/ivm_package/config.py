#!/usr/bin/env python3
"""
IVM Configuration Module
Handles all configuration data, coordinate loading, and output management
"""

import json
import os
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, asdict
import numpy as np

@dataclass
class VisualizationConfig:
    """Configuration for visualization settings"""
    figsize: Tuple[int, int] = (12, 9)
    elevation: int = 20
    azimuth: int = 45
    sphere_radius: float = 0.02
    vector_length: float = 0.1
    animation_frames: int = 30
    animation_interval: int = 100
    output_dpi: int = 300
    grid_alpha: float = 0.3

@dataclass
class OutputPaths:
    """Configuration for output file paths"""
    plots_dir: str = "outputs/plots"
    animations_dir: str = "outputs/animations"
    docs_dir: str = "outputs/docs"
    temp_dir: str = "outputs/temp"

class IVMConfig:
    """Configuration manager for IVM system"""

    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file or "configs/ivm_coordinates.json"
        self.visualization_config = VisualizationConfig()
        self.output_paths = OutputPaths()
        self.polyhedron_data: Dict[str, Dict[str, Dict[str, Any]]] = {}
        self.constants: Dict[str, float] = {}

        # Ensure output directories exist
        self._ensure_output_dirs()

        # Load coordinate data
        self._load_coordinates()

        # Load constants
        self._load_constants()

    def _ensure_output_dirs(self):
        """Ensure all output directories exist"""
        for path in [self.output_paths.plots_dir, self.output_paths.animations_dir,
                    self.output_paths.docs_dir, self.output_paths.temp_dir]:
            os.makedirs(path, exist_ok=True)

    def _load_coordinates(self):
        """Load coordinate data from config file"""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                self.polyhedron_data = json.load(f)
        else:
            # Create default coordinate data
            self._create_default_coordinates()

    def _load_constants(self):
        """Load mathematical constants"""
        self.constants = {
            'golden_ratio': 1.414213562,
            'sqrt_2': 1.414213562,
            'sqrt_3': 1.732050808,
            'sqrt_1_2': 0.707106781,
            'sqrt_1_8': 0.353553391
        }

    def _create_default_coordinates(self):
        """Create default coordinate data if config file doesn't exist"""
        self.polyhedron_data = {
            'tetrahedron': {
                '1': {
                    'frequency': 1,
                    'sphere_count': 4,
                    'orientation': 'correct',
                    'coordinates': [
                        (0.353553, 0.353553, 0.353553),
                        (-0.353553, -0.353553, 0.353553),
                        (0.353553, -0.353553, -0.353553),
                        (-0.353553, 0.353553, -0.353553)
                    ]
                }
            }
        }

        # Save default data
        self.save_coordinates()

    def save_coordinates(self):
        """Save coordinate data to config file"""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.polyhedron_data, f, indent=2)

    def get_polyhedron_data(self, polyhedron_type: str, frequency: str) -> Dict[str, Any]:
        """Get data for a specific polyhedron and frequency"""
        if polyhedron_type not in self.polyhedron_data:
            raise ValueError(f"Unknown polyhedron type: {polyhedron_type}")

        if frequency not in self.polyhedron_data[polyhedron_type]:
            raise ValueError(f"Unknown frequency {frequency} for {polyhedron_type}")

        return self.polyhedron_data[polyhedron_type][frequency]

    def list_polyhedron_types(self) -> List[str]:
        """List all available polyhedron types"""
        return list(self.polyhedron_data.keys())

    def list_frequencies(self, polyhedron_type: str) -> List[str]:
        """List all available frequencies for a polyhedron type"""
        if polyhedron_type not in self.polyhedron_data:
            raise ValueError(f"Unknown polyhedron type: {polyhedron_type}")
        return list(self.polyhedron_data[polyhedron_type].keys())

    def get_coordinates(self, polyhedron_type: str, frequency: str) -> List[Tuple[float, float, float]]:
        """Get coordinate list for a specific polyhedron"""
        data = self.get_polyhedron_data(polyhedron_type, frequency)
        return data['coordinates']

    def get_sphere_count(self, polyhedron_type: str, frequency: str) -> int:
        """Get sphere count for a specific polyhedron"""
        data = self.get_polyhedron_data(polyhedron_type, frequency)
        return data['sphere_count']

    def get_orientation(self, polyhedron_type: str, frequency: str) -> str:
        """Get orientation for a specific polyhedron"""
        data = self.get_polyhedron_data(polyhedron_type, frequency)
        return data['orientation']

    def add_polyhedron_data(self, polyhedron_type: str, frequency: str, data: Dict[str, Any]):
        """Add new polyhedron data"""
        if polyhedron_type not in self.polyhedron_data:
            self.polyhedron_data[polyhedron_type] = {}

        self.polyhedron_data[polyhedron_type][frequency] = data
        self.save_coordinates()

    def generate_plot_path(self, polyhedron_type: str, frequency: str,
                          show_vectors: bool = False) -> str:
        """Generate standardized plot file path"""
        vectors_suffix = "_vectors" if show_vectors else ""
        filename = f"{polyhedron_type}_f{frequency}{vectors_suffix}.png"
        return os.path.join(self.output_paths.plots_dir, filename)

    def generate_animation_path(self, polyhedron_type: str, frequency: str) -> str:
        """Generate standardized animation file path"""
        filename = f"{polyhedron_type}_f{frequency}_animation.gif"
        return os.path.join(self.output_paths.animations_dir, filename)

    def generate_comparison_path(self, polyhedrons: List[Tuple[str, str]]) -> str:
        """Generate standardized comparison file path"""
        poly_str = "_".join([f"{p}_f{f}" for p, f in polyhedrons])
        filename = f"comparison_{poly_str}.png"
        return os.path.join(self.output_paths.plots_dir, filename)

    def generate_docs_path(self, polyhedron_type: str) -> str:
        """Generate standardized documentation file path"""
        filename = f"{polyhedron_type}_coordinates.md"
        return os.path.join(self.output_paths.docs_dir, filename)

    def generate_index_path(self) -> str:
        """Generate standardized documentation index path"""
        filename = "coordinates_index.md"
        return os.path.join(self.output_paths.docs_dir, filename)

    def get_temp_path(self, filename: str) -> str:
        """Generate temporary file path"""
        return os.path.join(self.output_paths.temp_dir, filename)

    def cleanup_temp_files(self, older_than_hours: int = 24):
        """Clean up temporary files older than specified hours"""
        import time
        import glob

        temp_files = glob.glob(os.path.join(self.output_paths.temp_dir, "*"))
        current_time = time.time()

        for temp_file in temp_files:
            file_age = current_time - os.path.getmtime(temp_file)
            if file_age > (older_than_hours * 3600):  # Convert hours to seconds
                try:
                    os.remove(temp_file)
                except OSError:
                    pass  # File might have been deleted already

    def get_config_summary(self) -> Dict[str, Any]:
        """Get summary of current configuration"""
        return {
            'config_file': self.config_file,
            'polyhedron_types': len(self.polyhedron_data),
            'visualization_config': asdict(self.visualization_config),
            'output_paths': asdict(self.output_paths),
            'constants': self.constants
        }

# Global config instance
_config_instance = None

def get_config() -> IVMConfig:
    """Get global config instance (singleton pattern)"""
    global _config_instance
    if _config_instance is None:
        _config_instance = IVMConfig()
    return _config_instance

def reset_config():
    """Reset global config instance"""
    global _config_instance
    _config_instance = None

# Default configuration for easy access
default_config = IVMConfig()
