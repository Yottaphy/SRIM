import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import scienceplots

darkgrey = "#000000"
plt.style.use("science")

#############################################################

beam = "213Rn"
energy_MeV = "131"
thickness_um = "15"
material = "Mylar"
gas = "Ar"

#############################################################
A = beam[:-2]
nuc = beam[-2:]
file = beam + "_" + thickness_um + "um" + material + "_" + gas
filename = file + "/" + file
depth, counts500, _ = np.genfromtxt(filename + "500mbar.txt", unpack=True)
depth, counts750, _ = np.genfromtxt(filename + "750mbar.txt", unpack=True)
depth, counts1000, _ = np.genfromtxt(filename + "1000mbar.txt", unpack=True)
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
ax.text(
    2,
    1.2 * maximum,
    "$^{" + A + "}$" + nuc + " @ " + energy_MeV + "$\,$MeV",
    size="smaller",
)

if "h" in thickness_um:
    thickness_um = thickness_um.replace("h", ".5")

ax.text(
    2,
    1.1 * maximum,
    thickness_um + "$\,\mu$m " + material + " window, " + gas + " gas",
    size="smaller",
)

plt.savefig(filename + ".pdf", bbox_inches="tight", transparent="True")
