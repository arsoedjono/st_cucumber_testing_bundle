import os
import sys
import sublime
import sublime_plugin

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CODE_DIRS = ["libs"]
sys.path += [BASE_PATH] + [os.path.join(BASE_PATH, f) for f in CODE_DIRS]

from libs.panels import Panel

class RunCucumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    panel = Panel(self.view.window(), edit, sublime.load_settings("Preferences.sublime-settings").get("panel_settings"))
    panel.write("running RunCucumberCommand")
    panel.display_panel()
