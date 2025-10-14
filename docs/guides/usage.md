# Usage Guide - IVM Polyhedron Visualization System

Complete usage guide with examples and best practices for the IVM Polyhedron Visualization System.

## 🚀 Basic Usage

### Quick Start

#### 1. Initialize the System
```python
import sys
sys.path.insert(0, 'src')
from ivm_system import IVMSystem

ivm = IVMSystem()
```

#### 2. Explore Available Data
```python
ivm.list_available_data()
```

#### 3. Create Visualizations
```python
# Plot a tetrahedron
ivm.plot_polyhedron('tetrahedron', '1')

# Create an animation
ivm.animate_transformation('tetrahedron', '2', frames=60)

# Compare polyhedrons
ivm.compare_polyhedrons([('tetrahedron', '1'), ('cube', '1')])
```

#### 4. Generate Complete Package
```python
ivm.create_comprehensive_output_package()
```

### Command Line Interface

#### Basic Commands
```bash
# List available polyhedrons
python src/ivm_system.py list

# Plot specific polyhedron
python src/ivm_system.py plot tetrahedron 1

# Create animation
python src/ivm_system.py animate tetrahedron 2 --frames 60

# Compare polyhedrons
python src/ivm_system.py compare tetrahedron 1 cube 1 octahedron 1

# Generate documentation
python src/ivm_system.py docs

# Create complete package
python src/ivm_system.py comprehensive

# Run tests
python src/ivm_system.py test
```

#### Command Options
```bash
# Custom output path
python src/ivm_system.py plot tetrahedron 1 --output custom_plot.png

# Animation with custom frames
python src/ivm_system.py animate tetrahedron 2 --frames 120

# Vector display
python src/ivm_system.py plot tetrahedron 1 --vectors
```

## 🎨 Visualization Examples

### Basic Polyhedron Plots

#### Tetrahedron
```python
ivm = IVMSystem()

# Frequency 1 tetrahedron
ivm.plot_polyhedron('tetrahedron', '1')

# Frequency 2 tetrahedron with vectors
ivm.plot_polyhedron('tetrahedron', '2', show_vectors=True)

# All tetrahedron frequencies
for freq in [1, 2, 3, 4]:
    ivm.plot_polyhedron('tetrahedron', str(freq))
```

#### Other Polyhedrons
```python
polyhedrons = ['octahedron', 'cube', 'cuboctahedron', 'truncated_tetrahedron', 'tetrakaidecahedron']

for poly in polyhedrons:
    ivm.plot_polyhedron(poly, '1')
```

### Animation Examples

#### Sphere-to-Vector Transformation
```python
# Basic transformation animation
ivm.animate_transformation('tetrahedron', '1', frames=30)

# High-quality animation
ivm.animate_transformation('tetrahedron', '2', frames=60, save_path='outputs/animations/tetra_f2.gif')

# Custom frame interval
ivm.animate_transformation('tetrahedron', '3', frames=45, interval=150)
```

#### Multiple Polyhedron Animations
```python
polyhedrons = ['tetrahedron', 'octahedron', 'cube']
frequencies = ['1', '2', '1']

for poly, freq in zip(polyhedrons, frequencies):
    ivm.animate_transformation(poly, freq, frames=30)
```

### Comparison Studies

#### Frequency Comparison
```python
# Compare tetrahedron frequencies
tetra_comparisons = [('tetrahedron', '1'), ('tetrahedron', '2'), ('tetrahedron', '3')]
ivm.compare_polyhedrons(tetra_comparisons)
```

#### Polyhedron Type Comparison
```python
# Compare different polyhedron types
type_comparisons = [('tetrahedron', '1'), ('octahedron', '1'), ('cube', '1')]
ivm.compare_polyhedrons(type_comparisons, save_path='outputs/plots/polyhedron_types.png')
```

#### Comprehensive Comparison
```python
# All polyhedrons at frequency 1
all_comparisons = [
    ('tetrahedron', '1'), ('octahedron', '1'), ('cube', '1'),
    ('cuboctahedron', '1'), ('truncated_tetrahedron', '1'), ('tetrakaidecahedron', '1')
]
ivm.compare_polyhedrons(all_comparisons)
```

