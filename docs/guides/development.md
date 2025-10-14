# Development Guide - IVM Polyhedron Visualization System

Complete development guide for extending and contributing to the IVM system.

## Project Structure

### Core Architecture
```
src/ivm_package/
├── coordinates.py    # Coordinate data management
├── visualizer.py     # Visualization and animation engine
└── config.py         # Configuration and output management
```

### Testing Framework
```
tests/
├── test_ivm_system.py  # Comprehensive test suite
└── __init__.py
```

### Documentation
```
docs/
├── original/         # Source materials
├── generated/        # Auto-generated docs
├── api/             # API documentation
└── guides/          # User guides
```

## Development Setup

### Prerequisites
```bash
# Python 3.7+ with development tools
python3 -m pip install --upgrade pip setuptools wheel

# Development dependencies
pip install numpy matplotlib pytest black flake8 mypy
```

### Repository Setup
```bash
# Clone repository
git clone https://github.com/your-repo/godel_ivm.git
cd godel_ivm

# Install in development mode
pip install -e .

# Run tests
python -m pytest tests/
```

### IDE Configuration

#### Visual Studio Code
```json
{
    "python.pythonPath": "src",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": false,
    "python.linting.flake8Enabled": true,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.formatting.provider": "black"
}
```

#### PyCharm
- Set Python interpreter to use `src/` directory
- Enable pytest for test discovery
- Configure code style with black
- Enable type checking with mypy

## Code Style

### Formatting
```bash
# Format code with black
black src/ tests/ docs/

# Check formatting
black --check src/ tests/ docs/
```

### Linting
```bash
# Run flake8
flake8 src/ tests/ docs/

# Run mypy for type checking
mypy src/ tests/
```

### Pre-commit Hooks
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run all checks
pre-commit run --all-files
```

## Adding New Features

### 1. New Polyhedron Type

**Step 1: Add coordinate data**
```python
# In src/ivm_package/coordinates.py
def _load_coordinates(self):
    # Add new polyhedron data
    self.polyhedrons['new_polyhedron'] = {
        '1': PolyhedronData(
            frequency=1,
            sphere_count=8,
            coordinates=[(1, 0, 0), (0, 1, 0), (0, 0, 1), ...],
            polyhedron_type='new_polyhedron',
            orientation='first'
        )
    }
```

**Step 2: Add visualization methods**
```python
# In src/ivm_package/visualizer.py
def plot_new_polyhedron(self, frequency):
    # Custom visualization logic
    pass
```

**Step 3: Add tests**
```python
# In tests/test_ivm_system.py
def test_new_polyhedron(self):
    coords = IVMCoordinates()
    data = coords.get_polyhedron('new_polyhedron', '1')
    self.assertEqual(data.sphere_count, 8)
```

**Step 4: Update documentation**
```python
# Update README.md and API docs
```

### 2. New Visualization Type

**Step 1: Add method to visualizer**
```python
def create_custom_visualization(self):
    # Custom visualization logic
    pass
```

**Step 2: Add HTML support**
```python
# Update HTML interface
def _create_custom_html_page(self):
    # Custom HTML generation
    pass
```

**Step 3: Add tests**
```python
def test_custom_visualization(self):
    viz = IVMVisualizer()
    # Test custom visualization
    pass
```

### 3. New Animation Type

**Step 1: Add animation method**
```python
def animate_custom_process(self, polyhedron_type, frequency):
    # Custom animation logic
    pass
```

**Step 2: Update HTML interface**
```python
# Add to animation gallery
```

## Testing Guidelines

### Test Categories

1. **Unit Tests**: Test individual functions and methods
2. **Integration Tests**: Test component interactions
3. **Mathematical Tests**: Verify coordinate properties
4. **Performance Tests**: Validate execution speed
5. **Error Handling Tests**: Test exception handling

### Test Structure
```python
class TestNewFeature(unittest.TestCase):
    def setUp(self):
        # Setup test fixtures
        pass

    def test_basic_functionality(self):
        # Test core functionality
        pass

    def test_edge_cases(self):
        # Test edge cases and error conditions
        pass

    def test_performance(self):
        # Test performance characteristics
        pass
```

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test class
python -m pytest tests.test_ivm_system.TestNewFeature

# Run with coverage
python -m pytest --cov=src tests/

# Run with verbose output
python -m pytest -v tests/
```

## Documentation Guidelines

### API Documentation
- Use docstrings for all public methods
- Include parameter types and return values
- Provide usage examples
- Document exceptions and error conditions

### User Documentation
- Keep guides simple and accessible
- Include step-by-step instructions
- Provide troubleshooting information
- Include examples for common use cases

### Technical Documentation
- Document mathematical foundations
- Include algorithm descriptions
- Provide performance analysis
- Include extension points

## Performance Optimization

### Profiling
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code to profile
ivm = IVMSystem()
ivm.plot_polyhedron('tetrahedron', '4')

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(20)
```

### Memory Optimization
```python
import tracemalloc

tracemalloc.start()

# Code to profile
ivm = IVMSystem()
ivm.create_comprehensive_animations()

