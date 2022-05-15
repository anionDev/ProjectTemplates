import os
import argparse
import os
import shutil
from ScriptCollection.GeneralUtilities import GeneralUtilities

def update_design_definition(folder:str, designname:str):
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    design_templates_folder=GeneralUtilities.resolve_relative_path("../Templates/Conventions/Designs",folder_of_current_file)
    gitversion_file=os.path.join(design_templates_folder,designname+".md")
    shutil.copy(gitversion_file,folder)

def update_design_definition_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--designname', default=None, required=True)
    parser.add_argument('-f', '--folder', default=None, required=True)
    args = parser.parse_args()
    folder=args.folder
    designname=args.designname
    update_design_definition(folder,designname)

if __name__=="__main__":
    update_design_definition_cli()
