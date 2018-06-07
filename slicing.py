from PIL import Image, ImageStat


def crop(im, width_chars=64):
    imgwidth, imgheight = im.size
    for i in range(width_chars):
        pixels = imgwidth // width_chars
        height_chars = imgheight // pixels
        for j in range(height_chars):
            box = (i * pixels, j * pixels, (i + 1) * pixels, (j + 1) * pixels)
            square = im.crop(box)
            yield (i, j), square


def brightness(im):
    im.convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]


def get_brightness_grid(fn):
    im = Image.open(fn)
    for (i, j), square in crop(im):
        # print(i, j, square)
        bright = brightness(square)
        frac = bright / 255
        yield (i, j), frac


if __name__ == '__main__':
    print(list(get_brightness_grid(fn='football-2518982_1920.jpg')))
