import os
import argparse
import os
import shutil
from ScriptCollection.GeneralUtilities import GeneralUtilities

def update_gitVersion_file(folder:str):
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    templates_folder=GeneralUtilities.resolve_relative_path("../Templates",folder_of_current_file)
    gitversion_file=os.path.join(templates_folder,"GitVersion.yml")
    shutil.copy(gitversion_file,folder)

def update_gitVersion_file_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    folder=args.folder
    update_gitVersion_file(folder)

if __name__=="__main__":
    update_gitVersion_file_cli()
