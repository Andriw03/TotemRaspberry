from django.contrib import admin

from raspberry.models import Usuario, Flujo, MCA, Lugar

admin.site.register(Usuario)
admin.site.register(Flujo)
admin.site.register(MCA)
admin.site.register(Lugar)