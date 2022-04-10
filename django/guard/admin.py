from django.contrib.gis import admin, forms
from django.contrib.gis.db import models


from .models import Button


class ButtonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {'widget': forms.OSMWidget(attrs={'template_name': 'gis/vector-osm.html'})},
    }


admin.site.register(Button, ButtonAdmin)
