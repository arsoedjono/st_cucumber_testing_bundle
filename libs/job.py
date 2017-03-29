from libs.panel import Panel
from libs.root import Root
from libs.settings import Settings

import sublime

class Job(object):
  NOT_VALID_CUCUMBER_FILE = "Not a valid cucumber file (.feature)"
  NOT_EXECUTABLE = "No such file or directory - features. You can use `cucumber --init` to get started."

  def __init__(self, view, edit):
    self.view = view
    self.window = view.window()
    self.edit = edit
    self.panel = Panel(self.window, self.edit)

  def _file_name(self):
    return self.view.file_name()

  def _is_cucumber_file(self, file_name):
    return file_name.endswith(".feature")

  def _project_name(self):
    return sublime.active_window().folders()[0]

  def is_executable(self, file_name = None):
    flag = self._is_cucumber_file(file_name) if file_name else self.root()

    if not flag:
      msg = "{0} -- {1}".format(self.NOT_VALID_CUCUMBER_FILE, file_name) if file_name else self.NOT_EXECUTABLE
      self.panel.write(msg)
      self.panel.display_panel()

    return flag

  def root(self):
    file_name = self._file_name() or self._project_name()
    return Root(file_name, Settings("cucumber_folder").retrieve()).retrieve()
