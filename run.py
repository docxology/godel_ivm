#!/usr/bin/env python3
"""
IVM Polyhedron Visualization System - Main Orchestrator

This script provides the top-level interface for the IVM system,
orchestrating all components and providing a unified entry point.
"""

import sys
import os
import argparse
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def main():
    """Main orchestrator function"""
    parser = argparse.ArgumentParser(
        description="IVM Polyhedron Visualization System - Main Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
IVM System Orchestrator

This script provides unified access to all IVM system functionality:

📦 PACKAGE STRUCTURE:
  src/ivm_package/     # Core modules
  tests/               # Test suite
  configs/             # Configuration data
  outputs/             # Generated content
  docs/                # Documentation

🎯 CORE COMPONENTS:
  • IVMCoordinates     # Coordinate data management
  • IVMVisualizer      # 3D visualization engine
  • IVMConfig          # Configuration management
  • IVMSystem          # Main system interface

🚀 QUICK START:
  python run.py comprehensive    # Generate everything
  python run.py test            # Run test suite
  python run.py docs            # Generate documentation

📚 DOCUMENTATION:
  See docs/README.md for complete documentation
  See outputs/docs/index.html for interactive interface

🔧 EXAMPLES:
  python run.py list                           # List available data
  python run.py plot tetrahedron 1             # Plot polyhedron
  python run.py animate tetrahedron 2          # Create animation
  python run.py compare tetrahedron 1 cube 1   # Compare polyhedrons
        """
    )

    # Core commands
    parser.add_argument('command', nargs='?', default='help',
                       choices=['help', 'list', 'plot', 'animate', 'compare', 'docs', 'test',
                               'visualize', 'animations', 'additional', 'polyhedrons',
                               'comprehensive', 'html', 'info'],
                       help='Command to execute')

    # Arguments for specific commands
    parser.add_argument('polyhedron', nargs='?', help='Polyhedron type')
    parser.add_argument('frequency', nargs='?', help='Frequency')

    # Options
    parser.add_argument('--vectors', action='store_true', help='Show vectors in plot')
    parser.add_argument('--frames', type=int, default=30, help='Animation frames')
    parser.add_argument('--output', '-o', help='Output file path')
    parser.add_argument('--comparisons', nargs='*', help='Polyhedron comparisons')

    # Import system components
    try:
        from ivm_system import IVMSystem
        system = IVMSystem()
    except ImportError as e:
        print(f"❌ Error importing IVM system: {e}")
        print("Make sure the src directory is properly set up.")
        print("Try: export PYTHONPATH=\"$PWD/src:$PYTHONPATH\"")
        sys.exit(1)

    args = parser.parse_args()

    # Execute commands
    try:
        if args.command == 'help':
            parser.print_help()
            print("\n" + "="*60)
            print("IVM SYSTEM STATUS:")
            print("="*60)

            # Check system health
            try:
                system.list_available_data()
                print("\n✅ System is ready to use!")
            except Exception as e:
                print(f"\n❌ System health check failed: {e}")

        elif args.command == 'list':
            system.list_available_data()

        elif args.command == 'plot':
            if not args.polyhedron or not args.frequency:
                print("❌ Error: plot command requires polyhedron and frequency")
                sys.exit(1)
            system.plot_polyhedron(args.polyhedron, args.frequency,
                                 show_vectors=args.vectors, save_path=args.output)

        elif args.command == 'animate':
            if not args.polyhedron or not args.frequency:
                print("❌ Error: animate command requires polyhedron and frequency")
                sys.exit(1)
            system.animate_transformation(args.polyhedron, args.frequency,
                                        frames=args.frames, save_path=args.output)

        elif args.command == 'compare':
            if not args.comparisons:
                print("❌ Error: compare command requires polyhedron comparisons")
                sys.exit(1)
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
            print("🚀 Generating complete IVM visualization package...")
            print("=" * 60)
            system.create_comprehensive_output_package()
            print("=" * 60)
            print("✅ Complete package generated!")
            print("\n📁 Output locations:")
            print("  • Plots: outputs/plots/")
            print("  • Animations: outputs/animations/")
            print("  • Documentation: outputs/docs/")
            print("  • Interactive interface: outputs/docs/index.html")

        elif args.command == 'html':
            system.create_html_visualizations()

        elif args.command == 'test':
            results = system.run_tests()
            if not results.wasSuccessful():
                print(f"\n❌ Tests failed: {len(results.failures)} failures, {len(results.errors)} errors")
                sys.exit(1)
            else:
                print("✅ All tests passed!")

        elif args.command == 'info':
            print("🎯 IVM Polyhedron Visualization System")
            print("=" * 50)
            print("📦 Version: 1.0.0")
            print("🔧 Python: 3.7+")
            print("📚 Based on R. Buckminster Fuller's Synergetics")
            print("🎨 Features: 3D plotting, animations, HTML interface")
            print("📁 Output: 40+ PNG files, 8+ GIF animations, HTML docs")

            # Show available data
            print("\n📊 Available Polyhedrons:")
            for poly_type in system.coordinates.list_polyhedrons():
                freqs = system.coordinates.list_frequencies(poly_type)
                print(f"  • {poly_type.title()}: {len(freqs)} frequencies")

    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

