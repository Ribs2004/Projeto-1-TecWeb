recipientes = {}
recipientes['recipiente A'] = [62.5, 37.5]
recipientes['recipiente B'] = [40, 60]
recipientes['recipiente C'] = [0, 0]

p = (100/10) * 0.07

recipientes['recipiente C'][0] += recipientes['recipiente A'][0] * p
recipientes['recipiente C'][0] += recipientes['recipiente B'][0] * (1 - p)
recipientes['recipiente C'][1] += recipientes['recipiente A'][1] * p
recipientes['recipiente C'][1] += recipientes['recipiente B'][1] * (1 - p)

print(recipientes['recipiente C'])
print(p)