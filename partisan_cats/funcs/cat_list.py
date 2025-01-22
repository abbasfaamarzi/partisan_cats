# This is a generated file.
import copy
import json

class CatListFuncs:

    def set_current_element(self, index):
        if self.length:
            if 0 <= index < len(self):
                self.current_element = index
        else:
            raise IndexError("Index out of range")

    def move_element(self, element_index, insert_index):
        pop_element = self.pop(element_index)
        self.insert(insert_index, pop_element)

    def move_current_value_to_index(self, element_index):
        self.move_element(self.current_element, element_index)

    def to_json(self):
        """
        Converts the list (self) to a JSON string with an indent of 4 spaces.

        Returns:
            str: The JSON formatted string of the list.
        """
        try:
            data_copy = copy.deepcopy(self)
            json_data = json.dumps(data_copy, indent=4)
            return json_data
        except Exception as e:
            return None

    def is_equal_with_hash_of(self, text):
        """
        Method to compare the SHA-256 hash of the given text with the hash of the original string.

        Args:
            text (str): The text to be compared with the original string's hash.

        Returns:
            bool: True if the hash of the given text matches the original string's hash, False otherwise.

        Logs:
            Logs the result of the hash comparison for debugging and verification.
        """
        result = self.hasher(text) == self.value_hash
        logging.info(
            f"cat_data_type {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Hash comparison result: {result}")
        return result
