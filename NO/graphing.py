from NO.constrain_class import ConstrainInput
x="PB"

exepath = "../../../CLionProjects/forks/gqcp/buildfci/exe/cfpat"
filestart = "xyz_res/PBIN/no_"
fileend = "_PB"
xyzlist = [2.3, 3.0, 4.0, 5.0, 7.0, 10.0]
#xyzlist = [2 + x/10.0 for x in range(80)]
xyznamelist = [filestart + str(x) + fileend for x in xyzlist]

print(xyznamelist)
exer = ConstrainInput(exepath,7,7,"0.05,-5,5", "0,1,2,3,4", "STO-3G")
exer.sets("/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/PBIN/", xyzlist, xyznamelist)
exer.run()
exer.move(x)
exer.graph(x)
