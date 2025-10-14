# IVMCoordinates API Documentation

Complete API documentation for the IVMCoordinates class.

## Overview

The `IVMCoordinates` class manages all polyhedron coordinate data for the IVM system, providing access to coordinate specifications from Noel Coughlin's paper "Mapping the Vanishing and Reappearing Quanta Points of the IVM's 6 Axis Metric Upon the Cartesian Coordinate System's 3 x,y,z axis".

## Constructor

```python
IVMCoordinates(config=None)
```

**Parameters:**
- `config` (IVMConfig, optional): Configuration instance. Uses default if not provided.

## Core Methods

### `get_polyhedron(polyhedron_type: str, frequency: str) -> PolyhedronData`

Get coordinate data for a specific polyhedron and frequency.

```python
tetra_data = coords.get_polyhedron('tetrahedron', '1')
```

**Parameters:**
- `polyhedron_type` (str): Type of polyhedron ('tetrahedron', 'octahedron', etc.)
- `frequency` (str): Frequency as string ('0', '1', '2', etc.)

**Returns:**
- `PolyhedronData`: Complete polyhedron data structure

**Raises:**
- `ValueError`: If polyhedron type or frequency not found

### `list_polyhedrons() -> List[str]`

Get list of all available polyhedron types.

```python
types = coords.list_polyhedrons()
# Returns: ['tetrahedron', 'octahedron', 'cube', 'cuboctahedron', ...]
```

### `list_frequencies(polyhedron_type: str) -> List[str]`

Get list of all available frequencies for a polyhedron type.

```python
freqs = coords.list_frequencies('tetrahedron')
# Returns: ['0', '1', '2', '3', '4']
```

### `save_to_json(filename: str)`

Save coordinate data to JSON file.

```python
coords.save_to_json('custom_coordinates.json')
```

## Data Structure

### PolyhedronData Class

```python
@dataclass
class PolyhedronData:
    frequency: int                    # Frequency number
    sphere_count: int                 # Number of spheres
    coordinates: List[Tuple[float, float, float]]  # Coordinate list
    polyhedron_type: str             # Polyhedron type name
    orientation: str                 # Orientation type ('first' or 'correct')
```

## Supported Polyhedron Types

### Tetrahedron
- **Frequencies**: 0, 1, 2, 3, 4
- **Orientations**: 'first' (Section B), 'correct' (Section C)
- **Sphere Counts**: 1, 4, 10, 20, 35

### Octahedron
- **Frequencies**: 1
- **Orientations**: 'first'
- **Sphere Counts**: 6

### Cube
- **Frequencies**: 1, 2
- **Orientations**: 'first'
- **Sphere Counts**: 14, 63

### Cuboctahedron (Vector Equilibrium)
- **Frequencies**: 1
- **Orientations**: 'first'
- **Sphere Counts**: 13

### Truncated Tetrahedron
- **Frequencies**: 1
- **Orientations**: 'first'
- **Sphere Counts**: 12

### Tetrakaidecahedron
- **Frequencies**: 1
- **Orientations**: 'first'
- **Sphere Counts**: 38

## Coordinate Systems

### Section B (First Orientation)
Coordinates aligned with x,y,z axes for easy calculation and visualization of edge length increments.

### Section C (Correct Orientation)
45-degree rotated coordinates representing the true IVM orientation within the 3-axis Cartesian system.

## Mathematical Properties

All coordinates maintain:
- **Unit vector magnitudes**: `|v| = 1` for all vectors
- **Center of mass at origin**: `Σv_i = 0`
- **Tetrahedral angular relationships**: 109.47° between vectors
- **Frequency-based scaling consistency**

## Usage Examples

### Basic Access
```python
from ivm_package.coordinates import IVMCoordinates

coords = IVMCoordinates()

# Get tetrahedron data
tetra_data = coords.get_polyhedron('tetrahedron', '1')
print(f"Sphere count: {tetra_data.sphere_count}")
print(f"Coordinates: {tetra_data.coordinates}")

# List all polyhedron types
types = coords.list_polyhedrons()
print(f"Available types: {types}")

# List frequencies for tetrahedron
freqs = coords.list_frequencies('tetrahedron')
print(f"Tetrahedron frequencies: {freqs}")
```

### Data Validation
```python
# Verify coordinate properties
coords = IVMCoordinates()
tetra_data = coords.get_polyhedron('tetrahedron', '1')

# Check unit vectors
magnitudes = [np.linalg.norm(coord) for coord in tetra_data.coordinates]
assert all(abs(mag - 1.0) < 1e-10 for mag in magnitudes)

# Check center of mass
center = np.mean(tetra_data.coordinates, axis=0)
assert np.allclose(center, [0, 0, 0], atol=1e-10)
```

### Custom Configuration
```python
from ivm_package.config import IVMConfig

# Custom config
config = IVMConfig()
coords = IVMCoordinates(config)

# Access coordinate data
data = coords.get_polyhedron('tetrahedron', '2')
```

## Error Handling

### Common Exceptions

#### `ValueError`
- Raised when polyhedron type not found
- Raised when frequency not found for polyhedron type
- Raised when invalid parameters provided

### Error Handling Patterns
```python
try:
    data = coords.get_polyhedron('tetrahedron', '1')
except ValueError as e:
    print(f"Polyhedron not found: {e}")
    # Handle gracefully
```

## Performance Considerations

- **Large coordinate sets**: Frequency 4 tetrahedron has 35 spheres
- **Memory efficient**: Coordinates stored as tuples, not numpy arrays
- **Fast access**: Direct dictionary lookup for polyhedron data
- **Lazy loading**: Coordinates loaded on-demand

## Integration

### With IVMVisualizer
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

config = IVMConfig()
coords = IVMCoordinates(config)

# Configuration affects coordinate loading
# Custom config files can be used
```

---

*This API documentation provides complete reference for the IVMCoordinates class, the core data management component of the IVM Polyhedron Visualization System.*

