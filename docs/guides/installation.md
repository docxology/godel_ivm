# Installation Guide - IVM Polyhedron Visualization System

Complete installation and setup guide for the IVM Polyhedron Visualization System.

## Prerequisites

### Required Software
- **Python 3.7+** (Python 3.8+ recommended)
- **pip** package manager
- **Git** (for cloning repository)

### Required Python Packages
```bash
pip install numpy matplotlib
```

## Installation Methods

### Method 1: Git Clone (Recommended)

```bash
# Clone the repository
git clone https://github.com/docxology/godel_ivm.git
cd godel_ivm

# Install dependencies
pip install numpy matplotlib

# Verify installation
python src/ivm_system.py --help
```

### Method 2: Direct Download

1. Download the repository as ZIP
2. Extract to desired location
3. Navigate to the directory
4. Install dependencies: `pip install numpy matplotlib`

## Directory Structure

After installation, your directory should look like:

```
godel_ivm/
├── src/                          # Source code
│   ├── ivm_system.py            # Main command-line interface
│   └── ivm_package/             # Core package
├── tests/                        # Test suite
├── configs/                      # Configuration data
├── outputs/                      # Generated content (created on first run)
├── docs/                         # Documentation
└── README.md                     # Project overview
```

## Verification

### Test Installation

```bash
# Test the system
python src/ivm_system.py list

# Should display available polyhedrons
# Tetrahedron: frequencies 0, 1, 2, 3, 4
# Octahedron: frequency 1
# Cube: frequencies 1, 2
# etc.
```

### Test Dependencies

```python
import numpy as np
import matplotlib.pyplot as plt

# Test basic functionality
print("NumPy version:", np.__version__)
print("Matplotlib version:", plt.matplotlib.__version__)

# Test our modules
import sys
sys.path.insert(0, 'src')
from ivm_system import IVMSystem

ivm = IVMSystem()
print("IVM System initialized successfully")
```

## Configuration

### Default Configuration

The system uses sensible defaults:
- **Output directory**: `outputs/`
- **Figure size**: 12×9 inches
- **DPI**: 300
- **Animation frames**: 30

### Custom Configuration

```python
from ivm_package.config import IVMConfig

# Create custom config
config = IVMConfig("my_config.json")

# Modify settings
config.visualization_config.figsize = (16, 12)
config.output_paths.plots_dir = "my_plots"

# Use with system
from ivm_system import IVMSystem
ivm = IVMSystem()  # Will use custom config
```

## First Run

### Generate All Content

```bash
# Create all visualizations and documentation
python src/ivm_system.py comprehensive

# This creates:
# - 36 PNG visualizations
# - 8 GIF animations
# - Interactive HTML interface
# - Complete documentation
```

### Verify Output

```bash
# Check generated files
ls -la outputs/

# Should see:
# plots/     - PNG visualization files
# animations/ - GIF animation files
# docs/       - HTML interface and documentation
```

### Open Interactive Interface

```bash
# Open the main interface
open outputs/docs/index.html

# Or specific animations
open outputs/animations/sphere_vector_transformation.gif
```

## Troubleshooting

### Common Issues

#### "Module not found" errors
```bash
# Ensure proper path setup
export PYTHONPATH="$PWD/src:$PYTHONPATH"

# Or run from project root
cd /path/to/godel_ivm
python src/ivm_system.py list
```

#### Import errors
```bash
# Check Python path
python -c "import sys; print(sys.path)"

# Ensure src/ is in path
export PYTHONPATH="$PWD/src:$PYTHONPATH"
```

#### Permission errors
```bash
# Ensure write permissions
chmod 755 outputs/
mkdir -p outputs/plots outputs/animations outputs/docs
```

#### Matplotlib backend issues
```python
# Set backend explicitly
import matplotlib
matplotlib.use('Agg')  # For headless environments

# Or install display server
# sudo apt-get install python3-tk  # Linux
```

### Debug Mode

```python
import logging

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Run with detailed output
python src/ivm_system.py comprehensive
```

## System Requirements

### Minimum Requirements
- **Python**: 3.7+
- **RAM**: 2GB
- **Storage**: 500MB free space
- **OS**: Linux, macOS, Windows

### Recommended Requirements
- **Python**: 3.8+
- **RAM**: 4GB
- **Storage**: 1GB free space
- **OS**: Linux or macOS (best matplotlib support)

## Performance Optimization

### For Large Polyhedrons
```bash
# Use appropriate frame counts
python src/ivm_system.py animate tetrahedron 4 --frames 30
```

### For Batch Processing
```bash
# Process multiple items efficiently
python src/ivm_system.py comprehensive
```

### Memory Management
```python
# System automatically manages memory
# Large animations may require more RAM
```

## Development Setup

### For Contributors

```bash
# Clone repository
git clone https://github.com/docxology/godel_ivm.git
cd godel_ivm

# No packaging metadata is committed; run from the repo root
# (or add src/ to PYTHONPATH) instead of pip install -e .

# Run tests
python -m pytest tests/

# Or use the built-in test runner
python src/ivm_system.py test
```

### IDE Setup

#### Visual Studio Code
```json
{
    "python.defaultInterpreterPath": "python3",
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"]
}
```

#### PyCharm
- Set Python interpreter to use `src/` directory
- Enable pytest for test discovery
- Configure matplotlib backend if needed

## Environment Variables

### Optional Configuration

```bash
# Custom output directory
export IVM_OUTPUT_DIR="/custom/path"

# Custom config file
export IVM_CONFIG_FILE="my_config.json"

# Debug mode
export IVM_DEBUG=1
```

## Verification Checklist

- [ ] Python 3.7+ installed
- [ ] numpy and matplotlib installed
- [ ] Repository cloned/downloaded
- [ ] Can run `python src/ivm_system.py list`
- [ ] Output directories created automatically
- [ ] Can generate basic visualizations
- [ ] Can view HTML interface

## Getting Help

### Documentation
- **[📖 Complete Documentation](../../outputs/docs/output_summary.md)**
- **[🔧 API Reference](../api/)**
- **[🧪 Test Coverage](../generated/test_coverage.md)**

### Support
- Check the troubleshooting section above
- Review the installation logs
- Verify all dependencies are installed correctly

---

*This installation guide provides complete setup instructions for the IVM Polyhedron Visualization System.*

