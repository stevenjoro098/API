from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
# Create your models here.
class Movies(models.Model):
    image_url = models.ImageField(upload_to='Media/images/movies', blank=True)
    title = models.CharField(max_length=140)
    category = models.IntegerField(default=1)
    movie_url = models.FileField(upload_to='Media/movies', validators=[FileExtensionValidator(['mp4','mkv','flv'])],help_text='MP4,MKV,3GP Files allowed',blank=True)
    star_ratings = models.PositiveIntegerField(default=3)
    plot = models.TextField()
    year = models.PositiveIntegerField(default=2018)
    rating = models.PositiveIntegerField(default=1)
    runtime = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    website = models.URLField(blank=True)
    views = models.PositiveIntegerField(default=100)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Movies.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
            return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

