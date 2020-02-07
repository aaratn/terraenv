import os

DOWNLOAD_PATH = os.environ.get('TERRA_PATH', os.environ.get('HOME') + "/.terraenv") + "/"
VERSION_FILE = ".terraenv"