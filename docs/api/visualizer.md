# IVMVisualizer API Documentation

Complete API documentation for the IVMVisualizer class.

## Overview

The `IVMVisualizer` class handles 3D visualization and animation of polyhedrons in the IVM system, providing comprehensive plotting and animation capabilities.

## Constructor

```python
IVMVisualizer(config=None)
```

**Parameters:**
- `config` (IVMConfig, optional): Configuration instance. Uses default if not provided.

## Plotting Methods

### `plot_polyhedron(polyhedron_type: str, frequency: str, show_vectors: bool = False, save_path: Optional[str] = None)`

Create static 3D plot of a polyhedron.

```python
viz.plot_polyhedron('tetrahedron', '1')
viz.plot_polyhedron('tetrahedron', '2', show_vectors=True)
```

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (str): Frequency as string
- `show_vectors` (bool): Whether to show vector connections
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

### `animate_sphere_to_vector(polyhedron_type: str, frequency: str, frames: Optional[int] = None, save_path: Optional[str] = None)`

Create sphere-to-vector transformation animation.

```python
viz.animate_sphere_to_vector('tetrahedron', '1', frames=60)
```

**Parameters:**
- `polyhedron_type` (str): Polyhedron type
- `frequency` (str): Frequency as string
- `frames` (int, optional): Number of animation frames. Uses config default if not provided.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

### `compare_polyhedrons(polyhedrons: List[Tuple[str, str]], save_path: Optional[str] = None)`

Create side-by-side comparison of multiple polyhedrons.

```python
comparisons = [('tetrahedron', '1'), ('octahedron', '1'), ('cube', '1')]
viz.compare_polyhedrons(comparisons)
```

## Documentation Methods

### `create_coordinate_documentation(output_dir: Optional[str] = None)`

Generate comprehensive coordinate documentation.

```python
viz.create_coordinate_documentation('custom_docs')
```

### `create_comprehensive_visualizations()`

Create all conceptual visualizations from xyz_clean.md.

### `create_comprehensive_animations()`

Create all animation sequences.

### `create_additional_visualizations()`

Create advanced visualization types (vector fields, energy flows, etc.).

### `create_html_visualizations()`

Generate interactive HTML interface.

### `create_comprehensive_output_package()`

Generate complete output package with all visualizations.

## Visualization Features

### 3D Plotting
- **Interactive 3D plots** with matplotlib
- **Vector display** showing connections to origin
- **Auto-scaling** for optimal viewing
- **Save/export** capabilities

### Animation System
- **Sphere-to-vector transformation** animations
- **Configurable frame rates** and timing
- **Multiple animation types** (transformation, growth, rotation)
- **High-quality GIF output**

### Advanced Visualizations
- **Vector field visualizations** showing IVM structure
- **Particle interaction simulations**
- **Energy flow diagrams**
- **Transformation sequence diagrams**
- **3D surface plots** and cross-sections

## Configuration Integration

The visualizer uses configuration settings for:
- **Figure sizing** and layout
- **Camera angles** (elevation, azimuth)
- **Output paths** and file naming
- **Animation parameters** (frames, intervals)

## Usage Examples

### Basic Plotting
```python
from ivm_package.visualizer import IVMVisualizer

viz = IVMVisualizer()

# Simple tetrahedron plot
viz.plot_polyhedron('tetrahedron', '1')

# Plot with vectors
viz.plot_polyhedron('tetrahedron', '2', show_vectors=True)

# Custom save location
viz.plot_polyhedron('cube', '1', save_path='custom_cube.png')
```

### Animation Creation
```python
# Sphere-to-vector transformation
viz.animate_sphere_to_vector('tetrahedron', '1', frames=60)

# Custom animation parameters
viz.animate_sphere_to_vector('tetrahedron', '2', frames=120, save_path='custom_anim.gif')
```

### Advanced Visualizations
```python
# Create all comprehensive visualizations
viz.create_comprehensive_visualizations()

# Create additional advanced visualizations
viz.create_additional_visualizations()

# Generate complete output package
viz.create_comprehensive_output_package()
```

### Documentation Generation
```python
# Generate coordinate documentation
viz.create_coordinate_documentation()

# Generate HTML interface
viz.create_html_visualizations()

# Generate complete documentation package
viz.create_coordinate_documentation('custom_docs')
```

## Integration

### With IVMCoordinates
```python
from ivm_package.coordinates import IVMCoordinates
from ivm_package.visualizer import IVMVisualizer

coords = IVMCoordinates()
viz = IVMVisualizer()

# Get coordinate data and visualize
data = coords.get_polyhedron('tetrahedron', '1')
viz.plot_polyhedron('tetrahedron', '1')
```

### With IVMConfig
```python
from ivm_package.config import IVMConfig
from ivm_package.visualizer import IVMVisualizer

config = IVMConfig()
viz = IVMVisualizer(config)

# Configuration affects all visualizations
viz.plot_polyhedron('tetrahedron', '1')  # Uses config settings
```

## Performance Considerations

### Animation Performance
- **Frame generation**: Optimized for 60+ frames
- **File I/O**: Efficient GIF creation
- **Memory management**: Progressive frame loading

### Large Polyhedron Handling
- **Frequency 4 tetrahedron**: 35 spheres handled efficiently
- **Memory optimization**: Coordinate reuse
- **Processing time**: < 5 seconds for complex animations

## Error Handling

### Common Exceptions

#### `ValueError`
- Raised when polyhedron type not found
- Raised when frequency not found for polyhedron type
- Raised when invalid parameters provided

#### `FileNotFoundError`
- Raised when output directories cannot be created
- Raised when config files are missing

### Error Handling Patterns
```python
try:
    viz.plot_polyhedron('tetrahedron', '1')
except ValueError as e:
    print(f"Plotting failed: {e}")
    # Handle gracefully
```

## Output Management

### Automatic File Saving
- All plots saved as PNG files
- All animations saved as GIF files
- Documentation generated as Markdown and HTML
- Standardized file naming conventions

### Directory Structure
```
outputs/
├── plots/          # PNG visualization files
├── animations/     # GIF animation files
└── docs/          # Documentation and HTML
```

---

*This API documentation provides complete reference for the IVMVisualizer class, the visualization engine of the IVM Polyhedron Visualization System.*

