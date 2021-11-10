from django.urls import reverse
from django.contrib.auth.models import User


from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to= 'photos/%Y/%m/%d')
    creation_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=30,unique=True,db_index=True)
    cat = models.ForeignKey('Category',on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    class Meta:
        ordering=['creation_date']
class Category(models.Model):
    name = models.CharField(max_length=20, null=False)
    slug = models.SlugField(max_length=20,unique=True,db_index=True)

    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('category',kwargs={'category_slug':self.slug})

class Comentaries(models.Model):
    post=models.ForeignKey(Post,on_delete=models.PROTECT)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    commentary =models.TextField(verbose_name='What you think?')

    class Meta:
        ordering=['created_on']
