# Troubleshooting Guide - IVM Polyhedron Visualization System

Comprehensive troubleshooting guide for common issues and solutions in the IVM Polyhedron Visualization System.

## 🚨 Common Issues

### Import and Module Errors

#### "Module not found" errors
**Symptoms:**
```
ModuleNotFoundError: No module named 'ivm_package'
ImportError: cannot import name 'IVMSystem'
```

**Solutions:**

1. **Path Setup**
   ```bash
   # Ensure src/ is in Python path
   export PYTHONPATH="$PWD/src:$PYTHONPATH"

   # Or run from project root
   cd /path/to/godel_ivm
   python src/ivm_system.py list
   ```

2. **Installation Verification**
   ```python
   import sys
   print("Python path:", sys.path)

   # Check if src is included
   'src' in str(sys.path) or any('src' in p for p in sys.path)
   ```

3. **Dependencies Check**
   ```bash
   # Verify required packages
   python -c "import numpy; import matplotlib; print('Dependencies OK')"
   ```

#### Import Path Issues
**Symptoms:**
```
ImportError: attempted relative import with no known parent package
```

**Solutions:**
```python
# In your scripts, use absolute imports
import sys
sys.path.insert(0, 'src')

from ivm_system import IVMSystem
```

### Visualization Issues

#### Matplotlib Backend Problems
**Symptoms:**
```
_tkinter.TclError: no display name and no $DISPLAY environment variable
```

**Solutions:**

1. **Set Backend Explicitly**
   ```python
   import matplotlib
   matplotlib.use('Agg')  # For headless environments
   ```

2. **Install Display Server (Linux)**
   ```bash
   sudo apt-get install python3-tk  # Ubuntu/Debian
   sudo yum install tkinter          # CentOS/RHEL
   ```

3. **Use Virtual Display**
   ```bash
   pip install xvfb
   xvfb-run -a python src/ivm_system.py plot tetrahedron 1
   ```

#### Plot Display Issues
**Symptoms:**
```
Figure not showing, blank plots, or distorted visualizations
```

**Solutions:**

1. **Update Matplotlib**
   ```bash
   pip install --upgrade matplotlib
   ```

2. **Check Coordinate Data**
   ```python
   from ivm_package.coordinates import IVMCoordinates

   coords = IVMCoordinates()
   data = coords.get_polyhedron('tetrahedron', 1)
   print(f"Coordinates: {data.coordinates}")
   print(f"Sphere count: {data.sphere_count}")
   ```

3. **Test Basic Plotting**
   ```python
   import matplotlib.pyplot as plt
   import numpy as np

   # Test basic 3D plotting
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   ax.scatter([1, 0, 0], [0, 1, 0], [0, 0, 1])
   plt.savefig('test_plot.png')
   ```

### File and Path Issues

#### Permission Errors
**Symptoms:**
```
PermissionError: [Errno 13] Permission denied: 'outputs/plots/filename.png'
OSError: [Errno 28] No space left on device
```

**Solutions:**

1. **Check Permissions**
   ```bash
   # Ensure write permissions
   chmod 755 outputs/
   mkdir -p outputs/plots outputs/animations outputs/docs
   chmod 755 outputs/plots outputs/animations outputs/docs
   ```

2. **Check Disk Space**
   ```bash
   df -h  # Check available space
   du -sh outputs/  # Check output directory size
   ```

3. **Clean Output Directory**
   ```bash
   # Remove old files if needed
   rm -rf outputs/*
   mkdir -p outputs/plots outputs/animations outputs/docs
   ```

