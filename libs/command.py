from libs.settings import Settings
from libs.root import Root

import os

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

  def retrieve(self, target = None, line = None):
    return " ".join(filter(None, [
      self._get_rvm(),
      self._get_bundler(),
      Settings("cucumber_command").retrieve(),
      ":".join(filter(None, [target, line]))
    ]))