## 🔧 Advanced Usage

### Custom Configuration

#### Basic Configuration
```python
from ivm_package.config import IVMConfig

# Default configuration
config = IVMConfig()

# Custom visualization settings
config.visualization_config.figsize = (16, 12)
config.visualization_config.elevation = 30
config.visualization_config.azimuth = 60

# Custom output paths
config.output_paths.plots_dir = "my_plots"
config.output_paths.animations_dir = "my_animations"

# Use with system
ivm = IVMSystem()  # Will use custom config
```

#### Custom Config File
```python
# Create custom config file
custom_config = {
    "visualization_config": {
        "figsize": [16, 12],
        "elevation": 30,
        "azimuth": 60,
        "sphere_radius": 0.03,
        "vector_length": 0.15
    },
    "output_paths": {
        "plots_dir": "custom_plots",
        "animations_dir": "custom_animations"
    }
}

import json
with open('custom_config.json', 'w') as f:
    json.dump(custom_config, f, indent=2)

# Use custom config
config = IVMConfig('custom_config.json')
ivm = IVMSystem()  # Will use custom settings
```

### Direct Component Access

#### Coordinate Data Access
```python
from ivm_package.coordinates import IVMCoordinates

coords = IVMCoordinates()

# Get specific polyhedron data
tetra_data = coords.get_polyhedron('tetrahedron', 1)
print(f"Sphere count: {tetra_data.sphere_count}")
print(f"Coordinates: {tetra_data.coordinates}")

# List all available data
print("Available polyhedrons:", coords.list_polyhedrons())
for poly in coords.list_polyhedrons():
    freqs = coords.list_frequencies(poly)
    print(f"{poly}: {freqs}")
```

#### Visualization Control
```python
from ivm_package.visualizer import IVMVisualizer

viz = IVMVisualizer()

# Custom plotting options
viz.plot_polyhedron(
    'tetrahedron', '1',
    sphere_radius=0.03,
    sphere_color='red',
    show_vectors=True,
    save_path='outputs/plots/custom_tetrahedron.png'
)

# Custom animation settings
viz.animate_sphere_to_vector(
    'tetrahedron', '2',
    frames=60,
    interval=100,
    save_path='outputs/animations/custom_animation.gif'
)
```

### Batch Processing

#### Process All Polyhedrons
```python
ivm = IVMSystem()

# Plot all polyhedrons at all frequencies
ivm.create_all_polyhedron_visualizations()

# Create all animations
ivm.create_comprehensive_animations()

# Generate documentation
ivm.create_documentation()
```

#### Custom Batch Processing
```python
# Process specific combinations
polyhedrons = ['tetrahedron', 'cube', 'octahedron']
frequencies = ['1', '2', '1']

for poly, freq in zip(polyhedrons, frequencies):
    ivm.plot_polyhedron(poly, freq)
    ivm.animate_transformation(poly, freq, frames=30)
```

## 📊 Data Analysis

### Mathematical Validation

#### Verify Coordinate Properties
```python
import numpy as np
from ivm_package.coordinates import IVMCoordinates

coords = IVMCoordinates()
tetra_data = coords.get_polyhedron('tetrahedron', 1)
coordinates = np.array(tetra_data.coordinates)

# Check unit vector magnitudes
magnitudes = np.linalg.norm(coordinates, axis=1)
print("All magnitudes close to 1:", np.allclose(magnitudes, 1.0))

# Check center of mass
center = np.mean(coordinates, axis=0)
print("Center of mass:", center)
print("Close to origin:", np.allclose(center, [0, 0, 0]))

# Check tetrahedral angles
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        dot_product = np.dot(coordinates[i], coordinates[j])
        angle = np.degrees(np.arccos(dot_product))
        print(f"Angle between vectors {i} and {j}: {angle:.2f}°")
```

#### Frequency Analysis
```python
# Analyze sphere count progression
sphere_counts = {}
for poly in coords.list_polyhedrons():
    sphere_counts[poly] = {}
    for freq in coords.list_frequencies(poly):
        data = coords.get_polyhedron(poly, freq)
        sphere_counts[poly][freq] = data.sphere_count

print("Sphere count progression:")
for poly, freqs in sphere_counts.items():
    print(f"{poly}: {freqs}")
```

