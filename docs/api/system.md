# IVMSystem API Documentation

Complete API documentation for the IVMSystem class.

## Overview

The `IVMSystem` class provides the main command-line interface and unified access to all IVM system functionality, serving as the primary entry point for users.

## Constructor

```python
IVMSystem()
```

Creates a new IVM system instance with default configuration.

## Core Methods

### `plot_polyhedron(polyhedron_type: str, frequency: str, show_vectors: bool = False, save_path: Optional[str] = None)`

Plot a polyhedron with optional vector display.

```python
ivm = IVMSystem()
ivm.plot_polyhedron('tetrahedron', '1')
ivm.plot_polyhedron('tetrahedron', '2', show_vectors=True)
```

**Parameters:**
- `polyhedron_type` (str): Type of polyhedron ('tetrahedron', 'octahedron', etc.)
- `frequency` (str): Frequency as string ('0', '1', '2', etc.)
- `show_vectors` (bool): Whether to show vector connections (default: False)
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

### `animate_transformation(polyhedron_type: str, frequency: str, frames: Optional[int] = None, save_path: Optional[str] = None)`

Create sphere-to-vector transformation animation.

```python
ivm = IVMSystem()
ivm.animate_transformation('tetrahedron', '1', frames=60)
```

**Parameters:**
- `polyhedron_type` (str): Type of polyhedron
- `frequency` (str): Frequency as string
- `frames` (int, optional): Number of animation frames. Uses config default if not provided.
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

### `compare_polyhedrons(comparisons: List[Tuple[str, str]], save_path: Optional[str] = None)`

Create side-by-side comparison of multiple polyhedrons.

```python
comparisons = [('tetrahedron', '1'), ('octahedron', '1'), ('cube', '1')]
ivm.compare_polyhedrons(comparisons)
```

**Parameters:**
- `comparisons` (List[Tuple[str, str]]): List of (polyhedron_type, frequency) tuples
- `save_path` (str, optional): Custom save path. Uses config default if not provided.

## Documentation Methods

### `create_documentation(output_dir: Optional[str] = None)`

Generate comprehensive coordinate documentation.

```python
ivm.create_documentation()  # Uses default output directory
ivm.create_documentation('custom_docs')  # Custom directory
```

**Parameters:**
- `output_dir` (str, optional): Custom output directory. Uses config default if not provided.

### `create_comprehensive_visualizations()`

Create all conceptual visualizations from Noel Coughlin's IVM coordinate paper.

```python
ivm.create_comprehensive_visualizations()
```

### `create_comprehensive_animations()`

Create all animation sequences.

```python
ivm.create_comprehensive_animations()
```

### `create_additional_visualizations()`

Create advanced visualization types.

```python
ivm.create_additional_visualizations()
```

### `create_html_visualizations()`

Generate interactive HTML interface.

```python
ivm.create_html_visualizations()
```

### `create_comprehensive_output_package()`

Generate complete output package with all visualizations.

```python
ivm.create_comprehensive_output_package()  # Creates everything
```

## Utility Methods

### `run_tests()`

Execute complete test suite.

```python
results = ivm.run_tests()
if not results.wasSuccessful():
    print("Tests failed!")
```

**Returns:**
- `unittest.TestResult`: Test execution results

### `list_available_data()`

Display available polyhedrons and frequencies.

```python
ivm.list_available_data()
```

## Usage Examples

### Basic Usage
```python
from ivm_system import IVMSystem

ivm = IVMSystem()

# List available data
ivm.list_available_data()

# Plot polyhedron
ivm.plot_polyhedron('tetrahedron', '1')

# Create animation
ivm.animate_transformation('tetrahedron', '2', frames=60)

# Compare polyhedrons
ivm.compare_polyhedrons([('tetrahedron', '1'), ('cube', '1')])
```

### Advanced Usage
```python
# Create complete output package
ivm.create_comprehensive_output_package()

# Generate documentation
ivm.create_documentation()

# Create HTML interface
ivm.create_html_visualizations()

# Run tests
ivm.run_tests()
```

### Custom Configuration
```python
from ivm_package.config import IVMConfig

# Use custom config
config = IVMConfig("custom_config.json")
ivm = IVMSystem()  # Uses default config

# The system uses configuration for paths and settings
ivm.plot_polyhedron('tetrahedron', '1')  # Uses config settings
```

## Integration

