import os

class Root(object):
  def __init__(self, file_name, cucumber_folder_name):
    self.file_name = file_name
    self.cucumber_folder_name = cucumber_folder_name

  def _via_inclusion(self):
    folder_name = "/{0}/".format(self.cucumber_folder_name)
    print(folder_name)
    print(self.file_name)
    if not folder_name in self.file_name: return

    return self.file_name[:self.file_name.rindex(folder_name)]

  def _via_upwards(self):
    path = self.file_name

    while True:
      (path, current_directory) = os.path.split(path)
      if not current_directory: return
      if self.cucumber_folder_name in os.listdir(path): return path

  def retrieve(self):
    if not (self.file_name or self.cucumber_folder_name): return
    return self._via_inclusion() or self._via_upwards()
