import subprocess
from .sbieini import SbieIni


type Phase = 1 or 0


class SandboxiePlus:
    def __init__(self,installation_dir: str, default_box_name: str) -> None:
        self.installation_dir = str
        self.sbieini_path = str
        self.start_path = str
        self.default_sndb_options = dict
        self.sbieini = SbieIni(self.installation_dir)
        ...

    def start_execute(self, args: list, **kwargs): ...
    def start(
            self, proc: str, box: str, env: str, silent: bool, elevate: bool, hide_window: bool, wait: bool, **kwargs
    ) -> subprocess.Popen: ...
    def terminate(self, box: str): ...
    def terminate_all(self): ...
    def mount(self, key: str, box: str, protected: bool): ...
    def unmount(self, box: str): ...
    def unmount_all(self): ...
    def list_pids(self): ...
    def delete_content(self, box: None, silent: bool, phase: Phase): ...
    def reload(self): ...
    def disable_force(self, proc_path: str): ...
    def create_default_box(self): ...
    def get_sandboxes(self): ...
    def create_sandbox(self, name: str, options=dict): ...
    def delete_sandbox(self, name: str): ...