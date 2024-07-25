from django.db import models

# Create your models here.

class HomeModel(models.Model):
    image = models.ImageField(upload_to='home_images/')
    title_banner = models.CharField(max_length=20)
    subtitle_banner = models.CharField(max_length=60)
    welcome_video = models.FileField(upload_to='videos/')


class HomeRoomImage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    room = models.ForeignKey(HomeModel, on_delete=models.CASCADE, related_name='home_room_image')

    def __str__(self):
        return str(self.id)+' '+str(self.image)+' '+str(self.room)


class HomeTourImage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    tour = models.ForeignKey(HomeModel, on_delete=models.CASCADE, related_name='home_tour_image')

    def __str__(self):
        return str(self.id)+' '+str(self.image)+' '+str(self.tour)


class HomeBreakfastImage(models.Model):
    image = models.ImageField(upload_to='home_images/')
    breakfast = models.ForeignKey(HomeModel, on_delete=models.CASCADE, related_name='home_breakfast_image')

    def __str__(self):
        return str(self.id)+' '+str(self.image)+' '+str(self.breakfast)
    

class IntroductionModel(models.Model):
    introduction_video = models.FileField(upload_to='videos/')


class GalleryModel(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='gallery_images/')

    def __str__(self):
        return str(self.id)+' '+str(self.image)