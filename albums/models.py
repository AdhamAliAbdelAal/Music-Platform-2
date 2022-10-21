from django.db import models
from artists.models import Artist
from model_utils.fields import AutoCreatedField
# Create your models here.


class TimeStampedModel(models.Model):
    creation_time =AutoCreatedField()

    class Meta:
        abstract = True


class Album(TimeStampedModel):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
        default="New Album",
    )
    release_time = models.DateTimeField(
        null=False,
        blank=False
    )
    cost = models.DecimalField(
        decimal_places=10,
        max_digits=20
    )
    is_approved = models.BooleanField(
        default=False,
    )

    def _str_(self):
        return self.name
