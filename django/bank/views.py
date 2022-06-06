from django.contrib import messages
from django.shortcuts import render
from tablib import Dataset

from bank.models import Data
from bank.resources import DataResourse


def home(request):
    if request.method == 'POST':
        data_resource = DataResourse()
        dataset = Dataset()
        new_data = request.FILES['myfile']

        if not new_data.name.endswith("xlsx"):
            messages.info(request, "Wrong format")
            return render(request, 'upload.html')

        imported_data = dataset.load(new_data.read(), format="xlsx")
        for data in imported_data:
            value = Data(
                data[0],
                data[1],
                data[2],
                # data[3],
                # data[4],
                # data[5],
                # data[6],
            )
            value.save()

    context = {}
    return render(request, 'index.html', context)
