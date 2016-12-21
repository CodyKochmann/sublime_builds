# @Author: cody
# @Date:   2016-09-14 17:55:07
# @Last Modified 2016-09-14
# @Last Modified time: 2016-09-14 18:37:38

# since netbeens needs a package name on the top of java files
# to indicate that it is using the folder it is put in, this 
# workaround will do what you need in order to test netbeens built
# java files

# usage example: java-build-run-netbeens-bullshit.sh JavaFile.java

print "this build system is not done yet"
exit()

import time
import os
from sys import argv 

timestamp = lambda: int(time.time())

tmp_dir=timestamp()
tmp_dir="/tmp/{}".format(tmp_dir)

os.mkdir(tmp_dir)
os.system("ln -s ./* {}/".format(tmp_dir))
os.chdir(tmp_dir)

print os.listdir("./")



filename=argv[-1].split('/')[-1]
classname=filename.split('.')[0]
os.mkdir(classname.lower())
bash("echo 'compiling: {}' && javac {}".format(filename,filename))
bash("echo 'running: {}' && echo '--------------------------------' && java {} && echo '--------------------------------'".format(classname,classname))

exit()
"""

javac reader/Reader.java 
java -classpath . reader.Reader

"""