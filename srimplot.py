import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import scienceplots

darkgrey = "#000000"

plt.style.use("science")

# filename = "My13um_Ar750mbar_80Zr.txt"
depth, counts500, _ = np.genfromtxt("My13um_Ar500mbar_80Zr.txt", unpack=True)
depth, counts750, _ = np.genfromtxt("My13um_Ar750mbar_80Zr.txt", unpack=True)
depth, counts1000, _ = np.genfromtxt("My13um_Ar1bar_80Zr.txt", unpack=True)
depth = depth / 1e7

plt.hist(
    depth,
    len(counts1000),
    weights=counts1000,
    histtype="stepfilled",
    color="black",
    linestyle=":",
    align="left",
    label="1000 mbar",
)
plt.hist(
    depth,
    len(counts750),
    weights=counts750,
    histtype="stepfilled",
    color="dimgrey",
    alpha=0.9,
    linestyle="--",
    align="left",
    label="750 mbar",
)
plt.hist(
    depth,
    len(counts500),
    weights=counts500,
    histtype="stepfilled",
    color="DarkGrey",
    alpha=0.9,
    align="left",
    label="500 mbar",
)
# plt.axvline(depth[1], color=darkgrey, linestyle="--")
# plt.text(
#    depth[1] + 0.25,
#    0.75 * counts1000.max(),
#    "Window",
#    rotation="vertical",
#    color=darkgrey,
# )
plt.xlim(0, 30)
plt.xlabel("Depth (mm)")
plt.ylabel("Linear density (cm$^{-1}$)")
plt.legend()
# plt.text(4.5, 0.85 * counts.max(), "$^{80}$Zr @ 120$\,$MeV")
# plt.text(20, 0.75 * counts.max(), "13$\,\mu$m Mylar window")
# plt.text(5, 0.65 * counts.max(), "Ar @ 750$\,$mbar")

# plt.savefig(filename.strip(".txt") + ".pdf", bbox_inches="tight", transparent="True")

plt.savefig("80Zr_13umMylar.pdf", bbox_inches="tight", transparent="True")
