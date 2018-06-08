from glob import glob
from main import main
from PIL import Image
import os


print(glob('pics/*'))
for fn in glob('pics/*'):
    main(fn)
    input('press enter to continue')
    Image.open(fn).show()
    input('press enter to continue')
    os.system('clear') and os.system('cls')
