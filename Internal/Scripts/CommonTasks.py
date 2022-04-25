import os
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ...Scripts.UpdateGitVersionFile import update_gitVersion_file

def update_gitversion_file():
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    repository_folder=GeneralUtilities.resolve_relative_path("../..",folder_of_current_file)
    templates_scripts_folder=GeneralUtilities.resolve_relative_path("Scripts",repository_folder)
    update_gitVersion_file(templates_scripts_folder)

def common_tasks():
    update_gitversion_file()

if __name__=="__main__":
    common_tasks()
