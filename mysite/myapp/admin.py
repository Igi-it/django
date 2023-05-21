from django.contrib import admin
from .models import Vyrobce, Zbran, Obchod, Zamestnanec

# Register your models here.
admin.site.register(Vyrobce)
admin.site.register(Zbran)
admin.site.register(Obchod)
admin.site.register(Zamestnanec)