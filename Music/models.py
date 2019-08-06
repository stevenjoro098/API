from django.db import models
from django.core.validators import FileExtensionValidator
Hiphop = 1
Trap = 2
Gospel = 3
Bongo = 4
Soul =5
NOT_CAT = 6

Category = (
        (Hiphop,'Hiphop'),
        (Trap,'Trap'),
        (Gospel,'Gospel'),
        (Bongo,'Bongo'),
        (Soul, 'Soul'),
        (NOT_CAT,'No Category'),
        )
class Music(models.Model):
    title = models.CharField(max_length=140)
    image_url = models.ImageField(upload_to='Media/images/music', blank=False)
    artist = models.CharField(max_length=140)
    album = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    genre = models.IntegerField(choices=Category,default=NOT_CAT)
    play = models.TimeField()
    music_file = models.FileField(upload_to='Media/audios',validators=[FileExtensionValidator(['mp3','wav','ogg'])],help_text='.mp3,.wav,.ogg Audio files Allowed',blank=True)
                                 #ext_whitelist=('.mp3','.wav','.ogg'))

    def __str__(self):
        return self.title