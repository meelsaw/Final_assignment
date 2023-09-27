import pickle


class Serialiser:
    def serialise(self, data):
        return pickle.dumps(data)

    def deserialise(self, data):
        return pickle.loads(data)