#### Path Issues
**Symptoms:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'configs/ivm_coordinates.json'
```

**Solutions:**

1. **Verify File Existence**
   ```bash
   ls -la configs/ivm_coordinates.json
   ls -la docs/original/xyz_clean.md  # Noel Coughlin's coordinate paper
   ```

2. **Create Missing Directories**
   ```bash
   mkdir -p configs outputs/plots outputs/animations outputs/docs
   ```

3. **Use Absolute Paths**
   ```python
   import os
   config_path = os.path.join(os.getcwd(), 'configs', 'ivm_coordinates.json')
   ```

### Animation Issues

#### Animation Generation Failures
**Symptoms:**
```
ValueError: Invalid animation parameters
MemoryError: Out of memory during animation
```

**Solutions:**

1. **Reduce Frame Count**
   ```python
   # Use fewer frames for large polyhedrons
   ivm.animate_transformation('tetrahedron', '4', frames=20)
   ```

2. **Process Individually**
   ```python
   # Don't create multiple large animations simultaneously
   for freq in [1, 2, 3]:
       ivm.animate_transformation('tetrahedron', str(freq), frames=30)
   ```

3. **Check Memory Usage**
   ```python
   import psutil
   print(f"Memory usage: {psutil.virtual_memory().percent}%")
   ```

#### GIF Quality Issues
**Symptoms:**
```
Large file sizes, poor image quality, or generation failures
```

**Solutions:**

1. **Optimize Frame Count**
   ```python
   # Balance quality vs file size
   ivm.animate_transformation('tetrahedron', '2', frames=45)  # Medium quality
   ```

2. **Check Pillow Installation**
   ```bash
   # GIFs are written with matplotlib's Pillow writer
   python -c "import PIL; print(PIL.__version__)"
   ```

3. **Alternative Backends**
   ```python
   # Try different matplotlib backends
   import matplotlib
   matplotlib.use('TkAgg')  # Or 'Qt5Agg'
   ```

### Performance Issues

#### Slow Execution
**Symptoms:**
```
Operations taking longer than expected, system hanging
```

**Solutions:**

1. **Monitor System Resources**
   ```bash
   # Check CPU and memory usage
   top -p $(pgrep python)
   ```

2. **Optimize Operations**
   ```python
   # Use batch processing for multiple operations
   ivm.create_comprehensive_output_package()  # Single optimized call
   ```

3. **Reduce Complexity**
   ```python
   # Use smaller frame counts for testing
   ivm.animate_transformation('tetrahedron', '1', frames=15)
   ```

#### Memory Issues
**Symptoms:**
```
MemoryError, system becoming unresponsive
```

**Solutions:**

1. **Monitor Memory Usage**
   ```python
   import tracemalloc

   tracemalloc.start()
   # Your operations here
   current, peak = tracemalloc.get_traced_memory()
   print(f"Memory: {current/1024**2:.1f}MB, Peak: {peak/1024**2:.1f}MB")
   tracemalloc.stop()
   ```

2. **Process in Batches**
   ```python
   # Process polyhedrons individually
   polyhedrons = ['tetrahedron', 'cube', 'octahedron']
   for poly in polyhedrons:
       ivm.plot_polyhedron(poly, '1')
   ```

3. **Clean Up Memory**
   ```python
   import gc
   gc.collect()  # Force garbage collection
   ```

### Configuration Issues

#### Config File Problems
**Symptoms:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'configs/ivm_coordinates.json'
JSONDecodeError: Expecting ',' delimiter
```

**Solutions:**

1. **Verify Config File**
   ```bash
   # Check if config file exists and is valid JSON
   python -c "import json; json.load(open('configs/ivm_coordinates.json'))"
   ```

2. **Regenerate Config**
   ```python
   from ivm_package.config import IVMConfig

   # Create default config
   config = IVMConfig()
   config.save_coordinates()
   ```

3. **Custom Config Location**
   ```python
   # Use custom config path
   config = IVMConfig('path/to/custom_config.json')
   ```

### Data Issues

#### Coordinate Data Problems
**Symptoms:**
```
ValueError: Unknown polyhedron type: 'tetrahedron'
ValueError: Unknown frequency 5 for tetrahedron
```

**Solutions:**

1. **Check Available Data**
   ```python
   ivm = IVMSystem()
   ivm.list_available_data()
   ```

2. **Verify Coordinate Loading**
   ```python
   from ivm_package.coordinates import IVMCoordinates

   coords = IVMCoordinates()
   print("Available polyhedrons:", coords.list_polyhedrons())
   ```

3. **Reload Data**
   ```python
   # Force reload coordinate data
   coords = IVMCoordinates()
   coords._load_coordinates()
   ```

#### Mathematical Property Issues
**Symptoms:**
```
AssertionError: Coordinate magnitudes not equal to 1
AssertionError: Center of mass not at origin
```

**Solutions:**

1. **Verify Data Integrity**
   ```python
   import numpy as np

   coords = IVMCoordinates()
   data = coords.get_polyhedron('tetrahedron', 1)
   coordinates = np.array(data.coordinates)

   # Check magnitudes
   magnitudes = np.linalg.norm(coordinates, axis=1)
   print("Magnitude range:", magnitudes.min(), "to", magnitudes.max())

   # Check center of mass
   center = np.mean(coordinates, axis=0)
   print("Center of mass:", center)
   ```

2. **Report Data Issues**
   ```python
   # If data appears corrupted, report to maintainers
   print("Data may be corrupted - check source files")
   ```

## 🔧 Debug Mode

### Enable Debug Logging
```python
import logging

# Enable debug output
logging.basicConfig(level=logging.DEBUG)

# Run with detailed logging
ivm = IVMSystem()
ivm.create_comprehensive_visualizations()
```

