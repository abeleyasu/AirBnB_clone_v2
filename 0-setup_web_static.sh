#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data folder to www-data user and group recursively
sudo chown -R www-data:www-data /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
sudo sed -i '/^server {/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$nginx_config"

# Output the modified Nginx configuration
echo "Modified Nginx configuration:"
cat "$nginx_config"

exit 0
