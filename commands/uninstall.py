from dotenv import load_dotenv
import os.path
import os
from config import DOWNLOAD_PATH, VERSION_FILE
from .list import list_local
import sys

def uninstall(args):

    program = args.program
    version = args.version

    available_versions = list_local(args)
    if version not in available_versions:
        print(program + " version '" + version + "' is not installed or version argument is blank.\
            \nYou can check installed versions by running 'terraenv terraform/terragrunt list local'.\
            \nFor more informaion, Please refer terraenv document https://github.com/aaratn/terraenv#terraenv-uninstall-terraformterragrunt-version.\n")
        sys.exit(1)

    dest_path = DOWNLOAD_PATH + program + "_" + version
    try:
        active_version = os.readlink("/usr/local/bin/" + program ).split('_')[1]

        if active_version != version:
            os.remove(dest_path)
            print("Uninstalled " + program  + " version " + version)
        else:
            print(version + " is currently in use, please change the version and re-run uninstall command !")
    except Exception as error:
        print(error)
