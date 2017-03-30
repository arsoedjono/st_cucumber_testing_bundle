from libs.command import Command

class Executor(object):
  def __init__(self, job):
    self.job = job

  def _execute(self, command):
    print("Running command: {0}".format(command))
    self.job.window.run_command("exec", {
      "shell_cmd": command,
      "working_dir": self.job.root(),
    })

  def _line_number(self):
    return (str)(self.job.view.rowcol(self.job.view.sel()[0].begin())[0] + 1)

  def _prepare(self, file_name = None, line = None):
    cmd_obj = Command(self.job)
    command = cmd_obj.retrieve(file_name, line)

    cmd_obj.save(command)
    self._execute(command)

  def run_cucumber(self):
    self._prepare()

  def run_current_file(self):
    self._prepare(self.job.view.file_name())

  def run_current_line(self):
    self._prepare(self.job.view.file_name(), self._line_number())

  def run_last(self):
    self._execute(Command(self.job).last_command())
