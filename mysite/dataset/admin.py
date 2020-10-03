from django.contrib import admin
from .models import Dataset,Contributor, ContributrFolder, PremiumDataset
# Register your models here.

admin.site.register(Dataset)
admin.site.register(Contributor)
admin.site.register(ContributrFolder)
admin.site.register(PremiumDataset)