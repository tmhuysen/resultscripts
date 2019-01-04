import os
import shutil as sh


sourcepath = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/"
destout = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/out3/"
destlog = "/Users/quantum/PycharmProjects/ConstrainedResults/NO/xyz_res/log3/"
source = os.listdir(sourcepath)
for files in source:
    if files.endswith('.output'):
        sh.move(os.path.join(sourcepath,files), os.path.join(destout,files))
    if files.endswith('.log'):
        sh.move(os.path.join(sourcepath,files), os.path.join(destlog,files))
