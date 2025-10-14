"""
IVM Package - Isotropic Vector Matrix Visualization System

A comprehensive package for visualizing polyhedrons from the Isotropic Vector Matrix (IVM)
coordinate system based on R. Buckminster Fuller's Synergetics geometry.
"""

from .coordinates import IVMCoordinates, PolyhedronData
from .visualizer import IVMVisualizer
from .config import IVMConfig, get_config

__version__ = "1.0.0"
__author__ = "IVM Visualization Team"
__all__ = ["IVMCoordinates", "PolyhedronData", "IVMVisualizer", "IVMConfig", "get_config"]
