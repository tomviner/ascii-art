import os, sys
import board
import slicing
import draw_art

def main(filepath):
    grid = board.Board((64, 64))
    for coord, brightness in slicing.get_brightness_grid(filepath):
        draw_art.put_pixel_on_grid(grid, coord, brightness)

    _, (mx, my) = grid.occupied()
    occupied_grid = grid[:mx + 1, :my + 1]
    #~ grid.paint("grid.png", background_colour="#000", use_borders=False)
    occupied_grid.draw(use_borders=False)

if __name__ == '__main__':
    main(*sys.argv[1:])
