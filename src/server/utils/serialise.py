import pickle


class Serialiser:
    """
    A class for serialising and deserialising data using the pickle module.
    """
    def serialise(self, data):
        """
        Serialises the data using pickle.
        :param data: The data that need to be serialised
        :return: bytes: returns the serialised data.
        """
        return pickle.dumps(data)

    def deserialise(self, data):
        """
        deserialises the data using pickle.
        :param data: The data that need to be deserialised
        :return: bytes: returns the deserialised data.
        """
        return pickle.loads(data)
