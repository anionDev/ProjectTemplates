import os
import argparse
from ScriptCollection.core import resolve_relative_path, ScriptCollection, write_message_to_stdout, ensure_directory_does_not_exist,ensure_directory_exists
from distutils.dir_util import copy_tree

def update_gitLab_templates():
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    templates_folder=resolve_relative_path("../Templates/.gitlab",folder_of_current_file)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    target_folder=os.path.join(args.folder,".gitlab")
    ensure_directory_does_not_exist(target_folder)
    ensure_directory_exists(target_folder)
    copy_tree(templates_folder, target_folder)

update_gitLab_templates()
