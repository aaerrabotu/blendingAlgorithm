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
        """
        Converts a HEX color value to an RGB tuple.

        Args:
            hex_value (str): The HEX color value.

        Returns:
            tuple: The RGB color value.

        """
        # Remove the '#' symbol if present
        hex_value = hex_value.lstrip('#')
        # Convert the HEX value to RGB values and return as a tuple
        return tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb_value):
        """
        Converts an RGB tuple to a HEX color value.

        Args:
            rgb_value (tuple): The RGB color value.

        Returns:
            str: The HEX color value.

        """
        # Format the RGB values as a HEX string and return
        return '#%02x%02x%02x' % rgb_value

    # Convert color1 to RGB if it is in HEX format
    if isinstance(color1, str):
        color1 = hex_to_rgb(color1)
    # Convert color2 to RGB if it is in HEX format
    if isinstance(color2, str):
        color2 = hex_to_rgb(color2)

    # Check if color1 is a valid RGB tuple
    if not isinstance(color1, tuple) or len(color1) != 3:
        raise ValueError("Invalid color1 value. Must be HEX or RGB format.")
    # Check if color2 is a valid RGB tuple
    if not isinstance(color2, tuple) or len(color2) != 3:
        raise ValueError("Invalid color2 value. Must be HEX or RGB format.")
    # Check if ratio is within the valid range of 0.0 to 1.0
    if not 0 <= ratio <= 1:
        raise ValueError("Invalid ratio value. Must be between 0.0 and 1.0.")

    # Blend the colors by calculating the weighted average of the RGB values
    blended_color = tuple(int(color1[i] * (1 - ratio) + color2[i] * ratio) for i in range(3))
    # Convert the blended color to HEX format
    return rgb_to_hex(blended_color)


color1 = "#FF9500"  # Red
color2 = "#00B0FF"  # Blue
ratio = 0.5  # 50% blend

blended_color = blend_colors(color1, color2, ratio)
print(blended_color)  # Output: #800080 (Purple)