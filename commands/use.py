from dotenv import load_dotenv
import os.path
import os
from config import DOWNLOAD_PATH, VERSION_FILE

def use(args):
    
    program = args.program
    version = args.version
    
    if os.path.exists(VERSION_FILE) and not args.version:
        load_dotenv(dotenv_path=VERSION_FILE)
        version = (os.getenv(program.upper()))

    dest_path = DOWNLOAD_PATH + program + "_" + version
    try:
        os.remove("/usr/local/bin/" + program )
    except FileNotFoundError:
        pass
    os.symlink(dest_path, "/usr/local/bin/" + program )