# This is a generated file.
import logging
import datetime


class CatDictFuncs:
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
