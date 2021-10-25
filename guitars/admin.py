from django.contrib import admin
from guitars.models import GuitarComercial, GuitarHandMade, Brand, Country
# Register your models here.

admin.site.register(GuitarHandMade)
admin.site.register(GuitarComercial)
admin.site.register(Brand)
admin.site.register(Country)