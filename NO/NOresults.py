import subprocess as sp
import shutil as sh
import os


exepath = "../../../CLionProjects/forks/gqcp/buildfci/exe/cf"
filestart = "xyz_res/no_"
fileend = "_PB.xyz"
#xyzlist = [2.3, 3.0, 4.0, 5.0, 7.0, 10.0]
xyzlist = [2 + x/10.0 for x in range(80)]
xyznamelist = [filestart + str(x) + fileend for x in xyzlist]

for x in xyznamelist:
    args = (
    exepath, "-f",
      str(x) ,
    "-a", "7", "-b", "7", "-c", "0.1,-1,1.1", "-q", "0,1,2,3,4", "-s", "STO-3G")
    sp.run(args)



sourcepath = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/"
destout = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/out2/"
destlog = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/log2/"

if(os.path.exists(destout)):
    sh.rmtree(destout)
if(os.path.exists(destlog)):
    sh.rmtree(destlog)
os.makedirs(destout)
os.makedirs(destlog)
source = os.listdir(sourcepath)
for files in source:
    if files.endswith('.output'):
        sh.move(os.path.join(sourcepath,files), os.path.join(destout,files))
    if files.endswith('.log'):
        sh.move(os.path.join(sourcepath,files), os.path.join(destlog,files))
