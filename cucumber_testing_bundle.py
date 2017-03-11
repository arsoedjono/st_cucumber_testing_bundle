import sublime
import sublime_plugin


class RunCucumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    panel = self.view.window().get_output_panel("ctb")
    settings = sublime.load_settings("Preferences.sublime-settings").get("panel_settings")

    for key, value in settings.items():
      panel.settings().set(key, value)
    panel.insert(edit, 0, "running RunCucumberCommand")

    self.view.window().run_command("show_panel", {"panel": "output.ctb"})