### Interactive Debugging
```python
from ivm_system import IVMSystem

ivm = IVMSystem()

# Step through operations
print("1. System initialized")
coords = ivm.coordinates
print("2. Coordinates loaded")

# Check specific data
tetra_data = coords.get_polyhedron('tetrahedron', 1)
print(f"3. Tetrahedron data: {tetra_data.sphere_count} spheres")

# Test visualization
print("4. Creating visualization...")
ivm.plot_polyhedron('tetrahedron', '1')
print("5. Visualization complete")
```

### Performance Profiling
```python
import cProfile
import pstats

# Profile system operations
profiler = cProfile.Profile()
profiler.enable()

ivm = IVMSystem()
ivm.create_comprehensive_visualizations()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

## 📊 System Health Checks

### Quick Health Check
```bash
#!/bin/bash
# system_health_check.sh

echo "=== IVM System Health Check ==="

# Check Python path
echo "1. Python path:"
python -c "import sys; print('Python path includes src:', 'src' in str(sys.path))"

# Check dependencies
echo "2. Dependencies:"
python -c "import numpy, matplotlib; print('NumPy:', numpy.__version__); print('Matplotlib:', matplotlib.__version__)"

# Check coordinate data
echo "3. Coordinate data:"
python -c "
import sys
sys.path.insert(0, 'src')
from ivm_package.coordinates import IVMCoordinates
coords = IVMCoordinates()
print('Polyhedrons available:', len(coords.list_polyhedrons()))
"

# Check file permissions
echo "4. File permissions:"
ls -ld outputs/ configs/ 2>/dev/null || echo "Directory issues detected"

echo "=== Health Check Complete ==="
```

### Comprehensive System Test
```python
def system_health_check():
    """Comprehensive system health check"""
    from ivm_system import IVMSystem
    import traceback

    print("Running comprehensive health check...")

    try:
        # 1. Initialize system
        print("✓ System initialization")
        ivm = IVMSystem()

        # 2. Check coordinate loading
        print("✓ Coordinate loading")
        coords = ivm.coordinates

        # 3. Test basic plotting
        print("✓ Basic plotting")
        ivm.plot_polyhedron('tetrahedron', '1')

        # 4. Test animation
        print("✓ Animation creation")
        ivm.animate_transformation('tetrahedron', '1', frames=10)

        # 5. Test comparison
        print("✓ Polyhedron comparison")
        ivm.compare_polyhedrons([('tetrahedron', '1'), ('cube', '1')])

        # 6. Test documentation
        print("✓ Documentation generation")
        ivm.create_documentation()

        print("🎉 All systems operational!")
        return True

    except Exception as e:
        print(f"❌ Health check failed: {e}")
        traceback.print_exc()
        return False

# Run health check
system_health_check()
```

## 🚑 Emergency Recovery

### Reset System to Defaults
```python
from ivm_package.config import IVMConfig

# Reset to default configuration
config = IVMConfig()  # Creates default config
config.save_coordinates()

# Clear output directories
import shutil
shutil.rmtree('outputs', ignore_errors=True)
```

### Regenerate All Data
```bash
#!/bin/bash
# complete_reset.sh

echo "Resetting IVM system to defaults..."

# Remove existing data
rm -rf outputs/
rm -f configs/ivm_coordinates.json

# Regenerate everything
python src/ivm_system.py comprehensive

echo "System reset complete!"
```

### Manual Data Verification
```python
# Verify coordinate data integrity
from ivm_package.coordinates import IVMCoordinates
import numpy as np

coords = IVMCoordinates()

for poly in coords.list_polyhedrons():
    for freq in coords.list_frequencies(poly):
        data = coords.get_polyhedron(poly, freq)
        coordinates = np.array(data.coordinates)

        # Check unit vectors
        magnitudes = np.linalg.norm(coordinates, axis=1)
        assert np.allclose(magnitudes, 1.0, atol=1e-10), f"Invalid magnitudes for {poly} F{freq}"

        # Check center of mass
        center = np.mean(coordinates, axis=0)
        assert np.allclose(center, [0, 0, 0], atol=1e-10), f"Invalid center for {poly} F{freq}"

        print(f"✓ {poly} F{freq}: {data.sphere_count} spheres, valid coordinates")
