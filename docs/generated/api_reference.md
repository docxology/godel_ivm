# Complete API Reference - IVM Polyhedron Visualization System

This document provides comprehensive API documentation for all components of the IVM system.

## 📋 Table of Contents

- [IVMSystem](#ivmsystem)
- [IVMCoordinates](#ivmcoordinates)
- [IVMVisualizer](#ivmvisualizer)
- [IVMConfig](#ivmconfig)
- [Data Structures](#data-structures)
- [Error Handling](#error-handling)
- [Examples](#examples)

## 🎯 IVMSystem

Main command-line interface providing unified access to all IVM functionality.

### Constructor
```python
IVMSystem()
```

### Core Methods

#### `plot_polyhedron(polyhedron_type: str, frequency: str, show_vectors: bool = False, save_path: Optional[str] = None) -> None`

Create static 3D plot of specified polyhedron.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type ('tetrahedron', 'octahedron', 'cube', 'cuboctahedron', 'truncated_tetrahedron', 'tetrakaidecahedron')
- `frequency` (str): Frequency as string ('0', '1', '2', '3', '4')
- `show_vectors` (bool, optional): Display vector connections to origin. Defaults to False.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Raises:**
- `ValueError`: If polyhedron type or frequency not found

**Example:**
```python
ivm = IVMSystem()
ivm.plot_polyhedron('tetrahedron', '1', show_vectors=True)
```

#### `animate_transformation(polyhedron_type: str, frequency: str, frames: Optional[int] = None, save_path: Optional[str] = None) -> None`

Create sphere-to-vector transformation animation.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (str): Frequency as string
- `frames` (int, optional): Number of animation frames. Uses config default if not provided.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Raises:**
- `ValueError`: If polyhedron type or frequency not found

**Example:**
```python
ivm.animate_transformation('tetrahedron', '2', frames=60)
```

#### `compare_polyhedrons(comparisons: List[Tuple[str, str]], save_path: Optional[str] = None) -> None`

Create side-by-side comparison of multiple polyhedrons.

**Parameters:**
- `comparisons` (List[Tuple[str, str]]): List of (polyhedron_type, frequency) tuples
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Raises:**
- `ValueError`: If any polyhedron type or frequency not found

**Example:**
```python
comparisons = [('tetrahedron', '1'), ('octahedron', '1'), ('cube', '1')]
ivm.compare_polyhedrons(comparisons)
```

### Documentation Methods

#### `create_documentation(output_dir: Optional[str] = None) -> None`

Generate comprehensive coordinate documentation.

**Parameters:**
- `output_dir` (str, optional): Custom output directory. Uses config default if not provided.

**Example:**
```python
ivm.create_documentation('custom_docs')
```

#### `create_comprehensive_visualizations() -> None`

Create all conceptual visualizations from Noel Coughlin's IVM coordinate paper.

**Example:**
```python
ivm.create_comprehensive_visualizations()
```

#### `create_comprehensive_animations() -> None`

Create all animation sequences.

**Example:**
```python
ivm.create_comprehensive_animations()
```

#### `create_additional_visualizations() -> None`

Create advanced visualization types (vector fields, energy flows, etc.).

**Example:**
```python
ivm.create_additional_visualizations()
```

#### `create_html_visualizations() -> None`

Generate interactive HTML interface.

**Example:**
```python
ivm.create_html_visualizations()
```

#### `create_comprehensive_output_package() -> None`

Generate complete output package with all visualizations.

**Example:**
```python
ivm.create_comprehensive_output_package()
```

### Utility Methods

#### `run_tests() -> unittest.TestResult`

Execute complete test suite.

**Returns:**
- `unittest.TestResult`: Test execution results

**Example:**
```python
results = ivm.run_tests()
if not results.wasSuccessful():
    print("Tests failed!")
```

#### `list_available_data() -> None`

Display available polyhedrons and frequencies.

**Example:**
```python
ivm.list_available_data()
```

## 🧮 IVMCoordinates

Manages all polyhedron coordinate data from Noel Coughlin's IVM coordinate specifications.

### Constructor
```python
IVMCoordinates(config: Optional[IVMConfig] = None)
```

### Core Methods

#### `get_polyhedron(polyhedron_type: str, frequency: int, orientation: str = 'correct') -> PolyhedronData`

Get coordinate data for specific polyhedron.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (int): Frequency number
- `orientation` (str, optional): Orientation type ('first' or 'correct'). Defaults to 'correct'.

**Returns:**
- `PolyhedronData`: Complete polyhedron data structure

**Raises:**
- `ValueError`: If polyhedron type or frequency not found

**Example:**
```python
coords = IVMCoordinates()
tetra_data = coords.get_polyhedron('tetrahedron', 1)
```

#### `list_polyhedrons() -> List[str]`

Get list of all available polyhedron types.

**Returns:**
- `List[str]`: List of polyhedron type names

**Example:**
```python
types = coords.list_polyhedrons()
# ['tetrahedron', 'octahedron', 'cube', 'cuboctahedron', 'truncated_tetrahedron', 'tetrakaidecahedron']
```

#### `list_frequencies(polyhedron_type: str) -> List[int]`

Get list of all available frequencies for a polyhedron type.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type

**Returns:**
- `List[int]`: List of available frequencies

**Raises:**
- `ValueError`: If polyhedron type not found

**Example:**
```python
freqs = coords.list_frequencies('tetrahedron')
# [0, 1, 2, 3, 4]
```

#### `save_to_json(filename: str) -> None`

Save coordinate data to JSON file.

**Parameters:**
- `filename` (str): Output filename

**Example:**
```python
coords.save_to_json('my_coordinates.json')
```

## 🎨 IVMVisualizer

3D visualization and animation engine for IVM polyhedrons.

### Constructor
```python
IVMVisualizer(config: Optional[IVMConfig] = None)
```

### Plotting Methods

#### `plot_polyhedron(polyhedron_type: str, frequency: str, sphere_radius: float = 0.02, sphere_color: str = 'blue', show_vectors: bool = False, vector_length: float = 0.1, save_path: Optional[str] = None) -> None`

Create static 3D plot of polyhedron.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (str): Frequency as string
- `sphere_radius` (float, optional): Sphere display radius. Defaults to 0.02.
- `sphere_color` (str, optional): Sphere color. Defaults to 'blue'.
- `show_vectors` (bool, optional): Display vector connections. Defaults to False.
- `vector_length` (float, optional): Vector display length. Defaults to 0.1.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Example:**
```python
viz = IVMVisualizer()
viz.plot_polyhedron('tetrahedron', '1', show_vectors=True, sphere_color='red')
```

#### `animate_sphere_to_vector(polyhedron_type: str, frequency: str, frames: int = 30, interval: int = 100, save_path: Optional[str] = None) -> None`

Create sphere-to-vector transformation animation.

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (str): Frequency as string
- `frames` (int, optional): Number of animation frames. Defaults to 30.
- `interval` (int, optional): Frame interval in milliseconds. Defaults to 100.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Example:**
```python
viz.animate_sphere_to_vector('tetrahedron', '2', frames=60, interval=50)
```

#### `compare_polyhedrons(polyhedrons: List[Tuple[str, str]], save_path: Optional[str] = None) -> None`

Create side-by-side comparison of multiple polyhedrons.

**Parameters:**
- `polyhedrons` (List[Tuple[str, str]]): List of (polyhedron_type, frequency) tuples
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

**Example:**
```python
polyhedrons = [('tetrahedron', '1'), ('cube', '1'), ('octahedron', '1')]
viz.compare_polyhedrons(polyhedrons)
```

### Documentation Methods

#### `create_coordinate_documentation(output_dir: str = 'docs') -> None`

Generate comprehensive coordinate documentation.

**Parameters:**
- `output_dir` (str, optional): Output directory. Defaults to 'docs'.

**Example:**
```python
viz.create_coordinate_documentation('my_docs')
```

#### `create_comprehensive_visualizations() -> None`

Create all conceptual visualizations from Noel Coughlin's IVM coordinate paper.

**Example:**
```python
viz.create_comprehensive_visualizations()
```

#### `create_comprehensive_animations() -> None`

Create all animation sequences.

**Example:**
```python
viz.create_comprehensive_animations()
```

#### `create_additional_visualizations() -> None`

Create advanced visualization types.

**Example:**
```python
viz.create_additional_visualizations()
```

#### `create_html_visualizations() -> None`

Generate interactive HTML interface.

**Example:**
```python
viz.create_html_visualizations()
```

#### `create_comprehensive_output_package() -> None`

Generate complete output package.

**Example:**
```python
viz.create_comprehensive_output_package()
```

## ⚙️ IVMConfig

Configuration management for the IVM system.

### Constructor
```python
IVMConfig(config_file: Optional[str] = None)
```

### Configuration Access

#### `visualization_config` (VisualizationConfig)

Visualization settings dataclass.

**Attributes:**
- `figsize` (Tuple[int, int]): Figure size (width, height)
- `elevation` (int): Camera elevation angle
- `azimuth` (int): Camera azimuth angle
- `sphere_radius` (float): Sphere display radius
- `vector_length` (float): Vector display length
- `animation_frames` (int): Default animation frames
- `animation_interval` (int): Animation frame interval
- `output_dpi` (int): Output DPI
- `grid_alpha` (float): Grid transparency

#### `output_paths` (OutputPaths)

Output directory configuration.

**Attributes:**
- `plots_dir` (str): Plot output directory
- `animations_dir` (str): Animation output directory
- `docs_dir` (str): Documentation output directory
- `temp_dir` (str): Temporary files directory

#### `polyhedron_data` (Dict)

Loaded coordinate data for all polyhedrons.

#### `constants` (Dict)

Mathematical constants used in calculations.

### Path Generation Methods

#### `generate_plot_path(polyhedron_type: str, frequency: str, show_vectors: bool = False) -> str`

Generate standardized plot file path.

**Example:**
```python
path = config.generate_plot_path('tetrahedron', '1', show_vectors=True)
# Returns: "outputs/plots/tetrahedron_f1_vectors.png"
```

#### `generate_animation_path(polyhedron_type: str, frequency: str) -> str`

Generate standardized animation file path.

**Example:**
```python
path = config.generate_animation_path('tetrahedron', '1')
# Returns: "outputs/animations/tetrahedron_f1_animation.gif"
```

#### `generate_comparison_path(polyhedrons: List[Tuple[str, str]]) -> str`

Generate standardized comparison file path.

**Example:**
```python
polyhedrons = [('tetrahedron', '1'), ('cube', '1')]
path = config.generate_comparison_path(polyhedrons)
# Returns: "outputs/plots/comparison_tetrahedron_f1_cube_f1.png"
```

### Data Access Methods

#### `get_polyhedron_data(polyhedron_type: str, frequency: str) -> Dict`

Get data for specific polyhedron and frequency.

#### `list_polyhedron_types() -> List[str]`

Get list of all available polyhedron types.

#### `list_frequencies(polyhedron_type: str) -> List[str]`

Get list of all available frequencies for a polyhedron type.

#### `get_coordinates(polyhedron_type: str, frequency: str) -> List[Tuple[float, float, float]]`

Get coordinate list for specific polyhedron.

#### `get_sphere_count(polyhedron_type: str, frequency: str) -> int`

Get sphere count for specific polyhedron.

#### `get_orientation(polyhedron_type: str, frequency: str) -> str`

Get orientation for specific polyhedron.

### Management Methods

#### `add_polyhedron_data(polyhedron_type: str, frequency: str, data: Dict) -> None`

Add new polyhedron data.

#### `save_coordinates() -> None`

Save coordinate data to config file.

#### `cleanup_temp_files(older_than_hours: int = 24) -> None`

Clean up temporary files older than specified hours.

## 🏗️ Data Structures

### PolyhedronData

```python
@dataclass
class PolyhedronData:
    frequency: int                    # Frequency number
    sphere_count: int                 # Number of spheres
    coordinates: List[Tuple[float, float, float]]  # Coordinate list
    polyhedron_type: str             # Polyhedron type name
    orientation: str                 # Orientation type ('first' or 'correct')
```

**Usage:**
```python
data = coords.get_polyhedron('tetrahedron', 1)
print(f"Frequency: {data.frequency}")
print(f"Sphere count: {data.sphere_count}")
print(f"Coordinates: {len(data.coordinates)} points")
```

### VisualizationConfig

```python
@dataclass
class VisualizationConfig:
    figsize: Tuple[int, int] = (12, 9)      # Figure size
    elevation: int = 20                     # Camera elevation
    azimuth: int = 45                       # Camera azimuth
    sphere_radius: float = 0.02             # Sphere display radius
    vector_length: float = 0.1              # Vector display length
    animation_frames: int = 30              # Default animation frames
    animation_interval: int = 100           # Animation frame interval
    output_dpi: int = 300                   # Output DPI
    grid_alpha: float = 0.3                 # Grid transparency
```

### OutputPaths

```python
@dataclass
class OutputPaths:
    plots_dir: str = "outputs/plots"           # Plot output directory
    animations_dir: str = "outputs/animations" # Animation output directory
    docs_dir: str = "outputs/docs"             # Documentation output directory
    temp_dir: str = "outputs/temp"             # Temporary files directory
```

## 🚨 Error Handling

### Common Exceptions

#### ValueError
- Raised when polyhedron type not found
- Raised when frequency not found for polyhedron type
- Raised when invalid parameters provided

#### FileNotFoundError
- Raised when config file not found
- Raised when output directories cannot be created

#### OSError
- Raised when file operations fail
- Raised when directory creation fails

### Error Handling Patterns

```python
try:
    ivm.plot_polyhedron('tetrahedron', '1')
except ValueError as e:
    print(f"Plotting failed: {e}")
    # Handle gracefully

try:
    config = IVMConfig("missing_file.json")
except FileNotFoundError:
    print("Config file not found, using defaults")
    config = IVMConfig()
```

## 💡 Examples

### Complete Workflow
```python
from ivm_system import IVMSystem

# Initialize system
ivm = IVMSystem()

# List available data
ivm.list_available_data()

# Create basic visualization
ivm.plot_polyhedron('tetrahedron', '1')

# Create animation
ivm.animate_transformation('tetrahedron', '2', frames=60)

# Compare polyhedrons
ivm.compare_polyhedrons([('tetrahedron', '1'), ('cube', '1')])

# Generate complete package
ivm.create_comprehensive_output_package()

# Run tests
results = ivm.run_tests()
```

### Advanced Configuration
```python
from ivm_package.config import IVMConfig
from ivm_package.coordinates import IVMCoordinates
from ivm_package.visualizer import IVMVisualizer

# Custom configuration
config = IVMConfig("custom_config.json")
config.visualization_config.figsize = (16, 12)
config.output_paths.plots_dir = "my_plots"

# Use with components
coords = IVMCoordinates(config)
viz = IVMVisualizer(config)

# Access data
tetra_data = coords.get_polyhedron('tetrahedron', 1)
viz.plot_polyhedron('tetrahedron', '1')
```

### Mathematical Validation
```python
import numpy as np
from ivm_package.coordinates import IVMCoordinates

coords = IVMCoordinates()
tetra_data = coords.get_polyhedron('tetrahedron', 1)

# Verify unit vectors
magnitudes = [np.linalg.norm(coord) for coord in tetra_data.coordinates]
assert all(abs(mag - 1.0) < 1e-10 for mag in magnitudes)

# Verify center of mass
center = np.mean(tetra_data.coordinates, axis=0)
assert np.allclose(center, [0, 0, 0], atol=1e-10)

# Verify tetrahedral angles
for i in range(len(tetra_data.coordinates)):
    for j in range(i + 1, len(tetra_data.coordinates)):
        dot_product = np.dot(tetra_data.coordinates[i], tetra_data.coordinates[j])
        angle = np.degrees(np.arccos(dot_product))
        assert abs(angle - 109.47) < 0.1
```

---

*This complete API reference provides comprehensive documentation for all components and methods in the IVM Polyhedron Visualization System.*
