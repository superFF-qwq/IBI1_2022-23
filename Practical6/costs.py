costs=[1,8,15,7,5,14,43,40]
costs.sort() #costs=sorted(costs)
print(costs)

import numpy as np
import matplotlib.pyplot as plt
plt.boxplot(costs,
	widths = 0.6,
	vert = True,
	whis = 1.5,
	patch_artist = True,
	meanline = False,
	showbox = True,
	showcaps = True,
	showfliers = True,
	notch = True
	)
plt.show()