import os
import argparse
import os
import shutil
from ScriptCollection.core import resolve_relative_path, ScriptCollection, write_message_to_stdout

def update_desifn_definition():
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    design_templates_folder=resolve_relative_path("../Templates/Conventions/Designs",folder_of_current_file)
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--designname', default=None, required=True)
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    folder=args.folder
    designname=args.designname
    gitversion_file=os.path.join(design_templates_folder,designname+".md")
    shutil.copy(gitversion_file,folder)

update_desifn_definition()
