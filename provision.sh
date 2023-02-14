# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       provision.sh to set up virtual machine env
#
# =================================================================================================
#    Date      Name                    Description of Change
# 14-Feb-2023  Wayne Shih              Initial create
# 14-Feb-2023  Wayne Shih              Create superuser
# $HISTORY$
# =================================================================================================

#!/usr/bin/env bash

echo 'Start!'

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

sudo apt-get update
sudo apt-get install tree

cd /vagrant


# install mysql8
if ! [ -e /vagrant/mysql-apt-config_0.8.15-1_all.deb ]; then
	wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb
fi

sudo dpkg -i mysql-apt-config_0.8.15-1_all.deb
sudo DEBIAN_FRONTEND=noninteractivate apt-get install -y mysql-server
sudo apt-get install -y libmysqlclient-dev


if [ ! -f "/usr/bin/pip" ]; then
  sudo apt-get install -y python3-pip
  sudo apt-get install -y python-setuptools
  sudo ln -s /usr/bin/pip3 /usr/bin/pip
else
  echo "pip3 installed"
fi

pip install --upgrade setuptools      
pip install --ignore-installed wrapt  
pip install -U pip                    
pip install -r requirements.txt       


# Set mysql root with password 'yourpassword' 
# Create user_service database
sudo mysql -u root << EOF
	ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
	flush privileges;
	show databases;
	CREATE DATABASE IF NOT EXISTS user_service;
EOF


# Set superuser for django backend management
# superuser name
USER="admin"
# superuser password
PASS="admin"
# superuser email
MAIL="admin@twitter.com"
script="
from django.contrib.auth.models import User;
username = '$USER';
password = '$PASS';
email = '$MAIL';
if not User.objects.filter(username=username).exists():
	User.objects.create_superuser(username, email, password);
	print( 'Superuser created.' );
else:
	print( 'Superuser creation skipped.' );
"
printf " $script"  | python manage.py shell


echo 'All Done!'
