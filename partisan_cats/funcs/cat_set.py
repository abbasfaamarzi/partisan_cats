# This is a generated file.
from partisan_cats.machines.cat_list import CatListTool


class CatSetFuncs:

    def union(self, other_list):
        return CatListTool(list(dict.fromkeys(self.data + other_list)))

    def intersection(self, other_list):
        return CatListTool([item for item in self.data if item in other_list])

    def difference(self, other_list):
        return CatListTool([item for item in self.data if item not in other_list])

    def symmetric_difference(self, other_list):
        return CatListTool([item for item in self.data if item not in other_list] + [item for item in other_list if
                                                                                     item not in self.data])

