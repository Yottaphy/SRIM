import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import math
import scienceplots

beam = ["94Ag", "80Zr", "213Rn", "226Th"]
thickness_um = ["5h", "4", "21", "13", "17h", "13", "21", "15"]
material = ["Ti", "Mylar"]
gas = ["He", "Ar"]

for i in range(8):
    material = "Ti" if i < 2 else "Mylar"
    g = gas[i % 2]
    A = beam[int(i / 2)][:-2]
    nuc = beam[int(i / 2)][-2:]
    file = beam[int(i / 2)] + "_" + thickness_um[i] + "um" + material + "_" + g
    filename = file + "/" + file

    _, counts500, _ = np.genfromtxt(filename + "500mbar.txt", unpack=True)
    _, counts750, _ = np.genfromtxt(filename + "750mbar.txt", unpack=True)
    _, counts1000, _ = np.genfromtxt(filename + "1000mbar.txt", unpack=True)

    print(A, nuc, thickness_um[i], material, g)
    print("500", f"{3 * sum(counts500[1:]):.1f}", " %")
    print("750", f"{3 * sum(counts750[1:]):.1f}", " %")
    print("1000", f"{3 * sum(counts1000[1:]):.1f}", " %")
