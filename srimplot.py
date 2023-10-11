import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import scienceplots

darkgrey = "#000000"
plt.style.use("science")

#############################################################

beam = ["94Ag", "80Zr", "213Rn", "226Th"]
energy_MeV = ""
thickness_um = ["5h", "4", "21", "13", "17h", "13", "21", "15"]
material = ["Ti", "Mylar"]
gas = ["He", "Ar"]
flag250 = False
textflag = False

#############################################################
fig, ax = plt.subplots(4, 2, figsize=(7, 12), sharex=True, gridspec_kw={"hspace": 0})


for i in range(8):
    print(i, int(i / 2), i % 2)
    material = "Ti" if i < 2 else "Mylar"
    g = gas[i % 2]
    A = beam[int(i / 2)][:-2]
    nuc = beam[int(i / 2)][-2:]
    file = beam[int(i / 2)] + "_" + thickness_um[i] + "um" + material + "_" + g
    filename = file + "/" + file

    if flag250:
        depth, counts250, _ = np.genfromtxt(filename + "250mbar.txt", unpack=True)
        total250 = sum(counts250)
    depth, counts500, _ = np.genfromtxt(filename + "500mbar.txt", unpack=True)
    total500 = sum(counts500)
    depth, counts750, _ = np.genfromtxt(filename + "750mbar.txt", unpack=True)
    total750 = sum(counts750)
    depth, counts1000, _ = np.genfromtxt(filename + "1000mbar.txt", unpack=True)
    total1000 = sum(counts1000)
    depth = depth / 1e7

    ax[int(i / 2)][i % 2].hist(
        depth,
        bins=len(counts1000),
        weights=counts1000,
        histtype="step",
        fill=True,
        color="black",
        linestyle="-",
        linewidth=0.5,
        edgecolor="black",
        align="left",
        label="1000 mbar",
    )

    ax[int(i / 2)][i % 2].hist(
        depth,
        bins=len(counts750),
        weights=counts750,
        histtype="step",
        fill=True,
        color="dimgrey",
        alpha=0.9,
        linestyle="-",
        linewidth=0.5,
        edgecolor="black",
        align="left",
        label="750 mbar",
    )

    ax[int(i / 2)][i % 2].hist(
        depth,
        bins=len(counts500),
        weights=counts500,
        histtype="step",
        fill=True,
        color="DarkGrey",
        alpha=0.9,
        linestyle="-",
        linewidth=0.5,
        edgecolor="black",
        align="left",
        label="500 mbar",
    )

    if flag250:
        ax[int(i / 2)][i % 2].hist(
            depth,
            bins=len(counts250),
            weights=counts250,
            histtype="step",
            fill=True,
            color="silver",
            alpha=0.9,
            linestyle="-",
            linewidth=0.5,
            edgecolor="black",
            align="left",
            label="250 mbar",
        )

    # ax[int(i/4)][i%2].ax[int(i/4)][i%2]vline(depth[1], color=darkgrey, linestyle="--")
    # ax[int(i/4)][i%2].text(
    #    depth[1] + 0.25,
    #    0.75 * counts1000.max(),
    #    "Window",
    #    rotation="vertical",
    #    color=darkgrey,
    # )
    maximum = max(counts500.max(), counts750.max(), counts1000.max())

    ax[int(i / 2)][i % 2].set_xlim(0, 30)
    ax[int(i / 2)][i % 2].set_ylim(0, 1.1 * maximum)
    if i == 1:
        handles, labels = ax[int(i / 2)][i % 2].get_legend_handles_labels()
        ax[int(i / 2)][i % 2].legend(reversed(handles), reversed(labels))
    if i < 2:
        ax[int(i / 2)][i % 2].xaxis.set_label_coords(0.5, 1.08, transform=None)
        ax[int(i / 2)][i % 2].set_xlabel(g)
    if i > 5:
        ax[int(i / 2)][i % 2].set_xlabel("Depth [mm]")
    if i % 2 == 0:
        ax[int(i / 2)][i % 2].yaxis.set_label_coords(-0.175, 0.5, transform=None)
        ax[int(i / 2)][i % 2].set_ylabel("$^{" + A + "}$" + nuc, rotation=0)

    ax[int(i / 2)][i % 2].text(
        2,
        1.025 * maximum,
        material + ", " + thickness_um[i].replace("h", ".5") + "\,\\textmu m",
    )

    if textflag:
        ax[i].text(
            2,
            1.2 * maximum,
            "$^{" + A + "}$" + nuc + " @ " + energy_MeV + "$\,$MeV",
            size="smaller",
        )

        if "h" in thickness_um:
            thickness_um = thickness_um.replace("h", ".5")

        ax[i].text(
            2,
            1.1 * maximum,
            thickness_um + "$\,\mu$m " + material + " window, " + gas + " gas",
            size="smaller",
        )

    fig.supylabel("Recoil Linear Density [cm$^{-1}$]")

plt.savefig("multi.pdf", bbox_inches="tight", transparent="True")
