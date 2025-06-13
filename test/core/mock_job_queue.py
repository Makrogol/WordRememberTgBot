class MockJobQueue:
    def __init__(self):
        self.__when = []
        self.__callbacks = []

    def run_once(self, callback, when):
        self.__when.append(when)
        self.__callbacks.append(callback)

    def get_when(self):
        return self.__when

    def get_callbacks(self):
        return self.__callbacks
