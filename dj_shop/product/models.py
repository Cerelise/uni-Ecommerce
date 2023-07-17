import os
import uuid

from io import BytesIO
from PIL import Image

from django.core.files import File

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    Ctype = models.IntegerField(default=1)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    # pid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    tip = models.CharField(max_length=50, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/',
                                  blank=True,
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return self.name

    @property
    def category_slug(self):
        # return int(self.category.slug)
        return self.category.slug

    @property
    def ctype(self):
        return self.category.Ctype

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        # image.name
        # FileUrl = image.name.split('/')[1]
        filename = os.path.basename(image.name)
        thumbnail = File(thumb_io, name=filename)

        return thumbnail