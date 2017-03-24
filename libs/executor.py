from libs.command import Command

class Executor(object):
  def __init__(self, job):
    self.job = job

  def run_cucumber(self):
    command = "{cucumber_command}".format(
      cucumber_command = Command(self.job).retrieve(),
    )

    self.job.window.run_command("exec", {
      "shell_cmd": command,
      "working_dir": self.job.root(),
    })
