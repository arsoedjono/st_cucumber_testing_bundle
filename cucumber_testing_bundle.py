import sublime
import sublime_plugin


class RunCucumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    panel = self.view.window().get_output_panel("ctb")
    panel.insert(edit, 0, "running RunCucumberCommand")
    self.view.window().run_command("show_panel", {"panel": "output.ctb"})
