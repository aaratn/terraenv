from requests_html import HTMLSession
from distutils.version import StrictVersion
import json
from config import DOWNLOAD_PATH
import os

def list_local(args):
    program = args.program
    dest_path = DOWNLOAD_PATH
    
    """ lists installed terraform/terragrunt versions """
    
    for f_name in os.listdir(DOWNLOAD_PATH):
        if f_name.startswith(program):
            print (f_name.split('_')[1])

def list_remote(args):
    program = args.program
    
    """ lists terraform/terragrunt versions """
    
    if program == "terraform":
        session = HTMLSession()
        terraform_url = session.get(
            "https://releases.hashicorp.com/terraform/")
        unstable_releases = '-'
        data = terraform_url.html.links
        data = filter(lambda x: program in x, data)
        data = filter(lambda x: unstable_releases not in x, data)
        available_versions = ['']
        
        for d in data:
            version = d.split('/')[2]
            available_versions.append(version)
        available_versions.remove('')
        available_versions.sort(key=StrictVersion)
        
        for version in available_versions:
            print(version)

    elif program == "terragrunt":
        session = HTMLSession()
        terragrunt_url = session.get(
            "https://api.github.com/repos/gruntwork-io/terragrunt/tags?per_page=1000")
        data = terragrunt_url.html.full_text
        parsed_json = (json.loads(data))
        available_versions = ['']
        
        for version in parsed_json:
            available_versions.append(version['name'].lstrip('v'))
        available_versions.remove('')
        available_versions.sort(key=StrictVersion)
        
        for version in available_versions:
            print(version)

    else:
        raise Exception(
            'Invalid Arguement !! It should be either terraform / terragrunt')