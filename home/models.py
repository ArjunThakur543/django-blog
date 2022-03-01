from django.db import models
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):            
    sno = models.AutoField(primary_key=True)
    title = models.CharField( max_length=50)
    content = models.TextField()
    author = models.CharField( max_length=50)
    slug = models.SlugField(unique = True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + 'by' + self.author 
    
    def __unicode__(self):
        return self.title 

    def __str__(self):
        return self.title



def pre_save_post_reciever(sender, instance,*args, **kwargs):
    slug=slugify(instance.title)
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)

    instance.slug = slug

pre_save.connect(pre_save_post_reciever, sender=Post)