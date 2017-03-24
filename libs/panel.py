from libs.settings import Settings
import sublime

class Panel(object):
  NAME_PREFIX = "ctb"

  def __init__(self, window, edit):
    self.window = window
    self.edit = edit
    self.panel = self._prepare_panel()

  def _prepare_panel(self):
    panel = self.window.get_output_panel(Panel.NAME_PREFIX)

    for key, value in self._panel_settings().items():
      panel.settings().set(key, value)

    return panel

  def _panel_name(self):
    return "output.{0}".format(Panel.NAME_PREFIX)

  def _panel_settings(self):
    return Settings("panel_settings").retrieve()

  def display_panel(self):
    self.window.run_command("show_panel", {"panel": self._panel_name()})

  def write(self, text):
    self.panel.insert(self.edit, 0, "{0}\n".format(text))