### Performance Analysis

#### Benchmarking
```python
import time
from ivm_system import IVMSystem

ivm = IVMSystem()

# Time basic operations
start = time.time()
ivm.plot_polyhedron('tetrahedron', '1')
plot_time = time.time() - start

start = time.time()
ivm.animate_transformation('tetrahedron', '2', frames=30)
anim_time = time.time() - start

print(f"Plot time: {plot_time:.3f}s")
print(f"Animation time: {anim_time:.3f}s")
```

#### Memory Usage
```python
import tracemalloc
from ivm_system import IVMSystem

ivm = IVMSystem()
tracemalloc.start()

# Memory-intensive operation
ivm.create_comprehensive_animations()

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024**2:.2f} MB")
print(f"Peak memory: {peak / 1024**2:.2f} MB")

tracemalloc.stop()
```

## 🎯 Educational Examples

### Learning Progression

#### 1. Basic Geometry
```python
# Start with simple tetrahedron
ivm = IVMSystem()
ivm.plot_polyhedron('tetrahedron', '1')

# Examine coordinate structure
coords = ivm.coordinates.get_polyhedron('tetrahedron', 1)
print("Tetrahedron coordinates:")
for i, coord in enumerate(coords.coordinates):
    print(f"Vertex {i+1}: {coord}")
```

#### 2. Frequency Relationships
```python
# Explore frequency progression
for freq in [1, 2, 3, 4]:
    data = ivm.coordinates.get_polyhedron('tetrahedron', freq)
    print(f"Frequency {freq}: {data.sphere_count} spheres")

# Visualize the progression
freq_comparisons = [('tetrahedron', '1'), ('tetrahedron', '2'), ('tetrahedron', '3'), ('tetrahedron', '4')]
ivm.compare_polyhedrons(freq_comparisons)
```

#### 3. Transformation Processes
```python
# Understand sphere-to-vector transformation
ivm.animate_transformation('tetrahedron', '1', frames=60)

# Compare different polyhedron transformations
for poly in ['tetrahedron', 'octahedron', 'cube']:
    ivm.animate_transformation(poly, '1', frames=30)
```

#### 4. Omni-Concentric Hierarchy
```python
# Visualize nested structures
ivm.plot_polyhedron('tetrahedron', '4')  # Contains all lower frequencies

# Create comprehensive hierarchy visualization
ivm.create_comprehensive_visualizations()
```

### Research Applications

#### Nuclear Physics Correlations
```python
# Analyze frequency relationships to particle physics
coords = IVMCoordinates()

# Vector equilibrium at frequency 17
ve_data = coords.get_polyhedron('cuboctahedron', 1)  # Approximates VE structure

# Calculate mass ratios
total_vectors = sum(len(coords.get_polyhedron('tetrahedron', f).coordinates)
                   for f in range(1, 18))  # Up to F17
print(f"Total vectors up to F17: {total_vectors}")
```

#### Crystallography Studies
```python
# Analyze space-filling properties
tetrakai_data = coords.get_polyhedron('tetrakaidecahedron', 1)
print(f"Tetrakaidecahedron vertices: {tetrakai_data.sphere_count}")

# Study packing efficiency
cube_data = coords.get_polyhedron('cube', 1)
print(f"Cube vertices: {cube_data.sphere_count}")
```

## 🔧 Best Practices

### Performance Optimization

#### For Large Datasets
```python
# Use appropriate frame counts for animations
ivm.animate_transformation('tetrahedron', '4', frames=30)  # Not 60

# Process in batches
polyhedrons = ['tetrahedron', 'cube', 'octahedron']
for poly in polyhedrons:
    ivm.plot_polyhedron(poly, '1')
```

#### Memory Management
```python
# System manages memory automatically
# For very large animations, process individually
for freq in [1, 2, 3]:
    ivm.animate_transformation('tetrahedron', str(freq), frames=30)
```

### File Organization

