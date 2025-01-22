# This is a generated file.
from partisan_cats.properties.cat_string import CatStringProperty


class CatStringMachine(
    CatStringProperty,
    str
):
    """
    CatString is a specialized string class designed for scenarios where
    there is a need to access the SHA-256 hash of data and compare a given
    data with its hash.

    Inherits from:
    - HashTool: Provides hashing functionality using SHA-256.
    - str: The built-in Python string type.

    Methods:
    - hasher: Static method to hash the given string data.
    - value_hash: Property to get the SHA-256 hash of the original string data.
    - is_equal_with_hash_of: Method to compare the SHA-256 hash of the given data with the hash of the original string data.
    - value_str: Property to get the original string data.

    Example usage:
    s = CatString("example_string")
    """

    pass




