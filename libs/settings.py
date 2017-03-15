import sublime

class Settings(object):
  def __init__(self, key):
    self.key = key

  def _default_settings(self):
    return sublime.load_settings("Preferences.sublime-settings")

  def _user_settings(self):
    return sublime.load_settings("CucumberTestingBundle.sublime-settings")

  def retrieve(self):
    return self._user_settings().get(
      self.key,
      self._default_settings().get(self.key, None)
    )
