d=[
[1467,	21,	19600,	17]
,[1539	,22,	23135,	17]
,[1570,	20,	14233,	17]
,[1468,	21,	15807,	17]
,[1890,	23,	15132,	17]
,[1344,	20,	16297,	18]
,[1351,	21,	23808,	18]
,[1437,	21,	23988,	17]
,[1735,	22,	14928,	18]
,[1517,	21,	17211,	18]
,[1467,	21,	19600,	17]
]

def envy(one,two):
  yes=False
  for x,y in zip(one,two):
    if x > y:  yes=True
    if x < y: return False
  return yes
 
out = [[' '] * len(d)] * len(d)
for n1,one in enumerate(d):
  for n2,two in enumerate(d):
    if envy(one,two):
      print "\n",n1,one,"envies\n",n2,two

  





