import os
import sys
import sublime
import sublime_plugin

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CODE_DIRS = ["libs"]
sys.path += [BASE_PATH] + [os.path.join(BASE_PATH, f) for f in CODE_DIRS]

from libs.job import Job
from libs.executor import Executor

# view.run_command("run_cucumber")
class RunCucumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(): Executor(job).run_cucumber()

# view.run_command("run_current_file")
class RunCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(self.view.file_name()): Executor(job).run_current_file()
