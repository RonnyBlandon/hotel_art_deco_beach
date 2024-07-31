from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
# Create your models here.

class RoomModel(TimeStampedModel, models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    amount_of_people = models.IntegerField()
    size = models.IntegerField('Size in sq')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField()
    slug = models.SlugField(editable=False, max_length=300)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
    
    def __str__(self):
        return str(self.id)+' - '+self.name

    # Added unique slugs to products
    def save(self, *args, **kwargs):
        #We join the room name with the id to create the unique slug
        slug_unique = f"{self.name} {self.id}"
        self.slug = slugify(slug_unique)
        super(RoomModel, self).save(*args, **kwargs)


class RoomImage(models.Model):
    image = models.ImageField(upload_to='room_images/')
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE, related_name='room_image')

    def __str__(self):
        return str(self.id)+' '+str(self.image)+' '+str(self.room)