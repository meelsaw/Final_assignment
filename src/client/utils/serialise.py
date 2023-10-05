import pickle


class Serialiser:
    """
    A class for serialising and deserialising data using the pickle module.
    """

    def serialise(self, data):
        """
        Serialises the data using pickle.

        Parameters:
        - data: The data that need to be serialised

        Returns:
        - bytes: returns the serialised data.
        """
        return pickle.dumps(data)

    def deserialise(self, data):
        """
        deserialises the data using pickle.

        Parameters:
        - data: The data that need to be deserialised

        Returns:
        - bytes: returns the deserialised data.
        """
        return pickle.loads(data)
