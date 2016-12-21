# @Author: cody
# @Date:   2016-09-14 18:13:43
# @Last Modified by:   cody
# @Last Modified time: 2016-09-14 18:23:06

sublime_path="/home/$USER/sublime-text-3/Packages/User/"

path_has(){
    ls $1 | grep $2 -c 
    if [ $? -eq 0 ]
    then
        # false
        return 1
    else
        # true
        return 0
    fi 
}



sublime-text-3/Packages/User/java-build-run.sublime-build