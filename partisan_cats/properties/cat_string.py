# This is a generated file.
import re

class CatStringProperty:
    @property
    def class_to_model_name(self):
        return re.sub('([A-Z])', r'_\1', self).lower().lstrip('_')

    @property
    def model_name_to_class(self):
        return ''.join(word.title() if i > 0 else word for i, word in enumerate(self.split('_')))
