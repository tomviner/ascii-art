import os, sys
import board
import slicing
import draw_art

def main(filepath):
    grid = board.Board((64, 64))
    for coord, brightness in slicing.get_brightness_grid(filepath):
        draw_art.put_pixel_on_grid(grid, coord, brightness)

    grid.paint(use_borders=False)
    #~ grid.draw(use_borders=False)

if __name__ == '__main__':
    main(*sys.argv[1:])
