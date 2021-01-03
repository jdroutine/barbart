from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Home, Napkin, Gobelin, Tablecloth, Coverlate, About, Christmas, Easter

# Register your models here.
admin.site.register(Home)
admin.site.register(Napkin)
admin.site.register(Gobelin)
admin.site.register(Tablecloth)
admin.site.register(Coverlate)
admin.site.register(About)
admin.site.register(Christmas)
admin.site.register(Easter)