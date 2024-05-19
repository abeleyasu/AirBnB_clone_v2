from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the current datetime string for the archive name
        now = datetime.now()
        time_format = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + time_format + ".tgz"
        
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")
        
        # Compress the web_static folder into the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))
        
        # Return the archive path
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
