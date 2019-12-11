import os.path
import os
from dotenv import load_dotenv
import sys
import platform
import requests
from zipfile import ZipFile
from config import DOWNLOAD_PATH, VERSION_FILE
from .list import list_remote

""" Download Required Terraform / Terragrunt Versions """

def download_program(args, program, version):

    operating_sys = sys.platform
    # Upsert download path
    not os.path.exists(DOWNLOAD_PATH) and os.mkdir(DOWNLOAD_PATH)

    available_versions = list_remote(args)
    if version not in available_versions:
        print("Version '" + version + "' is not right available " + program + " version.\
            \nYou can check right available versions by running 'terraenv terraform/terragrunt list remote'.\
            \nFor more informaion, Please refer terraenv document https://github.com/aaratn/terraenv#terraenv-terraformterragrunt-list-remote.\n")
        sys.exit(1)

    if program == "terraform":
        url = "https://releases.hashicorp.com" + "/terraform/" + version + \
            "/terraform_" + version + "_" + operating_sys + "_amd64.zip"

    elif program == "terragrunt":
        url = "https://github.com/gruntwork-io/terragrunt/releases/download/v" + \
            version + "/terragrunt_" + operating_sys + "_amd64"

    if not os.path.exists(DOWNLOAD_PATH + program + "_" + version):

        print("Downloading", program, version, "from", url)

        binary = requests.get(url)

        if binary.status_code == 404:
            raise Exception("Invalid version, got 404 error !")

        dest_path = DOWNLOAD_PATH + program + "_" + version

        open(dest_path, 'wb').write(binary.content)

        if program == "terraform":

            with ZipFile(dest_path, 'r') as zip:
                zip.extract('terraform', path=DOWNLOAD_PATH)

            if os.path.exists(DOWNLOAD_PATH + '/' + program) and os.path.exists(dest_path):
                os.remove(dest_path)
                os.rename(DOWNLOAD_PATH + '/' + program, dest_path)

            else:
                raise Exception("Issue extracting terraform !!")

        os.chmod(dest_path, 0o755)
    else:
        print (program, version, "already downloaded")

""" Installs Required Terraform / Terragrunt Versions """

def install(args):

    program = args.program
    version = args.version

    if not version and os.path.exists(VERSION_FILE):
        load_dotenv(dotenv_path=VERSION_FILE)
        version = (os.getenv(program.upper()))

    if not version:
        print("Please define version or add that to .terraenv file.\
            \nYou don't need to mention version if you have .terraenv file at current path. \
            \nFor more informaion, Please refer terraenv document https://github.com/aaratn/terraenv#terraenv-file.\n")
        sys.exit(1)

    dest_path = DOWNLOAD_PATH + program + "_" + version

    if program == "terraform":
        download_program(args, program, version)

    elif program == "terragrunt":
        download_program(args, program, version)

    else:
        raise Exception(
            'Invalid Arguement !! It should be either terraform / terragrunt')

    if not os.access('/usr/local/bin', os.W_OK):
        print("Error: User doesn't have write permission of /usr/local/bin directory.\
            \n\nRun below command to grant permission and rerun 'terraenv install' command.\
            \nsudo chown -R $(whoami) /usr/local/bin\n")
        sys.exit(1)

    try:
        os.remove("/usr/local/bin/" + program )

    except FileNotFoundError:
        pass

    os.symlink(dest_path, "/usr/local/bin/" + program )
