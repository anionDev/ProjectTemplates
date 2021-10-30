import os
from ScriptCollection.core import resolve_relative_path, ScriptCollection, write_message_to_stdout

class common_files_updater:

    sc= ScriptCollection()
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    repository_folder=resolve_relative_path("../..",folder_of_current_file)
    templates_scripts_folder=resolve_relative_path("Scripts",repository_folder)
    target_repository=repository_folder

    def execute_program(self,script,argument):
        self.sc.start_program_synchronously("python",f"{script}.py {argument}",self.templates_scripts_folder,verbosity=2,throw_exception_if_exitcode_is_not_zero=True,prevent_using_epew=True)

    def update_common_files(self):
        self.execute_program("UpdateGitLabTemplates", f"--folder {self.target_repository}")
        self.execute_program("UpdateGitVersionFile", f"--folder {self.target_repository}")

common_files_updater().update_common_files()
