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
	showmeans = True,
	meanline = False,
	showbox = True,
	showcaps = True,
	showfliers = True,
	notch = False,
	boxprops={"facecolor": "C0", "edgecolor": "black","linewidth": 0.5, "alpha":0.4}
	)
plt.show()