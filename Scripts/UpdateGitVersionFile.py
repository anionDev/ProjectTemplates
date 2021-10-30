import os
import argparse
import os
import shutil
from ScriptCollection.core import resolve_relative_path, ScriptCollection, write_message_to_stdout

def update_gitVersion_file():
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    templates_folder=resolve_relative_path("../Templates",folder_of_current_file)
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    folder=args.folder
    gitversion_file=os.path.join(templates_folder,"GitVersion.yml")
    shutil.copy(gitversion_file,folder)

update_gitVersion_file()
