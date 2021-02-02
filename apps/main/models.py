from django.db import models

# Create your models here.
class Menu(models.Model):
    active = models.BooleanField(verbose_name='Active?', default=True)
    menuName = models.CharField(verbose_name='Menu Name', max_length = 50)
    menuPDF = models.FileField(verbose_name='Menu PDF', upload_to="media/")
    slug = models.SlugField(verbose_name='slug', max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.menuName