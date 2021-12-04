import numpy as np

data = np.genfromtxt('./2021/data/data03', dtype=int, delimiter=1)

# First answer
(height, width) = data.shape
gamma_rate = epsilon_rate = ''

for x in range(width):
  moreOnes = np.count_nonzero(data[:, x]) >= height/2
  if (moreOnes):
    gamma_rate += '1'
    epsilon_rate += '0'
  else:
    gamma_rate += '0'
    epsilon_rate += '1'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Second answer
ogr = co2sr = np.copy(data)
for x in range(width):
  if (len(ogr) > 1):
    moreOnes = np.count_nonzero(ogr[:, x]) >= len(ogr)/2
    ogr = np.array([a for a in ogr if a[x] == moreOnes])

  if (len(co2sr) > 1):
    lessOnes = np.count_nonzero(co2sr[:, x]) < len(co2sr)/2
    co2sr = np.array([a for a in co2sr if a[x] == lessOnes])

ogr = np.array2string(ogr[0], separator='')[1:-1]
co2sr = np.array2string(co2sr[0], separator='')[1:-1]

print(int(ogr, 2) * int(co2sr, 2))


