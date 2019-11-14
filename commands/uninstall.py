from dotenv import load_dotenv
import os.path
import os
from config import DOWNLOAD_PATH, VERSION_FILE

def uninstall(args):
    
    program = args.program
    version = args.version
    
    if os.path.exists(VERSION_FILE) and not args.version:
        load_dotenv(dotenv_path=VERSION_FILE)
        version = (os.getenv(program.upper()))

    dest_path = DOWNLOAD_PATH + program + "_" + version
    
    try:
        active_version = os.readlink("/usr/local/bin/" + program ).split('_')[1]
        
        if active_version != version:
            os.remove(dest_path)
        
        else:
            raise Exception(version + " is currently in use, please change the version and re-run uninstall command !")
    
    except FileNotFoundError:
        pass