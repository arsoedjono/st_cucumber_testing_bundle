from libs.command import Command

class Executor(object):
  def __init__(self, job):
    self.job = job

  def _execute(self, command):
    self.job.window.run_command("exec", {
      "shell_cmd": command,
      "working_dir": self.job.root(),
    })

  def _line_number(self):
    return (str)(self.job.view.rowcol(self.job.view.sel()[0].begin())[0] + 1)

  def _prepare_file(self, file_name, line = None):
    self._execute(Command(self.job).retrieve(file_name, line))

  def run_cucumber(self):
    self._execute(Command(self.job).retrieve())

  def run_current_file(self):
    self._prepare_file(self.job.view.file_name())

  def run_current_line(self):
    self._prepare_file(self.job.view.file_name(), self._line_number())
