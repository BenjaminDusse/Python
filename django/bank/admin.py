from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from bank.models import Data

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    list_display = ('name', "row1", "row2", "row3", "row4", "row5")
