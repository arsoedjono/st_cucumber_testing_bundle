from libs.settings import Settings
from libs.root import Root

import os
import sublime

class Command(object):
  GEMFILE_NAME = "Gemfile"

  def __init__(self, job):
    self.job = job

  def _get_bundler(self):
    gemfile_dir = os.path.join(self.job.root(), Command.GEMFILE_NAME)
    if os.path.isfile(gemfile_dir): return "bundle exec"

  def _get_rvm(self):
    file_dir = os.path.expanduser(Settings("rvm_path").retrieve())
    if file_dir and os.path.isfile(file_dir): return "{0} -S".format(file_dir)

  def last_command(self):
    return sublime.load_settings(Settings.SETTINGS_FILE).get(Settings.LAST_RUN_KEY)

  def retrieve(self, target = None, line = None, tags = None):
    return " ".join(filter(None, [
      self._get_rvm(),
      self._get_bundler(),
      Settings("cucumber_command").retrieve(),
      ":".join(filter(None, [target, line])) or None,
      tags
    ]))

  def save(self, command):
    settings = sublime.load_settings(Settings.SETTINGS_FILE)
    settings.set(Settings.LAST_RUN_KEY, command)
    sublime.save_settings(Settings.SETTINGS_FILE)
