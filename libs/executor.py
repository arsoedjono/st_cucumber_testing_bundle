from libs.command import Command

class Executor(object):
  def __init__(self, job):
    self.job = job

  def _execute(self, command):
    self.job.window.run_command("exec", {
      "shell_cmd": command,
      "working_dir": self.job.root(),
    })

  def run_cucumber(self):
    self._execute(Command(self.job).retrieve())

  def run_current_file(self):
    self._execute(Command(self.job).retrieve(self.job.view.file_name()))
