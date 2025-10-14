# IVMConfig API Documentation

Complete API documentation for the IVMConfig class.

## Overview

The `IVMConfig` class manages configuration settings, output paths, and coordinate data loading for the IVM system.

## Constructor

```python
IVMConfig(config_file: Optional[str] = None)
```

**Parameters:**
- `config_file` (str, optional): Custom config file path. Uses default if not provided.

## Configuration Access

### `visualization_config` (VisualizationConfig)

Visualization settings (figsize, elevation, azimuth, etc.).

### `output_paths` (OutputPaths)

Output directory paths for plots, animations, docs.

### `polyhedron_data` (Dict)

Loaded coordinate data for all polyhedrons.

### `constants` (Dict)

Mathematical constants used in calculations.

## Path Generation Methods

### `generate_plot_path(polyhedron_type: str, frequency: str, show_vectors: bool = False) -> str`

Generate standardized plot file path.

```python
path = config.generate_plot_path('tetrahedron', '1', show_vectors=True)
# Returns: "outputs/plots/tetrahedron_f1_vectors.png"
```

### `generate_animation_path(polyhedron_type: str, frequency: str) -> str`

Generate standardized animation file path.

```python
path = config.generate_animation_path('tetrahedron', '1')
# Returns: "outputs/animations/tetrahedron_f1_animation.gif"
```

### `generate_comparison_path(polyhedrons: List[Tuple[str, str]]) -> str`

Generate standardized comparison file path.

```python
polyhedrons = [('tetrahedron', '1'), ('cube', '1')]
path = config.generate_comparison_path(polyhedrons)
# Returns: "outputs/plots/comparison_tetrahedron_f1_cube_f1.png"
```

### `generate_docs_path(polyhedron_type: str) -> str`

Generate standardized documentation file path.

```python
path = config.generate_docs_path('tetrahedron')
# Returns: "outputs/docs/tetrahedron_coordinates.md"
```

## Configuration Classes

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

## Usage Examples

### Basic Configuration Access
```python
from ivm_package.config import IVMConfig

config = IVMConfig()

# Access visualization settings
print(config.visualization_config.figsize)  # (12, 9)
print(config.visualization_config.elevation)  # 20

# Access output paths
print(config.output_paths.plots_dir)  # "outputs/plots"
print(config.output_paths.animations_dir)  # "outputs/animations"

# Access mathematical constants
print(config.constants['golden_ratio'])  # 1.414213562
```

### Custom Configuration
```python
# Custom config file
config = IVMConfig("custom_config.json")

# Modify settings
config.visualization_config.figsize = (16, 12)
config.output_paths.plots_dir = "custom_plots"

# Generate paths
plot_path = config.generate_plot_path('tetrahedron', '1')
anim_path = config.generate_animation_path('tetrahedron', '1')
```

### Path Generation
```python
config = IVMConfig()

# Standard paths
plot_path = config.generate_plot_path('tetrahedron', '1')
# "outputs/plots/tetrahedron_f1.png"

plot_vector_path = config.generate_plot_path('tetrahedron', '1', show_vectors=True)
# "outputs/plots/tetrahedron_f1_vectors.png"

anim_path = config.generate_animation_path('tetrahedron', '1')
# "outputs/animations/tetrahedron_f1_animation.gif"

comparison_path = config.generate_comparison_path([('tetrahedron', '1'), ('cube', '1')])
# "outputs/plots/comparison_tetrahedron_f1_cube_f1.png"
```

### Data Access
```python
config = IVMConfig()

# Access polyhedron data
tetra_data = config.get_polyhedron_data('tetrahedron', '1')
coordinates = config.get_coordinates('tetrahedron', '1')
sphere_count = config.get_sphere_count('tetrahedron', '1')
orientation = config.get_orientation('tetrahedron', '1')

# Add custom data
custom_data = {
    'frequency': 5,
    'sphere_count': 56,
    'coordinates': [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],
    'polyhedron_type': 'tetrahedron',
    'orientation': 'custom'
}
config.add_polyhedron_data('tetrahedron', '5', custom_data)
```

## Configuration Management

### Default Configuration

The system uses sensible defaults:

```python
config = IVMConfig()
print(config.visualization_config.figsize)  # (12, 9)
print(config.output_paths.plots_dir)        # "outputs/plots"
```

### Custom Configuration Files

```python
# Use custom config file
config = IVMConfig("my_config.json")

# Modify and save
config.visualization_config.figsize = (16, 12)
config.save_coordinates()  # Saves to my_config.json
```

### Directory Management

```python
config = IVMConfig()

# Ensure output directories exist
config._ensure_output_dirs()

# Clean up temporary files
config.cleanup_temp_files(older_than_hours=24)
```

## Integration

### With IVMCoordinates
```python
from ivm_package.config import IVMConfig
from ivm_package.coordinates import IVMCoordinates

config = IVMConfig()
coords = IVMCoordinates(config)

# Configuration affects coordinate loading
data = coords.get_polyhedron('tetrahedron', '1')
```

### With IVMVisualizer
```python
from ivm_package.config import IVMConfig
from ivm_package.visualizer import IVMVisualizer

config = IVMConfig()
viz = IVMVisualizer(config)

# Configuration affects all visualizations
viz.plot_polyhedron('tetrahedron', '1')  # Uses config settings
```

## Performance Considerations

- **Lazy loading**: Configuration loaded on-demand
- **Directory creation**: Automatic creation of output directories
- **File management**: Efficient path generation and file handling
- **Memory efficient**: Configuration data cached appropriately

## Error Handling

### Common Exceptions

#### `ValueError`
- Raised when polyhedron type not found
- Raised when frequency not found for polyhedron type
- Raised when invalid parameters provided

#### `FileNotFoundError`
- Raised when config file not found
- Raised when output directories cannot be created

#### `OSError`
- Raised when file operations fail
- Raised when directory creation fails

### Error Handling Patterns
```python
try:
    config = IVMConfig("custom_config.json")
except FileNotFoundError:
    print("Config file not found, using defaults")
    config = IVMConfig()
```

## Configuration Extensions

### Custom Configuration Classes

```python
from dataclasses import dataclass
from ivm_package.config import IVMConfig

@dataclass
class CustomVisualizationConfig:
    # Extend with custom settings
    custom_setting: str = "default"
    advanced_feature: bool = False

class CustomIVMConfig(IVMConfig):
    def __init__(self, config_file=None):
        super().__init__(config_file)
        self.custom_config = CustomVisualizationConfig()
```

### Configuration Validation

```python
def validate_config(config):
    """Validate configuration settings"""
    if config.visualization_config.figsize[0] < 4:
        raise ValueError("Figure width too small")

    if config.output_paths.plots_dir == "":
        raise ValueError("Plots directory cannot be empty")

    return True
```

---

*This API documentation provides complete reference for the IVMConfig class, the configuration management component of the IVM Polyhedron Visualization System.*

