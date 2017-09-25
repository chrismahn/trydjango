from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from .validators import validate_category
from .utils import unique_slug_generator


User = settings.AUTH_USER_MODEL

# Create your models here.
class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    #my_date_field = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name  #obj.title


def rl_pre_save_reciever(sender, instance, *args, **kwargs):
    instance.category = instance.category.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

'''
def rl_post_save_reciever(sender, instance, created, *args, **kwargs):
    print('Saved..')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()
'''

pre_save.connect(rl_pre_save_reciever, sender=RestaurantLocation)
#pre_save.connect(rl_post_save_reciever, sender=RestaurantLocation)

