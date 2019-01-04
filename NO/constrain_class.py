import os
import shutil as sh
import subprocess as sp
import matplotlib
import matplotlib.pyplot as plt

class ConstrainInput:
    def __init__(self, exepath, n_alpha, n_beta, csl_lambda, targets, basisset):
        self.n_alpha = str(n_alpha)
        self.n_beta = str(n_beta)
        self.csl_lambda = str(csl_lambda)
        self.targets = str(targets)
        self.basisset = str(basisset)
        self.exepath = str(exepath)

    def sets(self, sourcepath, xyzlist, xyznamelist):
        self.sourcepath = sourcepath
        self.xyzlist = xyzlist
        self.xyznamelist = xyznamelist

    def move(self, number = ""):

        destout = self.sourcepath + "out" + str(number) + "/"
        destlog = self.sourcepath + "log" + str(number) + "/"

        if (os.path.exists(destout)):
            sh.rmtree(destout)
        if (os.path.exists(destlog)):
            sh.rmtree(destlog)
        os.makedirs(destout)
        os.makedirs(destlog)

        source = os.listdir(self.sourcepath)
        for files in source:
            if files.endswith('.output'):
                sh.move(os.path.join(self.sourcepath, files), os.path.join(destout, files))
            if files.endswith('.log'):
                sh.move(os.path.join(self.sourcepath, files), os.path.join(destlog, files))

    def run(self):
        for x in self.xyznamelist:
            args = (
                self.exepath, "-f",
                str(x),
                "-a", self.n_alpha, "-b", self.n_beta, "-c", self.csl_lambda, "-q",  self.targets, "-s", self.basisset)
            sp.run(args)

    def readout(self,file):
        e = list()
        l = list()
        p = list()
        f = open(file, "r")
        for line in f:
            x = line.split("\t")
            e.append(float(x[0]))
            l.append(float(x[1]))
            p.append(float(x[2]))
        return (e, l, p)

    def graph(self, number=""):
        outpat = self.sourcepath + "out" + str(number) + "/"
        source = os.listdir(outpat)
        q = list()
        yy = list()
        for files in source:
            if files.endswith(".output"):
                q.append(self.readout(os.path.join(outpat, files)))
                yy.append(files)

        figLE, axLE = plt.subplots()
        figLP, axLP = plt.subplots()
        figPE, axPE = plt.subplots()

        lm = "Lagrange Multiplier"
        en = "Energy (hartree)"
        po = "Population (a.u.)"

        axLE.set(xlabel=lm, ylabel=en)
        axLP.set(xlabel=lm, ylabel=po)
        axPE.set(xlabel=po, ylabel=en)

        counter = 0
        for p in q:
            labelv = str(yy[counter])
            axLE.plot(p[1],p[0],label = labelv)
            axLP.plot(p[1],p[2],label = labelv)
            axPE.plot(p[2],p[0],label = labelv)
            counter += 1

        axLE.grid()
        axLP.grid()
        axPE.grid()

        #figLE.legend()
        #figLP.legend()
        #figPE.legend()

        figLE.savefig("LE" + str(number) + ".pdf", bbox_inches='tight')
        figLP.savefig("LP" + str(number) + ".pdf", bbox_inches='tight')
        figPE.savefig("PE" + str(number) + ".pdf", bbox_inches='tight')








