from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=300, null=True)
    row1 = models.CharField(max_length=50, null=True, blank=True)
    row2 = models.CharField(max_length=50, null=True, blank=True)    
    row3 = models.CharField(max_length=50, null=True, blank=True)
    row4 = models.CharField(max_length=50, null=True, blank=True)
    row5 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.name