### With Individual Components
```python
from ivm_system import IVMSystem
from ivm_package.coordinates import IVMCoordinates
from ivm_package.visualizer import IVMVisualizer

ivm = IVMSystem()

# Access underlying components
coords = ivm.coordinates
viz = ivm.visualizer

# Use directly
data = coords.get_polyhedron('tetrahedron', '1')
viz.plot_polyhedron('tetrahedron', '1')
```

### With Configuration
```python
from ivm_package.config import IVMConfig

# Custom configuration affects entire system
config = IVMConfig("custom_config.json")
ivm = IVMSystem()  # System uses config settings

# All operations use custom settings
ivm.plot_polyhedron('tetrahedron', '1')  # Uses custom paths
```

## Command Line Interface

The IVMSystem class powers the main command-line interface:

```bash
# List available data
python src/ivm_system.py list

# Plot polyhedron
python src/ivm_system.py plot tetrahedron 1

# Create animations
python src/ivm_system.py animate tetrahedron 2

# Compare polyhedrons
python src/ivm_system.py compare tetrahedron 1 cube 1

# Generate documentation
python src/ivm_system.py docs

# Create comprehensive output
python src/ivm_system.py comprehensive

# Run tests
python src/ivm_system.py test
```

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
    ivm.plot_polyhedron('tetrahedron', '1')
except ValueError as e:
    print(f"Plotting failed: {e}")
    # Handle gracefully
```

## Performance Considerations

- **Large polyhedron handling**: Optimized for frequency 4 tetrahedrons (35 spheres)
- **Animation generation**: Efficient for 60+ frame animations
- **Memory management**: Progressive coordinate loading
- **File I/O optimization**: Batch processing for multiple outputs

## Configuration Integration

The system integrates with IVMConfig for:

- **Output path management**: Standardized file naming and locations
- **Visualization settings**: Figure sizes, camera angles, DPI
- **Animation parameters**: Frame counts, intervals
- **Directory management**: Automatic creation and cleanup

## Extension Points

### Custom Commands
```python
# Add custom commands to the system
class CustomIVMSystem(IVMSystem):
    def custom_visualization(self):
        # Custom visualization logic
        pass
```

### Integration with Other Systems
```python
# Use IVMSystem as component in larger system
ivm = IVMSystem()

# Integrate with other visualization tools
data = ivm.coordinates.get_polyhedron('tetrahedron', '1')
# Process with external tools
```

## Testing Integration

### Test Suite Integration
```python
ivm = IVMSystem()
results = ivm.run_tests()  # Runs complete test suite

if results.wasSuccessful():
    print("All tests passed!")
else:
    print(f"Tests failed: {len(results.failures)} failures")
```

### Individual Component Testing
```python
# Test individual components through the system
ivm.coordinates.get_polyhedron('tetrahedron', '1')  # Test coordinates
ivm.visualizer.plot_polyhedron('tetrahedron', '1')  # Test visualization
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

## Performance Optimization

### Batch Processing
```python
# Process multiple visualizations efficiently
ivm.create_comprehensive_output_package()  # Single call for everything
```

### Memory Management
```python
# System manages memory automatically
ivm.animate_transformation('tetrahedron', '4', frames=120)  # Large animation
```

### File I/O Optimization
```python
# Optimized for multiple file operations
ivm.create_all_polyhedron_visualizations()  # 30+ files efficiently
```

## Error Recovery

### Graceful Degradation
```python
try:
    ivm.plot_polyhedron('invalid_type', '1')
except ValueError:
    print("Invalid polyhedron type - using default")
    ivm.plot_polyhedron('tetrahedron', '1')
```

### Configuration Fallbacks
```python
# System works even with missing config
config = IVMConfig("missing_file.json")  # Falls back to defaults
ivm = IVMSystem()  # Works with default config
```

## Educational Value

### Learning Tool
```python
# Explore different polyhedrons
ivm.list_available_data()
ivm.plot_polyhedron('tetrahedron', '1')
ivm.plot_polyhedron('tetrahedron', '2')
ivm.compare_polyhedrons([('tetrahedron', '1'), ('tetrahedron', '2')])
```

### Research Platform
```python
# Mathematical validation
ivm.coordinates.get_polyhedron('tetrahedron', '1')
# Analyze coordinate properties
```

### Visualization Reference
```python
# Complete visual documentation
ivm.create_comprehensive_output_package()
# All concepts visualized
```

---

*This API documentation provides complete reference for the IVMSystem class, the main interface for the IVM Polyhedron Visualization System.*

