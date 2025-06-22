import abc

class BaseSniffer(abc.ABC):
    def __init__(self, track_name):
        self.track_name = track_name

    @abc.abstractmethod
    def search(self):
        pass

    def normalize(self, title):
        return title.lower().strip()
