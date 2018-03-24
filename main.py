import PixelClass
import WebAccess
import sys
import time
from random import *

pixels = []

for z in range(0, 1000):
  for x in range(0, 8):
    rand1 = randint(0, 255)
    rand2 = randint(0, 255)
    rand3 = randint(0, 255)
    for y in range(7, -1, -1):
      #pixel = PixelClass.Pixel(x, y, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
      pixel = PixelClass.Pixel(x, y, rand1, rand2, rand3)

      pixels.append(pixel)

  WebAccess.PostSetPixels(pixels)
  #time.sleep(2)
#WebAccess.PostMessage(str(sys.argv[1]))
