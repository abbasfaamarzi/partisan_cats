# This is a generated file.
from partisan_cats.magics.cat_list import CatListMagic
from partisan_cats.vars.cat_list import CatListVars
from partisan_cats.statics.cat_list import CatListStatics
from partisan_cats.funcs.cat_list import CatListFuncs
from partisan_cats.properties.cat_list import CatListProperties


class CommonCodeCatList(
    CatListMagic,
    CatListVars,
    CatListStatics,
    CatListFuncs,
    CatListProperties,
    list

):
    pass


class CatListTool(
    CommonCodeCatList
):
    """
            CatList is a specialized list class designed for scenarios where there
            is a need to access the SHA-256 hash of list data and compare a given
            data with its hash. Additionally, it can convert its data to a JSON
            format with an indent of 4 spaces.

            Inherits from:
            - HashTool: Provides hashing functionality using SHA-256.
            - CatJsonTool: Provides JSON conversion functionality.
            - list: The built-in Python list type.

            Methods:
            - hasher: Static method to hash the given list data.
            - value_hash: Property to get the SHA-256 hash of the original list data.
            - is_equal_with_hash_of: Method to compare the SHA-256 hash of the given data with the hash of the original list data.
            - value_str: Property to get the original list data as a JSON string.
            - to_json: Method to convert the list data to a JSON string with an indent of 4 spaces.
            - next: Method to get the next element in the list.
            - previous: Method to get the previous element in the list.
            - get_value_from_element_key: Method to get values from dictionary elements by key.

            Example usage:
            l = CatList(["item1", "item2"])
            """
    pass


class CatListSerializerTool(
    CatListTool
):
    @property
    def value_types(self):
        return [
            type(element) for element in self
        ]

    def value_types_show(self, keys : list):
        data_types_str = str(self.value_types)  # استفاده از عبارت منظم برای استخراج نوع داده‌ها
        pattern = re.compile(r"<class '(\w+)'>")
        matches = pattern.findall(data_types_str)




if __name__ == "__main__":

    students = ["Arshia", "Abbas", "Sara"]
    students_cat_list = CatListTool(students)

    #if loop be True
    students = ["Jim", "Bill", "Case"]
    students_cat_list = CatListTool(students)
    students_cat_list.loop = True
    print(students_cat_list.previous)



