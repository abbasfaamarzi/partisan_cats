# This is a generated file.
import copy


class CatListProperties:

    @property
    def first_element(self):
        """
        Property to get the first element of the list.

        Returns:
            The first element of the list.
        """
        return self[0]

    @property
    def last_element(self):
        """
        Property to get the last element of the list.

        Returns:
            The last element of the list.
        """
        return self[-1]

    @property
    def current_element_value(self):
        return self[self.current_element]

    @property
    def next(self):
        """
        Method to get the next element in the list.

        Returns:
            The next element in the list.

        Raises:
            StopIteration: If the end of the list is reached.
        """
        if self.current_element_value == self.last_element:
            if self.loop:
                self.current_element = 0
                return self.first_element
            else:
                pass
        else:
            self.current_element += 1
            return self[self.current_element]

    @property
    def previous(self):
        """
        Method to get the previous element in the list.

        Returns:
            The previous element in the list.

        Raises:
            StopIteration: If the beginning of the list is reached.
        """
        if self.current_element_value == self.first_element:
            if self.loop:

                self.current_element = copy.copy(self.index(self.last_element))
                return self.last_element
            else:
                pass
        else:
            self.current_element -= 1
            return self[self.current_element]

    def get_value_from_element_key(self, key):
        """
        Method to get values from dictionary elements by key.

        Args:
            key (str): The key to get values for.

        Returns:
            list: A list of values corresponding to the key.
        """
        value_list = []
        try:
            for dict_element in self:
                if key in dict_element:
                    value_list.append(dict_element[key])
        except Exception as e:
            print(e)
        else:
            return value_list

    @property
    def length(self):
        return len(self)

    @property
    def list_data(self) -> dict:
        data = self
        return data



    @property
    def list_to_json(self):
        data = self.list_data
        return self.to_json(data)

    @property
    def convert_to_json(self):
        """
        Converts the dictionary or list data to a JSON string with an indent of 4 spaces.

        Returns:
            str: The JSON formatted string of the data.

        Logs:
            Logs the JSON conversion for debugging and verification.
        """
        try:
            json_data = json.dumps(self, indent=4)
            logging.info(f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Data converted to JSON: {json_data}")
            return json_data
        except TypeError as e:
            logging.error(f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Error converting to JSON: {e}")
            return None

    @staticmethod
    def hasher(text):
        """
        Static method to hash the given text using SHA-256 algorithm.

        Args:
            text (str): The text to be hashed.

        Returns:
            str: The hexadecimal digest of the SHA-256 hash.

        Logs:
            Logs the hashed text for debugging and verification.
        """
        hashed_text = hashlib.sha256(
            json.dumps(
                text, sort_keys=True
            ).encode()
        ).hexdigest()
        logging.info(
            f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Text hashed: {hashed_text}")
        return hashed_text

    @property
    def value_hash(self):
        """
        Property to get the SHA-256 hash of the original string.

        Returns:
            str: The hexadecimal digest of the SHA-256 hash of the original string.

        Logs:
            Logs access to the hashed value for debugging and verification.
        """
        hashed_value = self.hasher(self.value_str)
        logging.info(
            f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Value hash accessed: {hashed_value}")
        return hashed_value

    @property
    def value_str(self):
        """
        Property to get the original string value.

        Returns:
            str: The original string value.

        Logs:
            Logs access to the original string for debugging and verification.
        """
        original_value = self.__str__()
        logging.info(
            f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Original string accessed: {original_value}")
        return original_value

