import PixelClass
import WebAccess
import sys
import time
from random import *

pixels = []

for z in range(0, 1000):
  for x in range(0, 8):
    for y in range(7, -1, -1):
      pixel = PixelClass.Pixel(x, y, randint(0, 255), randint(0, 255), randint(0, 255))

      pixels.append(pixel)

  WebAccess.PostSetPixels(pixels)
