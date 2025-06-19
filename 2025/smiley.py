def display_pixel_art(binary_grid):
    for row in binary_grid:
        print(''.join('🟡' if bit == '1' else '⬛' for bit in row))

# 5x5 smiley face
smiley = [
    '01010',  # eyes
    '00000',  # empty space
    '10001',  # mouth sides
    '01110'   # mouth bottom
]

display_pixel_art(smiley)