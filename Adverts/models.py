from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
MOST_PRIORITY = 1
AVERAGE_PRIORITY  = 2
LEAST_PRIORITY = 3
PRIORITY = (
    (MOST_PRIORITY, 'Most Priority'),
    (AVERAGE_PRIORITY, 'Average Priority'),
    (LEAST_PRIORITY, 'Least Priority'),
)
class ImageAdverts(models.Model):
    company_name = models.CharField(max_length=100)
    ad_priority = models.PositiveIntegerField(choices=PRIORITY,default=LEAST_PRIORITY)
    advert_image = models.ImageField(upload_to='Media/adverts/images',validators=[FileExtensionValidator(['jpg','png','jpeg'])],help_text='Jpg image files allowed', blank=True)

    def __str__(self):
        return self.company_name

class VideosAdverts(models.Model):
    company_name = models.CharField(max_length=100)
    ad_priority = models.PositiveIntegerField(choices=PRIORITY,default=LEAST_PRIORITY)
    video_url = models.FileField(upload_to='Media/adverts/videos',validators=[FileExtensionValidator(['mp4','3gp','flv','mkv'])],help_text='Only Video Files Allowed',null=True)

    def __str__(self):
        return self.company_name

class GifAdverts(models.Model):
    company_name = models.CharField(max_length=100)
    ad_priority = models.PositiveIntegerField(choices=PRIORITY,default=LEAST_PRIORITY)
    gif_url = models.FileField(upload_to='Media/adverts/gif',validators=[FileExtensionValidator(['gif'])],help_text='Gif Files only allowed', null=True)

    def __str__(self):
        return self.company_name
