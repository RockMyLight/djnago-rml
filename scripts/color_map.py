# Specs
# 
# Two Functions:
# 1. Phase: phones with projected position > 0.5 have color inverted
# 2. Wave: need to insert more elements and map the same colors to lower values of colour
#
# Assume: list of [ pos, timestamp, color]
#         where pos is GPS position in range [0 or 1] 
#         where color is either 0 or 1. 
# 
# Functions return: list of [timestamp, color hex]

doWaveAtTime = -1 # some big number or -1 to skip
doPhaseAtTime = -1

baseColor = (1.0,1.0,1.0) #white

#tested 
def toHashColor(color):
  triplet = (int(color*255*baseColor[0]), int(color*255*baseColor[1]), int(color*255*baseColor[2]))
  return '#'+''.join(map(chr, triplet)).encode('hex')

# tested
def phase( oldlist ):
  "transforms phase"
  newlist = [0] * len(oldlist)
  for i in range(0, len(oldlist)):
    if oldlist[i][0] > 0.5 :
      newlist[i] = [oldlist[i][1], toHashColor( abs( oldlist[i][2]-1) ) ]
    else:
      newlist[i] = [oldlist[i][1], toHashColor( oldlist[i][2] ) ]
  return newlist