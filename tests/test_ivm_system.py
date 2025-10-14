#!/usr/bin/env python3
"""
Comprehensive Test Suite for IVM System
Tests all components: coordinates, visualization, and animations
"""

import unittest
import numpy as np
import os
import json
import tempfile
from unittest.mock import patch, MagicMock

# Import our modules
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ivm_package import coordinates as ivm_coordinates
from ivm_package import visualizer as ivm_visualizer
from ivm_package import config as ivm_config

class TestIVMCoordinates(unittest.TestCase):
    """Test the IVM coordinates module"""

    def setUp(self):
        """Set up test fixtures"""
        self.ivm_coords = ivm_coordinates.IVMCoordinates()

    def test_polyhedron_initialization(self):
        """Test that polyhedrons are properly initialized"""
        self.assertIn('tetrahedron', self.ivm_coords.polyhedrons)
        self.assertIn('octahedron', self.ivm_coords.polyhedrons)
        self.assertIn('cube', self.ivm_coords.polyhedrons)

    def test_tetrahedron_coordinates(self):
        """Test tetrahedron coordinate data"""
        tetra_data = self.ivm_coords.get_polyhedron('tetrahedron', 1)

        self.assertEqual(tetra_data.frequency, 1)
        self.assertEqual(tetra_data.sphere_count, 4)
        self.assertEqual(len(tetra_data.coordinates), 4)

        # Check that coordinates are tuples of 3 floats
        for coord in tetra_data.coordinates:
            self.assertIsInstance(coord, tuple)
            self.assertEqual(len(coord), 3)
            for val in coord:
                self.assertIsInstance(val, float)

    def test_coordinate_symmetry(self):
        """Test that tetrahedron coordinates are symmetric"""
        tetra_data = self.ivm_coords.get_polyhedron('tetrahedron', 1)
        coords = tetra_data.coordinates

        # Check that coordinate sums are zero (center of mass at origin)
        coord_sum = np.sum(coords, axis=0)
        np.testing.assert_array_almost_equal(coord_sum, [0, 0, 0], decimal=5)

    def test_get_polyhedron_errors(self):
        """Test error handling for invalid polyhedron requests"""
        with self.assertRaises(ValueError):
            self.ivm_coords.get_polyhedron('invalid_type', 1)

        with self.assertRaises(ValueError):
            self.ivm_coords.get_polyhedron('tetrahedron', 999)

    def test_list_functions(self):
        """Test listing functions"""
        poly_types = self.ivm_coords.list_polyhedrons()
        self.assertIn('tetrahedron', poly_types)
        self.assertIn('cube', poly_types)

        tetra_freqs = self.ivm_coords.list_frequencies('tetrahedron')
        self.assertIn(1, tetra_freqs)
        self.assertIn(2, tetra_freqs)

    def test_json_export(self):
        """Test JSON export functionality"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name

        try:
            self.ivm_coords.save_to_json(temp_file)

            # Verify file was created and contains valid JSON
            with open(temp_file, 'r') as f:
                data = json.load(f)

            self.assertIn('tetrahedron', data)
            self.assertIn('1', data['tetrahedron'])

        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

class TestIVMVisualizer(unittest.TestCase):
    """Test the IVM visualizer module"""

    def setUp(self):
        """Set up test fixtures"""
        self.visualizer = ivm_visualizer.IVMVisualizer()
        self.visualizer.load_coordinates()

    def test_visualizer_initialization(self):
        """Test visualizer initialization"""
        self.assertIsNone(self.visualizer.figure)
        self.assertIsNone(self.visualizer.ax)
        self.assertIsInstance(self.visualizer.polyhedron_data, dict)

    def test_coordinate_loading(self):
        """Test coordinate data loading"""
        # Should load without errors
        self.assertIsInstance(self.visualizer.polyhedron_data, dict)

        # Should have tetrahedron data
        self.assertIn('tetrahedron', self.visualizer.polyhedron_data)

    def test_setup_plot(self):
        """Test plot setup"""
        self.visualizer.setup_plot()

        self.assertIsNotNone(self.visualizer.figure)
        self.assertIsNotNone(self.visualizer.ax)
        self.assertEqual(self.visualizer.figure.get_label(), '')

    def test_polyhedron_plotting(self):
        """Test plotting functionality"""
        # Test plotting tetrahedron (should not raise errors)
        try:
            # Mock plt.show() to avoid blocking in tests
            with patch('matplotlib.pyplot.show'):
                self.visualizer.plot_polyhedron('tetrahedron', 1)
        except Exception as e:
            self.fail(f"Plotting tetrahedron raised an exception: {e}")

    def test_animation_frame_creation(self):
        """Test animation frame creation"""
        coords = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

        frame = self.visualizer._create_animation_frame(coords, 0, 10)

        self.assertIn('coordinates', frame)
        self.assertIn('sphere_scale', frame)
        self.assertIn('vector_scale', frame)
        self.assertEqual(frame['sphere_scale'], 1.0)
        self.assertEqual(frame['vector_scale'], 0.0)

        # Test middle frame
        frame_mid = self.visualizer._create_animation_frame(coords, 5, 10)
        self.assertEqual(frame_mid['sphere_scale'], 0.5)
        self.assertEqual(frame_mid['vector_scale'], 0.5)

    def test_compare_polyhedrons(self):
        """Test polyhedron comparison functionality"""
        polyhedrons = [('tetrahedron', 1), ('cube', 1)]

        try:
            with patch('matplotlib.pyplot.show'):
                self.visualizer.compare_polyhedrons(polyhedrons)
        except Exception as e:
            self.fail(f"Comparing polyhedrons raised an exception: {e}")

    def test_documentation_creation(self):
        """Test documentation creation"""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.visualizer.create_coordinate_documentation(temp_dir)

            # Check that files were created
            index_file = os.path.join(temp_dir, 'coordinates_index.md')
            tetra_file = os.path.join(temp_dir, 'tetrahedron_coordinates.md')

            self.assertTrue(os.path.exists(index_file))
            self.assertTrue(os.path.exists(tetra_file))

            # Check content
            with open(index_file, 'r') as f:
                content = f.read()
                self.assertIn('IVM Polyhedron Coordinates Documentation', content)
                self.assertIn('Tetrahedron', content)

class TestIVMIntegration(unittest.TestCase):
    """Integration tests for the complete IVM system"""

    def test_coordinate_visualizer_integration(self):
        """Test that coordinates and visualizer work together"""
        # Create coordinates
        coords = ivm_coordinates.IVMCoordinates()

        # Create visualizer and load same data
        viz = ivm_visualizer.IVMVisualizer()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name

        try:
            coords.save_to_json(temp_file)
            viz.load_coordinates(temp_file)

            # Test that they have the same data
            self.assertEqual(
                len(coords.polyhedrons['tetrahedron']),
                len(viz.polyhedron_data['tetrahedron'])
            )

        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

    def test_coordinate_mathematical_properties(self):
        """Test mathematical properties of coordinates"""
        coords = ivm_coordinates.IVMCoordinates()
        tetra_data = coords.get_polyhedron('tetrahedron', 1)

        coordinates = np.array(tetra_data.coordinates)

        # Test that all coordinates have the same magnitude (unit vectors)
        magnitudes = np.linalg.norm(coordinates, axis=1)
        np.testing.assert_array_almost_equal(magnitudes, magnitudes[0], decimal=5)

        # Test orthogonality (vectors should be at 109.47 degrees to each other)
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                dot_product = np.dot(coordinates[i], coordinates[j])
                expected_angle = np.arccos(dot_product / (magnitudes[i] * magnitudes[j]))
                # Tetrahedral angle is approximately 109.47 degrees
                self.assertAlmostEqual(np.degrees(expected_angle), 109.47, delta=0.1)

class TestIVMPerformance(unittest.TestCase):
    """Performance tests for the IVM system"""

    def test_large_polyhedron_handling(self):
        """Test handling of large coordinate sets"""
        # Test with a moderately large tetrahedron (frequency 4)
        coords = ivm_coordinates.IVMCoordinates()

        # This should not take too long or use too much memory
        import time
        start_time = time.time()

        tetra_data = coords.get_polyhedron('tetrahedron', 4)
        end_time = time.time()

        # Should complete in reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Less than 1 second

        # Should have reasonable number of coordinates
        self.assertLess(tetra_data.sphere_count, 1000)  # Reasonable upper bound

def run_all_tests():
    """Run all tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestIVMCoordinates))
    suite.addTests(loader.loadTestsFromTestCase(TestIVMVisualizer))
    suite.addTests(loader.loadTestsFromTestCase(TestIVMIntegration))
    suite.addTests(loader.loadTestsFromTestCase(TestIVMPerformance))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result

if __name__ == "__main__":
    # Run tests when script is executed directly
    results = run_all_tests()

    # Print summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests run: {results.testsRun}")
    print(f"Failures: {len(results.failures)}")
    print(f"Errors: {len(results.errors)}")
    print(f"Success rate: {((results.testsRun - len(results.failures) - len(results.errors)) / results.testsRun * 100):.1f}%")

    if results.failures:
        print(f"\nFAILURES:")
        for test, traceback in results.failures:
            print(f"  - {test}: {traceback}")

    if results.errors:
        print(f"\nERRORS:")
        for test, traceback in results.errors:
            print(f"  - {test}: {traceback}")
