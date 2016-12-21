
from os import system as bash
from sys import argv 
from time import sleep

filename=argv[-1].split('/')[-1]

bash("echo 'compiling: {}' && javac {}".format(filename,filename,filename))

classname=filename.split('.')[0]
bash("echo 'running: {}' && echo '--------------------------------' && java {} && echo '--------------------------------'".format(classname,classname))

