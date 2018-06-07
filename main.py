import os, sys
import slicing
import draw_art

def main(filepath):
    for coord, brightness in slicing.get_brightness_grid(filepath):
        draw_art.put_pixel_on_grid(coord, brightness)

    draw_art.draw_grid()

if __name__ == '__main__':
    main(*sys.argv[1:])
