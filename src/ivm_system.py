#!/usr/bin/env python3
"""
IVM System - Main Interface
Unified interface for the Isotropic Vector Matrix visualization system
"""

import sys
import argparse
from typing import List, Optional

# Import from src package
sys.path.insert(0, 'src')

from ivm_package import IVMVisualizer, IVMCoordinates, get_config

class IVMSystem:
    """Main system interface for IVM visualization"""

    def __init__(self):
        self.coordinates = IVMCoordinates()
        self.visualizer = IVMVisualizer()
        self.visualizer.load_coordinates()
        self.visualizer.coordinates = self.coordinates  # Make coordinates accessible to visualizer
        self.config = get_config()

    def plot_polyhedron(self, polyhedron_type: str, frequency: str,
                       show_vectors: bool = False, save_path: Optional[str] = None):
        """Plot a polyhedron with optional vector display"""
        self.visualizer.plot_polyhedron(
            polyhedron_type, frequency,
            show_vectors=show_vectors,
            save_path=save_path
        )

    def animate_transformation(self, polyhedron_type: str, frequency: str,
                              frames: Optional[int] = None, save_path: Optional[str] = None):
        """Animate sphere-to-vector transformation"""
        self.visualizer.animate_sphere_to_vector(
            polyhedron_type, frequency,
            frames=frames,
            save_path=save_path
        )

    def compare_polyhedrons(self, comparisons: List[tuple],
                           save_path: Optional[str] = None):
        """Compare multiple polyhedrons side by side"""
        self.visualizer.compare_polyhedrons(comparisons, save_path=save_path)

    def create_documentation(self, output_dir: Optional[str] = None):
        """Create comprehensive documentation"""
        self.visualizer.create_coordinate_documentation(output_dir)
        print(f"Documentation created in {output_dir or self.config.output_paths.docs_dir}/")

    def create_comprehensive_visualizations(self):
        """Create all comprehensive visualizations from xyz_clean.md"""
        self.visualizer.create_comprehensive_visualizations()

    def create_comprehensive_animations(self):
        """Create all comprehensive animations from xyz_clean.md"""
        self.visualizer.create_comprehensive_animations()

    def create_additional_visualizations(self):
        """Create additional visualizations for deeper understanding"""
        self.visualizer.create_additional_visualizations()

    def create_all_polyhedron_visualizations(self):
        """Create visualizations for all polyhedrons at all frequencies"""
        self.visualizer.create_all_polyhedron_visualizations()

    def create_comprehensive_output_package(self):
        """Create a complete output package with all visualizations"""
        self.visualizer.create_comprehensive_output_package()

    def create_html_visualizations(self):
        """Create interactive HTML visualizations"""
        self.visualizer.create_html_visualizations()

    def run_tests(self):
        """Run the complete test suite"""
        print("Running IVM System Tests...")
        print("=" * 50)

        # Import and run tests
        sys.path.insert(0, 'tests')
        import test_ivm_system
        results = test_ivm_system.run_all_tests()
        return results

    def list_available_data(self):
        """List all available polyhedrons and frequencies"""
        print("Available IVM Polyhedron Data:")
        print("=" * 40)

        for poly_type in self.coordinates.list_polyhedrons():
            print(f"\n{poly_type.title()}:")
            for freq in self.coordinates.list_frequencies(poly_type):
                data = self.coordinates.get_polyhedron(poly_type, freq)
                print(f"  Frequency {freq}: {data.sphere_count} spheres ({data.orientation} orientation)")

def main():
    """Main command-line interface"""
    parser = argparse.ArgumentParser(
        description="IVM Polyhedron Visualization System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ivm_system.py plot tetrahedron 1
  python ivm_system.py animate tetrahedron 2 --frames 60
  python ivm_system.py compare tetrahedron 1 cube 1
  python ivm_system.py docs
  python ivm_system.py visualize                    # Create concept visualizations
  python ivm_system.py animations                    # Create comprehensive animations
  python ivm_system.py additional                    # Create additional visualizations
  python ivm_system.py polyhedrons                   # Create all polyhedron plots
  python ivm_system.py html                         # Create interactive HTML interface
  python ivm_system.py comprehensive                 # Create complete output package
  python ivm_system.py test
  python ivm_system.py list
        """
    )

    parser.add_argument('command', choices=['plot', 'animate', 'compare', 'docs', 'test', 'list',
                                           'visualize', 'animations', 'additional', 'polyhedrons', 'comprehensive', 'html'],
                       help='Command to execute')

    parser.add_argument('polyhedron', nargs='?', help='Polyhedron type (tetrahedron, cube, etc.)')
    parser.add_argument('frequency', nargs='?', help='Frequency of the polyhedron')

    # Optional arguments
    parser.add_argument('--vectors', action='store_true', help='Show vectors in plot')
    parser.add_argument('--frames', type=int, help='Number of animation frames')
    parser.add_argument('--output', '-o', help='Output file path for saving plots/animations')
    parser.add_argument('--comparisons', nargs='*',
                       help='Polyhedron comparisons (e.g., tetrahedron 1 cube 1)')

    args = parser.parse_args()

    # Initialize system
    system = IVMSystem()

    try:
        if args.command == 'list':
            system.list_available_data()

        elif args.command == 'plot':
            if not args.polyhedron or not args.frequency:
                print("Error: plot command requires polyhedron and frequency")
                sys.exit(1)

            system.plot_polyhedron(args.polyhedron, args.frequency,
                                   show_vectors=args.vectors, save_path=args.output)

        elif args.command == 'animate':
            if not args.polyhedron or not args.frequency:
                print("Error: animate command requires polyhedron and frequency")
                sys.exit(1)

            system.animate_transformation(args.polyhedron, args.frequency,
                                          frames=args.frames, save_path=args.output)

        elif args.command == 'compare':
            if not args.comparisons:
                print("Error: compare command requires polyhedron comparisons")
                sys.exit(1)

            # Parse comparisons (polyhedron frequency pairs)
            comparisons = []
            for i in range(0, len(args.comparisons), 2):
                if i + 1 < len(args.comparisons):
                    poly_type = args.comparisons[i]
                    freq = args.comparisons[i + 1]
                    comparisons.append((poly_type, freq))

            system.compare_polyhedrons(comparisons, save_path=args.output)

        elif args.command == 'docs':
            system.create_documentation()

        elif args.command == 'visualize':
            system.create_comprehensive_visualizations()

        elif args.command == 'animations':
            system.create_comprehensive_animations()

        elif args.command == 'additional':
            system.create_additional_visualizations()

        elif args.command == 'polyhedrons':
            system.create_all_polyhedron_visualizations()

        elif args.command == 'comprehensive':
            system.create_comprehensive_output_package()

        elif args.command == 'html':
            system.create_html_visualizations()

        elif args.command == 'test':
            results = system.run_tests()
            if not results.wasSuccessful():
                sys.exit(1)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
