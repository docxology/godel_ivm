#!/usr/bin/env python3
"""
Coordinate Extractor for IVM Polyhedron Data
Extracts and organizes coordinate data from xyz_clean.md
"""

import re
import json
from collections import defaultdict
from typing import Dict, List, Tuple

class CoordinateExtractor:
    def __init__(self):
        self.polyhedron_data = defaultdict(lambda: defaultdict(list))
        self.constants = {}
        self.section_markers = {}

    def extract_coordinates(self, filename: str) -> Dict:
        """Extract all coordinate data from the markdown file"""
        with open(filename, 'r') as f:
            content = f.read()

        # Split content into sections based on headers
        sections = self._split_into_sections(content)

        # Extract coordinates from each section
        for section_name, section_content in sections.items():
            self._parse_section(section_name, section_content)

        return dict(self.polyhedron_data)

    def _split_into_sections(self, content: str) -> Dict[str, str]:
        """Split content into sections based on markdown headers"""
        sections = {}
        current_section = "preamble"
        sections[current_section] = ""

        lines = content.split('\n')

        for line in lines:
            # Check for section headers (lines starting with A-Z) followed by :)
            if re.match(r'^[A-Z]\)', line.strip()):
                current_section = line.strip()
                sections[current_section] = ""
            else:
                sections[current_section] += line + '\n'

        return sections

    def _parse_section(self, section_name: str, content: str):
        """Parse coordinate data from a section"""
        # Find polyhedron frequency definitions
        polyhedron_patterns = [
            (r'(\d+)\s*Frequency\s*Tetrahedron.*?(\d+)\s*Spheres?:?\s*$', 'tetrahedron'),
            (r'(\d+)\s*Frequency\s*Octahedron.*?(\d+)\s*Spheres?:?\s*$', 'octahedron'),
            (r'(\d+)\s*Frequency\s*Cube.*?(\d+)\s*Spheres?:?\s*$', 'cube'),
            (r'(\d+)\s*Frequency\s*(?:Cuboctahedron|VE).*?(\d+)\s*Spheres?:?\s*$', 'cuboctahedron'),
            (r'(\d+)\s*Frequency\s*Tetrakaidecahedron.*?(\d+)\s*Spheres?:?\s*$', 'tetrakaidecahedron'),
            (r'(\d+)\s*Frequency\s*Truncated\s*Tetrahedron.*?(\d+)\s*Spheres?:?\s*$', 'truncated_tetrahedron'),
        ]

        for pattern, poly_type in polyhedron_patterns:
            matches = re.finditer(pattern, content, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                frequency = int(match.group(1))
                sphere_count = int(match.group(2))

                # Extract coordinates that follow this definition
                coords = self._extract_coordinates_after_match(content, match.end())

                if coords:
                    self.polyhedron_data[poly_type][frequency] = {
                        'sphere_count': sphere_count,
                        'coordinates': coords,
                        'section': section_name
                    }

        # Also look for special cases like 0 frequency
        zero_freq_pattern = r'0\s*Frequency\s*Tetrahedron.*?(\d+)\s*Spheres?:?\s*$'
        zero_match = re.search(zero_freq_pattern, content, re.IGNORECASE)
        if zero_match:
            frequency = 0
            sphere_count = int(zero_match.group(1))
            coords = self._extract_coordinates_after_match(content, zero_match.end())
            if coords:
                self.polyhedron_data['tetrahedron'][frequency] = {
                    'sphere_count': sphere_count,
                    'coordinates': coords,
                    'section': section_name
                }

    def _extract_coordinates_after_match(self, content: str, start_pos: int) -> List[Tuple[float, float, float]]:
        """Extract coordinate tuples from text starting after a given position"""
        coordinates = []

        # Look for coordinate patterns like (x, y, z) or (x,y,z)
        coord_pattern = r'\(\s*([+-]?\d*\.?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*\)'

        # Find all coordinates in the remaining content
        remaining_content = content[start_pos:start_pos + 2000]  # Look ahead 2000 chars

        matches = re.findall(coord_pattern, remaining_content)
        for match in matches:
            try:
                x, y, z = map(float, match)
                coordinates.append((x, y, z))
            except ValueError:
                continue

        return coordinates

def main():
    extractor = CoordinateExtractor()
    data = extractor.extract_coordinates('xyz_clean.md')

    # Save extracted data as JSON for easy inspection
    with open('extracted_coordinates.json', 'w') as f:
        json.dump(data, f, indent=2)

    # Print summary
    print("Extracted coordinate data:")
    for poly_type, frequencies in data.items():
        print(f"\n{poly_type.title()}:")
        for frequency, info in frequencies.items():
            coord_count = len(info['coordinates'])
            print(f"  Frequency {frequency}: {coord_count} coordinates")

if __name__ == "__main__":
    main()
