import requests
import json
import time
import PixelClass

PORTNUM = '80'
ipAddress = '192.168.1.95'
url = 'http://' + ipAddress + ':' + PORTNUM
headers = {'content-type': 'application/json'}

def PostMessage(message):
  data = {}
  data['message'] = message

  try:
    r = requests.post(url + '/set/message', json=data, headers=headers)
    #print r.text
  except:
    print 'Couldn\'t Access WebServer'

def PostSetPixel(pixel):
  pixelData = {}
  pixelData['x'] = pixel.x
  pixelData['y'] = pixel.y
  pixelData['r'] = pixel.r
  pixelData['g'] = pixel.g
  pixelData['b'] = pixel.b

  data = {}
  data['pixel'] = pixelData

  try:
    r = requests.post(url + '/set/pixel', json=data, headers=headers)
    #print r.text
  except:
    print 'Couldn\'t Access WebServer'


def PostSetPixels(pixels):

  data = {}
  pixelsData = []

  for pixel in pixels:
    pixelData = {}

    #print '(' + str(pixel.x) + ',' + str(pixel.y) + ',' + str(pixel.r) + ',' + str(pixel.g) + ',' + str(pixel.b) + ')'
    pixelData['x'] = pixel.x
    pixelData['y'] = pixel.y
    pixelData['r'] = pixel.r
    pixelData['g'] = pixel.g
    pixelData['b'] = pixel.b

    pixelsData.append(pixelData)

  data['pixels'] = pixelsData

  try:
    r = requests.post(url + '/set/pixels', json=data, headers=headers)
    #print r.text
  except:
    print 'Couldn\'t Access WebServer'

