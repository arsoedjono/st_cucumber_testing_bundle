from libs.panel import Panel
from libs.root import Root
from libs.settings import Settings

import sublime

class Job(object):
  def __init__(self, view, edit):
    self.view = view
    self.window = view.window()
    self.edit = edit
    self.panel = Panel(self.window, self.edit)

  def _file_name(self):
    return self.view.file_name()

  def _project_name(self):
    return sublime.active_window().folders()[0]

  def is_executable(self):
    flag = self.root()

    if not flag:
      self.panel.write("No such file or directory - features. You can use `cucumber --init` to get started.")
      self.panel.display_panel()

    return flag

  def root(self):
    file_name = self._file_name() or self._project_name()
    return Root(file_name, Settings("cucumber_folder").retrieve()).retrieve()
