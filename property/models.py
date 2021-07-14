from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Property_buildings(models.Model):
    # today = datetime.datetime.now()
    property_auto = models.AutoField(primary_key=True)
    id = models.IntegerField(default=1)
    property_block = models.CharField(max_length=10)
    property_name = models.CharField(max_length=45)
    property_type = models.CharField(max_length=25, default="Residential")
    property_category = models.CharField(
        max_length=35, default="Apartment buildings")
    property_year = models.TextField(blank=True, null=True)
    property_added_by = models.ForeignKey(to=User, on_delete=CASCADE)

    class Meta:
        db_table = 'property_buildings'
