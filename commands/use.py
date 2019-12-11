from dotenv import load_dotenv
import os.path
import os
import sys
from config import DOWNLOAD_PATH, VERSION_FILE
from .list import list_local

def use(args):

    program = args.program
    version = args.version

    if os.path.exists(VERSION_FILE) and not args.version:
        load_dotenv(dotenv_path=VERSION_FILE)
        version = (os.getenv(program.upper()))

    if not version:
        print("Please define version or add that to .terraenv file.\
            \nYou don't need to mention version if you have .terraenv file at current path. \
            \nFor more informaion, Please refer terraenv document https://github.com/aaratn/terraenv#terraenv-file.\n")
        sys.exit(1)

    available_versions = list_local(args)
    if version not in available_versions:
        print(program + " version '" + version + "' is not installed.\
            \nYou can check installed versions by running 'terraenv terraform/terragrunt list local'.\
            \nFor more informaion, Please refer terraenv document https://github.com/aaratn/terraenv#terraenv-terraformterragrunt-list-local.\n")
        sys.exit(1)

    dest_path = DOWNLOAD_PATH + program + "_" + version
    try:
        os.remove("/usr/local/bin/" + program )
    except FileNotFoundError:
        pass
    os.symlink(dest_path, "/usr/local/bin/" + program )
    print(program + " version is set to " + version)
