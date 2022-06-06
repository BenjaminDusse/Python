from import_export import resources
from bank.models import Data

class DataResourse(resources.ModelResource):
    class Meta:
        model = Data