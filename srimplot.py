import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import scienceplots

darkgrey = "#000000"
plt.style.use("science")

filename = "213Rn_5umNi/213Rn_5umNi"
depth, counts500, _ = np.genfromtxt(filename + "_Ar500mbar.txt", unpack=True)
depth, counts750, _ = np.genfromtxt(filename + "_Ar750mbar.txt", unpack=True)
depth, counts1000, _ = np.genfromtxt(filename + "_Ar1000mbar.txt", unpack=True)
depth = depth / 1e7

fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(
    depth,
    bins=len(counts1000),
    weights=counts1000,
    histtype="step",
    color="black",
    linestyle=":",
    align="left",
    label="1000 mbar",
)
ax.hist(
    depth,
    bins=len(counts750),
    weights=counts750,
    histtype="step",
    color="dimgrey",
    alpha=0.9,
    linestyle="--",
    align="left",
    label="750 mbar",
)
ax.hist(
    depth,
    bins=len(counts500),
    weights=counts500,
    histtype="step",
    color="DarkGrey",
    alpha=0.9,
    align="left",
    label="500 mbar",
)
# ax.axvline(depth[1], color=darkgrey, linestyle="--")
# ax.text(
#    depth[1] + 0.25,
#    0.75 * counts1000.max(),
#    "Window",
#    rotation="vertical",
#    color=darkgrey,
# )
maximum = max(counts500.max(), counts750.max(), counts1000.max())

ax.set_xlim(0, 30)
ax.set_ylim(0, 1.35 * maximum)
ax.set_xlabel("Depth (mm)")
ax.set_ylabel("Linear density (cm$^{-1}$)")

handles, labels = ax.get_legend_handles_labels()
ax.legend(reversed(handles), reversed(labels), fontsize="small")
ax.text(2, 1.2 * maximum, "$^{213}$Rn @ 131$\,$MeV", size="smaller")
ax.text(2, 1.1 * maximum, "5$\,\mu$m Ni window", size="smaller")
# ax.text(5, 0.65 * counts.max(), "Ar @ 750$\,$mbar")

# ax.savefig(filename.strip(".txt") + ".pdf", bbox_inches="tight", transparent="True")

plt.savefig(filename + ".pdf", bbox_inches="tight", transparent="True")
