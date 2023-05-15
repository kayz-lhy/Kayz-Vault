class File:
    _filelist = []

    def __init__(self, directory):
        self._directory = directory

    def __iadd__(self, file):
        self._filelist.append(file)

    def set