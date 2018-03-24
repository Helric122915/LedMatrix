import PixelClass
import WebAccess
import sys
import time
from random import *

for loopCount in range(0, 4):
  r = int(sys.argv[1])
  g = int(sys.argv[2])
  b = int(sys.argv[3])

  for y in range(loopCount, 8 - loopCount):
    pixel = PixelClass.Pixel(loopCount, y, r, g, b)

    WebAccess.PostSetPixel(pixel)

  for x in range(loopCount, 8 - loopCount):
    pixel = PixelClass.Pixel(x, 7 - loopCount, r, g, b)

    WebAccess.PostSetPixel(pixel)

  for y in range(7 - loopCount, -1 + loopCount, -1):
    pixel = PixelClass.Pixel(7 - loopCount, y, r, g, b)

    WebAccess.PostSetPixel(pixel)

  for x in range(7 - loopCount, 0 + loopCount, -1):
    pixel = PixelClass.Pixel(x, loopCount, r, g, b)

    WebAccess.PostSetPixel(pixel)
