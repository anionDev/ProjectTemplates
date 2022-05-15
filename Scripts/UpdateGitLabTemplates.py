import os
import argparse
from distutils.dir_util import copy_tree
from ScriptCollection.GeneralUtilities import GeneralUtilities

def update_gitLab_templates(target_folder:str):
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    templates_folder=GeneralUtilities.resolve_relative_path("../Templates/.gitlab",folder_of_current_file)
    GeneralUtilities.ensure_directory_does_not_exist(target_folder)
    GeneralUtilities.ensure_directory_exists(target_folder)
    copy_tree(templates_folder, target_folder)

def update_gitLab_templates_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    target_folder=os.path.join(args.folder,".gitlab")
    update_gitLab_templates(target_folder)

if __name__=="__main__":
    update_gitLab_templates_cli()
