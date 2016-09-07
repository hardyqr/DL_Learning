
#virtualenv
sudo pip install virtualenv
sudo pip install virtualenvwrapper

##activate some commands in virtualenvwrapper
export VIRTUAL_ENV_DISABLE_PROMPT=1
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
[ -f "/usr/local/bin/virtualenvwrapper.sh" ] && source "/usr/local/bin/virtualenvwrapper.sh"

#Set a virtualenv for  tensorflow
sudo virtualenv -p /Users/Fangyu/anaconda/bin/python tensorflow
#the path is the python PATH that uses in the environment and the "tensorflow" is the name of it.

#activate it
source tensorflow/bin/activate

#deactivate it
deactivate

#then go on tensorflow official site