current, peak = tracemalloc.get_traced_memory()
print(f"Memory: {current / 1024**2:.2f} MB, Peak: {peak / 1024**2:.2f} MB")
tracemalloc.stop()
```

### Optimization Strategies
1. **Lazy loading**: Load data only when needed
2. **Caching**: Cache expensive computations
3. **Batch processing**: Process multiple items together
4. **Memory management**: Clean up large objects

## Debugging

### Debug Mode
```python
import logging

logging.basicConfig(level=logging.DEBUG)

# Enable debug logging
ivm = IVMSystem()
ivm.create_comprehensive_output_package()
```

### Interactive Debugging
```python
from ivm_system import IVMSystem

ivm = IVMSystem()

# Step through operations
coords = ivm.coordinates.get_polyhedron('tetrahedron', '1')
viz = ivm.visualizer
viz.plot_polyhedron('tetrahedron', '1')
```

### Common Debugging Patterns
```python
# Check data integrity
data = coords.get_polyhedron('tetrahedron', '1')
assert len(data.coordinates) == data.sphere_count

# Check coordinate properties
magnitudes = [np.linalg.norm(coord) for coord in data.coordinates]
assert all(abs(mag - 1.0) < 1e-10 for mag in magnitudes)
```

## Code Review Guidelines

### Before Submitting Changes
1. **Run tests**: `python -m pytest tests/`
2. **Check formatting**: `black --check src/ tests/`
3. **Linting**: `flake8 src/ tests/`
4. **Type checking**: `mypy src/ tests/`
5. **Documentation**: Update relevant docs

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass and provide good coverage
- [ ] Documentation is updated
- [ ] Performance impact assessed
- [ ] Error handling is appropriate
- [ ] Backward compatibility maintained

## Version Control

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new_polyhedron

# Make changes
git add .
git commit -m "Add new polyhedron type"

# Push and create PR
git push origin feature/new_polyhedron
```

### Release Process
1. Update version numbers
2. Update changelog
3. Run full test suite
4. Create release notes
5. Tag release

## API Design Principles

### Consistency
- Use consistent parameter naming
- Follow established patterns
- Maintain backward compatibility

### Clarity
- Clear, descriptive method names
- Comprehensive docstrings
- Intuitive parameter ordering

### Robustness
- Proper error handling
- Input validation
- Graceful degradation

## Extension Points

### Adding New Visualization Types
1. Extend `IVMVisualizer` class
2. Add method to `create_additional_visualizations()`
3. Update HTML interface
4. Add tests

### Adding New Polyhedron Types
1. Add coordinate data to `IVMCoordinates`
2. Update frequency mappings
3. Add visualization methods if needed
4. Update tests and documentation

### Custom Configuration
1. Extend configuration dataclasses
2. Update config loading/saving
3. Add validation methods
4. Update documentation

## Performance Considerations

### Large Datasets
- **Frequency 4 tetrahedron**: 35 spheres
- **Animation frames**: 60+ frames per animation
- **Memory usage**: ~100MB for full system
- **Processing time**: < 5 seconds for animations

### Optimization Techniques
- **Lazy loading**: Load data only when needed
- **Caching**: Cache expensive computations
- **Batch processing**: Process multiple items together
- **Memory management**: Clean up large objects

## Security Considerations

### File Handling
- Validate file paths
- Check permissions before writing
- Sanitize user inputs
- Handle path traversal attacks

### Configuration
- Validate configuration values
- Use safe defaults
- Handle malformed config files gracefully

## Deployment

### Package Distribution
```bash
# Build package
python -m build

# Upload to PyPI
twine upload dist/*
```

### Docker Deployment
```dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN pip install numpy matplotlib
RUN pip install -e .

CMD ["python", "src/ivm_system.py", "comprehensive"]
```

## Maintenance

### Regular Tasks
- **Test execution**: Run test suite before releases
- **Performance monitoring**: Track execution times
- **Dependency updates**: Keep dependencies current
- **Security updates**: Monitor for vulnerabilities

### Long-term Maintenance
- **Code refactoring**: Improve code quality over time
- **Documentation updates**: Keep docs current
- **Performance optimization**: Identify and fix bottlenecks
- **Feature deprecation**: Remove obsolete features

## Contributing Guidelines

### Getting Started
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Update documentation
6. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints
- Write comprehensive docstrings
- Add appropriate tests
- Update documentation

### Review Process
1. Automated checks (linting, tests)
2. Code review by maintainers
3. Integration testing
4. Documentation review
5. Merge approval

## Support and Communication

### Issue Tracking
- Use GitHub issues for bug reports
- Use feature requests for new functionality
- Include detailed reproduction steps
- Provide system information

### Discussion
- Use GitHub discussions for questions
- Use pull request comments for code discussion
- Maintain respectful and constructive communication

### Documentation Updates
- Update documentation for new features
- Keep examples current
- Fix documentation bugs promptly

---

*This development guide provides comprehensive instructions for extending and maintaining the IVM Polyhedron Visualization System.*

