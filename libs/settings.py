import sublime

class Settings(object):
  def __init__(self, key):
    self.key = key

  def retrieve(self):
    return sublime.load_settings("Preferences.sublime-settings").get(self.key)
