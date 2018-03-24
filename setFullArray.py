import PixelClass
import WebAccess
import sys
import time
from random import *

pixels = []

for x in range(0, 8):
  for y in range(7, -1, -1):
    pixel = PixelClass.Pixel(x, y, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    pixels.append(pixel)

WebAccess.PostSetPixels(pixels)
