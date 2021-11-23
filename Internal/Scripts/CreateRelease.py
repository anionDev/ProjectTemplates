import os
from ScriptCollection.core import resolve_relative_path, ScriptCollection

class release_creator:

    sc= ScriptCollection()
    folder_of_current_file=os.path.dirname(os.path.realpath(__file__))
    repository_folder=resolve_relative_path("../..",folder_of_current_file)

    def create_release(self):
        self.sc.start_program_synchronously("python",f"UpdateCommonFiles.py",self.folder_of_current_file,verbosity=2,throw_exception_if_exitcode_is_not_zero=True,prevent_using_epew=True)
        self.sc.git_commit(self.repository_folder,"Updated common files")
        self.sc.start_program_synchronously("SCCreateSimpleMergeWithoutRelease",f"{self.repository_folder} stable main projects.aniondev",self.repository_folder,verbosity=2,throw_exception_if_exitcode_is_not_zero=True,prevent_using_epew=True)

release_creator().create_release()
