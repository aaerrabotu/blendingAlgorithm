from itertools import combinations


def blend_colors(color1, color2, ratio):
    """
    Blends two colors based on a given ratio.

    Args:
        color1 (str or tuple): The first color in HEX or RGB format.
        color2 (str or tuple): The second color in HEX or RGB format.
        ratio (float): The blending ratio between 0.0 and 1.0.

    Returns:
        str: The blended color in HEX format.

    Raises:
        ValueError: If the color values are not valid.

    """
    def hex_to_rgb(hex_value):
        hex_value = hex_value.lstrip('#')
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb_value):
        return '#%02x%02x%02x' % rgb_value

    if isinstance(color1, str):
        color1 = hex_to_rgb(color1)
    if isinstance(color2, str):
        color2 = hex_to_rgb(color2)

    if not isinstance(color1, tuple) or len(color1) != 3:
        raise ValueError("Invalid color1 value. Must be HEX or RGB format.")
    if not isinstance(color2, tuple) or len(color2) != 3:
        raise ValueError("Invalid color2 value. Must be HEX or RGB format.")
    if not 0 <= ratio <= 1:
        raise ValueError("Invalid ratio value. Must be between 0.0 and 1.0.")

    blended_color = tuple(int(color1[i] * (1 - ratio) + color2[i] * ratio) for i in range(3))
    return rgb_to_hex(blended_color)


# Function to generate colors using ratios
def generate_colors(ratio):
    # Create SVG file
    svg_header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
    svg_header += '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="800"'

    svg_content = ''

    # Generate all combinations of sets
    combinations_list = list(combinations(range(1, 8), 1)) + list(combinations(range(1, 8), 2)) + \
                        list(combinations(range(1, 8), 3)) + list(combinations(range(1, 8), 4)) + \
                        list(combinations(range(1, 8), 5)) + list(combinations(range(1, 8), 6)) + \
                        list(combinations(range(1, 8), 7))

    # Calculate blended color for each section and generate SVG content
    rectangle_width = 100
    rectangle_height = 100
    rectangle_spacing = 20  # Set the spacing between rectangles

    # Initialize variables for tracking occupied positions
    occupied_positions = set()
    max_y = 0

    for idx, combination in enumerate(combinations_list):
        binary_combination = [1 if i + 1 in combination else 0 for i in range(7)]
        num_colors = sum(binary_combination)

        # Blend colors using the specified starting colors
        blended_color = '#FFFFFF'  # Default color is white

        for i in range(7):
            if binary_combination[i]:
                color = colors[f'C{i+1}']
                if blended_color == '#FFFFFF':
                    blended_color = color
                else:
                    blended_color = blend_colors(blended_color, color, ratio)

        # Find the first available position that does not overlap with existing rectangles
        x_pos = 0
        y_pos = 0
        while (x_pos, y_pos) in occupied_positions:
            x_pos += rectangle_width + rectangle_spacing
            if x_pos + rectangle_width > 800:
                x_pos = 0
                y_pos += rectangle_height + rectangle_spacing

        # Update the maximum y-coordinate
        max_y = max(max_y, y_pos + rectangle_height)

        # Mark the current position as occupied
        for i in range(rectangle_width):
            for j in range(rectangle_height):
                occupied_positions.add((x_pos + i, y_pos + j))

        # Generate SVG rectangle for the color combination
        svg_content += f'<rect x="{x_pos}" y="{y_pos}" width="{rectangle_width}" height="{rectangle_height}" fill="{blended_color}" />\n'

        # Generate SVG text for the combination label
        label_x = x_pos + rectangle_width // 2
        label_y = y_pos + rectangle_height // 2
        svg_content += f'<text x="{label_x}" y="{label_y}" text-anchor="middle" dominant-baseline="middle" fill="black" font-size="12">{combination}</text>\n'

    # Update the SVG height
    svg_header += f' height="{max_y + rectangle_height + 50}"'  # Add extra padding of 50 units
    svg_header += '>\n'
    svg_footer = '</svg>'

    # Write SVG file
    svg_file_path = 'blended_colors2.svg'  # Path to the output SVG file
    with open(svg_file_path, 'w') as svg_file:
        svg_file.write(svg_header + svg_content + svg_footer)

    print(f"SVG file '{svg_file_path}' generated successfully.")


# Hex color values for each set
colors = {
    'C1': '#FF0000',
    'C2': '#FF9500',
    'C3': '#FFD60A',
    'C4': '#39E555',
    'C5': '#00B0FF',
    'C6': '#8000FF',
    'C7': '#FF2EBF'
}

# Generate colors using ratios
ratio = float(input("Enter the blending ratio (between 0.0 and 1.0): "))
generate_colors(ratio)