#### Output Structure
```
outputs/
├── plots/           # Static PNG visualizations
├── animations/      # GIF animation files
└── docs/           # Generated documentation
```

#### Custom Organization
```python
# Use custom output directories
config = IVMConfig()
config.output_paths.plots_dir = "research_plots"
config.output_paths.animations_dir = "research_animations"

ivm = IVMSystem()  # Uses custom paths
```

### Error Handling

#### Graceful Degradation
```python
try:
    ivm.plot_polyhedron('tetrahedron', '1')
except ValueError as e:
    print(f"Plotting failed: {e}")
    # Continue with other operations
    ivm.plot_polyhedron('cube', '1')
```

#### Configuration Fallbacks
```python
try:
    config = IVMConfig("custom_config.json")
except FileNotFoundError:
    print("Custom config not found, using defaults")
    config = IVMConfig()
```

## 📚 Documentation Generation

### Auto-Generated Documentation
```python
# Generate coordinate documentation
ivm.create_documentation()

# Generate API reference
# (Included in comprehensive package)

# Generate mathematical foundation docs
# (Included in comprehensive package)
```

### Custom Documentation
```python
# Generate docs for specific polyhedrons
from ivm_package.visualizer import IVMVisualizer

viz = IVMVisualizer()
viz.create_coordinate_documentation('custom_docs')
```

## 🎨 Visualization Tips

### Optimal Viewing Settings

#### Camera Angles
```python
# Good viewing angles for different polyhedrons
angles = {
    'tetrahedron': {'elevation': 20, 'azimuth': 45},
    'octahedron': {'elevation': 30, 'azimuth': 30},
    'cube': {'elevation': 25, 'azimuth': 45}
}
```

#### Color Schemes
```python
# Distinct colors for different frequencies
colors = ['blue', 'green', 'orange', 'red', 'purple']
```

### Animation Quality

#### Frame Rate Optimization
```python
# Balance quality vs file size
quality_settings = {
    'high': {'frames': 60, 'interval': 100},
    'medium': {'frames': 30, 'interval': 150},
    'low': {'frames': 20, 'interval': 200}
}
```

## 🚨 Common Issues and Solutions

### Import Errors
```python
# Ensure proper path setup
import sys
sys.path.insert(0, 'src')
```

### Matplotlib Issues
```python
# For headless environments
import matplotlib
matplotlib.use('Agg')
```

### Memory Issues
```python
# Process large polyhedrons individually
for freq in [1, 2, 3]:
    ivm.animate_transformation('tetrahedron', str(freq), frames=30)
```

### File Permission Errors
```bash
# Ensure write permissions
chmod 755 outputs/
mkdir -p outputs/plots outputs/animations outputs/docs
```

## 📈 Advanced Workflows

### Research Workflow
```python
# 1. Set up research environment
config = IVMConfig("research_config.json")
ivm = IVMSystem()

# 2. Generate baseline visualizations
ivm.create_comprehensive_visualizations()

# 3. Analyze coordinate properties
coords = ivm.coordinates
# ... mathematical analysis ...

# 4. Create custom visualizations
# ... custom research plots ...

# 5. Generate research report
ivm.create_documentation('research_docs')
```

### Educational Workflow
```python
# 1. Start with basics
ivm = IVMSystem()
ivm.plot_polyhedron('tetrahedron', '1')

# 2. Progress through frequencies
for freq in [1, 2, 3, 4]:
    ivm.plot_polyhedron('tetrahedron', str(freq))

# 3. Explore transformations
ivm.animate_transformation('tetrahedron', '1', frames=30)

# 4. Compare structures
ivm.compare_polyhedrons([('tetrahedron', '1'), ('cube', '1')])

# 5. Generate educational materials
ivm.create_documentation('educational_docs')
```

### Development Workflow
```python
# 1. Run tests
ivm.run_tests()

# 2. Create development visualizations
ivm.create_comprehensive_visualizations()

# 3. Test new features
# ... test custom implementations ...

# 4. Generate development docs
ivm.create_documentation('dev_docs')
```

---

*This usage guide provides comprehensive examples and best practices for working with the IVM Polyhedron Visualization System, from basic usage to advanced research applications.*
