from django.db import models

# Create your models here.

class NewsRoom(models.Model):
    RONGAI = 1
    KITENGELA = 2
    UMOJA = 3
    THIKA = 4
    NGONG = 5
    EASTLEIGH = 6
    KIKUYU = 7
    UTHIRU = 8
    ALL = 9
    CATEGORIES = (
        (RONGAI,'Hiphop'),
        (KITENGELA,'Trap'),
        (UMOJA,'Gospel'),
        (THIKA,'THIKA'),
        (NGONG, 'NGONG'),
        (EASTLEIGH,'EASTLEIGH'),
        (KIKUYU,'KIKUYU'),
        (UTHIRU,'UTHIRU'),
        (ALL,'ALL')
    )

    title = models.CharField(max_length=250)
    image_url = models.ImageField(upload_to="Media/newsroom")
    events = models.TextField(max_length=500)
    venue = models.CharField(max_length = 250,default="Nairobi")
    slug = models.SlugField(unique=True)
    location = models.IntegerField(choices=CATEGORIES,default=ALL)


    def __str__(self):
        return self.title