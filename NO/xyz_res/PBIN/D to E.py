import subprocess as sp
import shutil as sh
import os

sourcepath = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/PBIN/"
source = os.listdir(sourcepath)
outpath = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/PBIN/PBup"

for files in source:
    if (files.endswith(".one") or files.endswith(".two")):
        f1 = open(os.path.join(sourcepath, files), "r")
        f2 = open(os.path.join(outpath, files), "w")
        for line in f1:
            x = line.replace('D','E')
            f2.write(x)
