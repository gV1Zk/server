from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.


class Button(models.Model):
    mts_id = models.CharField(
        "MTS ID", max_length=191, unique=True, primary_key=True)
    geolocation = models.PointField('Geolocation', default=Point(0, 0))
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    def __str__(self):
        return self.mts_id

    class Meta:
        db_table = 'buttons'
        verbose_name = 'Button'
        verbose_name_plural = 'Buttons'


class ButtonClick(models.Model):
    TYPE_CHOICES = [
        ('click', 'click'),
        ('double_click', 'double_click'),
        ('long_press', 'long_press'),
    ]

    button = models.ForeignKey(Button, models.CASCADE, default=None)
    type = models.CharField('Type', max_length=12,
                            choices=TYPE_CHOICES, default=TYPE_CHOICES[0][0])
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        db_table = 'button_clicks'
        verbose_name = 'Button click'
        verbose_name_plural = 'Button clicks'
