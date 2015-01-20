# Colors

red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)
cyan = (0,255,255)
blue = (0,0,255)
magenta = (255,0,255)

white = (255,255,255)
black = (0,0,0)

maxRGB = 255

def calculateRGB(total,entry):
  # returns RGB tuple from color wheel position

  base = (3 * entry) / total
  remainder = (3 * entry) % total

  r = 0
  g = 0
  b = 0

  if base == 0:
    r = total - remainder
    g = remainder
    b = 0

  elif base == 1:
    r = 0
    g = total - remainder
    b = remainder

  elif base == 2:
    r = remainder
    g = 0
    b = total - remainder

  return (r,g,b)

def expandColor(myColor):

  # get value of greatest r,g,b val
  maxIdx = 0
  if myColor[1] > myColor[0]:
    maxIdx = 1
  if myColor[2] > myColor[maxIdx]:
    maxIdx = 2
  tmpMax = float(myColor[maxIdx])

  ratio = float(0)

  if tmpMax != 0:
    ratio = maxRGB / tmpMax

  r = myColor[0] * ratio
  g = myColor[1] * ratio
  b = myColor[2] * ratio

  return (r,g,b)




















