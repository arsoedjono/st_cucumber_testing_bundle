from libs.panel import Panel

class Job(object):
  def __init__(self, view, edit):
    self.view = view
    self.window = view.window()
    self.edit = edit
    self.panel = Panel(self.window, self.edit)

  def run_cucumber(self):
    self.window.run_command("exec", {
      "shell_cmd": "cucumber"
    })
