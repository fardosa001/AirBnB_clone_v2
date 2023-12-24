#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static.

config="location /hbnb_static {\n\talias /data/web_static/current/;\n\tindex index.html;\n}\n"

# check if nginx is installed.
if ! command -v nginx &> /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared/"

content="Website Under Construction, Coming Soon!"
timeStamp=$(date +"%Y-%m-%d %H:%M:%S")
HTML="<html>
  <head></head>
  <body>$content</body>
  <p>Created on: $timeStamp</p>
</html>"

echo "$HTML" | sudo tee /data/web_static/releases/test/index.html > /dev/null
rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "55i $config" /etc/nginx/sites-available/default
sudo service nginx restart