```

## 📞 Getting Help

### Documentation Resources
- **[📖 Complete Documentation](../../outputs/docs/output_summary.md)**: Full system documentation
- **[🔧 API Reference](../api/)**: Complete API documentation
- **[🧪 Test Coverage](../generated/test_coverage.md)**: Testing information
- **[📈 Mathematical Foundation](../generated/mathematical_foundation.md)**: Technical details

### Community Support
- **GitHub Issues**: Report bugs and request features
- **Discussions**: Ask questions and share insights
- **Pull Requests**: Contribute improvements

### Professional Support
For research applications or custom development:
- Contact the maintainers through GitHub
- Provide detailed use case descriptions
- Include system specifications and requirements

## 🔍 Diagnostic Tools

### System Information Script
```python
def system_diagnostics():
    """Gather comprehensive system information"""
    import platform
    import sys
    import numpy as np
    import matplotlib

    print("=== System Diagnostics ===")
    print(f"Platform: {platform.platform()}")
    print(f"Python: {sys.version}")
    print(f"NumPy: {np.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"Matplotlib backend: {matplotlib.get_backend()}")

    # Check file system
    import os
    print(f"Current directory: {os.getcwd()}")
    print(f"Config file exists: {os.path.exists('configs/ivm_coordinates.json')}")
    print(f"Output directory exists: {os.path.exists('outputs')}")

    # Check coordinate data
    try:
        from ivm_package.coordinates import IVMCoordinates
        coords = IVMCoordinates()
        polyhedrons = coords.list_polyhedrons()
        print(f"Available polyhedrons: {len(polyhedrons)}")
        print(f"Polyhedron types: {polyhedrons}")
    except Exception as e:
        print(f"Coordinate loading failed: {e}")

# Run diagnostics
system_diagnostics()
```

### Log Analysis
```python
import logging

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ivm_debug.log'),
        logging.StreamHandler()
    ]
)

# Run operations with logging
logger = logging.getLogger(__name__)
logger.info("Starting IVM system diagnostics...")

ivm = IVMSystem()
ivm.list_available_data()

logger.info("Diagnostics complete")
```

## 🛠️ Maintenance Procedures

### Regular Maintenance
```bash
# Weekly maintenance script
#!/bin/bash

echo "Performing weekly maintenance..."

# Run tests
echo "1. Running test suite..."
python -m pytest tests/ -q

# Check disk usage
echo "2. Checking disk usage..."
du -sh outputs/

# Clean old temporary files
echo "3. Cleaning temporary files..."
find outputs/temp -type f -mtime +7 -delete

# Regenerate documentation if needed
echo "4. Checking documentation..."
if [ ! -f "outputs/docs/README.md" ]; then
    echo "Regenerating documentation..."
    python src/ivm_system.py docs
fi

echo "Maintenance complete!"
```

### Performance Monitoring
```python
def performance_monitor():
    """Monitor system performance"""
    import time
    import tracemalloc

    operations = [
        ('coordinate_loading', lambda: IVMCoordinates()),
        ('tetrahedron_plot', lambda: ivm.plot_polyhedron('tetrahedron', '1')),
        ('animation_creation', lambda: ivm.animate_transformation('tetrahedron', '1', frames=10)),
    ]

    tracemalloc.start()

    for name, operation in operations:
        start_time = time.time()
        start_memory = tracemalloc.get_traced_memory()[0]

        try:
            operation()
            success = True
        except Exception as e:
            print(f"❌ {name} failed: {e}")
            success = False

        end_time = time.time()
        end_memory = tracemalloc.get_traced_memory()[0]

        if success:
            duration = end_time - start_time
            memory_used = (end_memory - start_memory) / 1024**2
            print(f"✓ {name}: {duration:.3f}s, {memory_used:.1f}MB")

    tracemalloc.stop()

# Monitor performance
performance_monitor()
```

## 🎯 Prevention Strategies

### Best Practices
1. **Regular Backups**: Keep copies of important output files
2. **Version Control**: Track configuration and data changes
3. **Testing**: Run tests before major operations
4. **Monitoring**: Track system performance trends
5. **Documentation**: Keep notes on custom configurations

### Proactive Monitoring
```python
# Create monitoring script
def create_monitoring_script():
    """Generate monitoring script for regular use"""
    script = '''
#!/bin/bash
# Daily monitoring script

echo "=== Daily IVM System Check ==="
date

# Check system health
python -c "
import sys
sys.path.insert(0, 'src')
from ivm_system import IVMSystem

try:
    ivm = IVMSystem()
    print('✓ System operational')
    ivm.list_available_data()
except Exception as e:
    print('❌ System issues detected:', e)
"

echo "=== Check Complete ==="
'''
    with open('daily_check.sh', 'w') as f:
        f.write(script)
    print("Monitoring script created: daily_check.sh")

# Create monitoring script
create_monitoring_script()
```

---

*This troubleshooting guide provides comprehensive solutions for common issues and maintenance procedures for the IVM Polyhedron Visualization System.*
