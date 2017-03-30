import os
import sys
import sublime
import sublime_plugin

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
CODE_DIRS = ["libs"]
sys.path += [BASE_PATH] + [os.path.join(BASE_PATH, f) for f in CODE_DIRS]

from libs.job import Job
from libs.executor import Executor

# view.run_command("ctb_run_cucumber")
class CtbRunCucumberCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(): Executor(job).run_cucumber()

# view.run_command("ctb_run_current_file")
class CtbRunCurrentFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(self.view.file_name()): Executor(job).run_current_file()

# view.run_command("ctb_run_current_line")
class CtbRunCurrentLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(self.view.file_name()): Executor(job).run_current_line()

# view.run_command("ctb_run_file_with_tags")
class CtbRunFileWithTagsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(self.view.file_name()): Executor(job).run_file_with_tags()

# view.run_command("ctb_run_last")
class CtbRunLastCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    Executor(job).run_last()

# view.run_command("ctb_run_tags")
class CtbRunTagsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    job = Job(self.view, edit)
    if job.is_executable(): Executor(job).run_tags()

# view.run_command("ctb_set_default_tags")
class CtbSetDefaultTags(sublime_plugin.TextCommand):
  def run(self, edit):
    Job(self.view, edit).save_tags()
