# This is a generated file.

from partisan_cats.magics.cat_dict import CatDictMagic
from partisan_cats.vars.cat_dict import CatDictVars
from partisan_cats.statics.cat_dict import CatListStatics
from partisan_cats.funcs.cat_dict import CatDictFuncs
from partisan_cats.properties.cat_dict import CatDictProperties


class CatDict(
    CatDictVars,
    CatDictMagic,
    CatListStatics,
    CatDictFuncs,
    CatDictProperties
):
    """
        This class combines the functionalities of CatJsonTool and CatDictTool
        to provide a comprehensive tool for working with JSON and dictionary data.

        CatDict is a specialized class designed for scenarios where there
        is a need to access the SHA-256 hash of dictionary data and compare a given
        data with its hash. Additionally, it can convert its data to a JSON
        format with an indent of 4 spaces.

        Inherits from:
        - CatJsonTool: Provides JSON conversion functionality.
        - CatDictTool: Provides dictionary management functionality.

        Methods:
        - hasher: Static method to hash the given dictionary data.
        - value_hash: Property to get the SHA-256 hash of the original dictionary data.
        - is_equal_with_hash_of: Method to compare the SHA-256 hash of the given data with the hash of the original dictionary data.
        - value_str: Property to get the original dictionary data as a JSON string.
        - to_json: Method to convert the dictionary data to a JSON string with an indent of 4 spaces.

        Example usage:
        d = CatDict({"key1": "value1", "key2": "value2"})
        """
    pass


if __name__ == "__main__":
    students_info = CatDict({})
    students_info.abbas = CatDict({})
    students_info.abbas.age = 34
    students_info.abbas.python_start = "97!100"
    students_info.arshia = CatDict({})
    students_info.arshia.age = 8
    students_info.arshia.python_start = "64!100"
    students_info.sara = CatDict({})
    students_info.sara.age = 37
    students_info.sara.python_start = "80!100"
    students_info['fatemeh'] = CatDict({'python_start' : "80!100"})
    print(students_info.fatemeh.python_start)
    print(students_info.sara.is_equal_with_hash_of(students_info.sara.value_str))



