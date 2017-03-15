from libs.panel import Panel

class Job(object):
  def __init__(self, window, edit):
    self.window = window
    self.edit = edit

  def run(self):
    panel = Panel(self.window, self.edit)
    panel.write("running RunCucumberCommand")
    panel.display_panel()
