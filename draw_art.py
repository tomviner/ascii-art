import board

characters = list(" .-o*=/\|%#@&")

def map_brightness_to_char(brightness):
    n_slots = len(characters)
    slot_width = 1.0/n_slots
    if brightness == 1.0:
        slot = n_slots - 1
    else:
        slot = int(brightness/slot_width)
    return characters[slot]

def put_pixel_on_grid(grid, coord, brightness):
    character = map_brightness_to_char(brightness)
    grid[coord] = character

if __name__ == '__main__':
    grid = board.Board((8, 8))
    art = """\
   ##
  #--#
 #----#
  #--#
   ##
"""

    for y, line in enumerate(art.splitlines()):
        for x, char in enumerate(line):
            if char == " ":
                brightness = 0
            elif char == "#":
                brightness = 0.8
            elif char == "-":
                brightness= 0.4

            put_pixel_on_grid(grid, (x,y), brightness)

    grid.draw(use_borders=False)
