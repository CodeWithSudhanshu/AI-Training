# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = [1,8,10]
# ypoints = [3,10,5]
# plt.figure(figsize=(5,3))
# plt.plot(xpoints,ypoints,marker="*")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = [1,8,10]
# ypoints = [3,10,5]
# plt.figure(figsize=(5,3))
# plt.plot(xpoints,ypoints,marker="s")
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend('fruit')
plt.show()

import seaborn as f
