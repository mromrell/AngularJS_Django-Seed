from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    create_date = models.DateTimeField()
    completed = models.BooleanField(default=0)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    user = models.ForeignKey(User)
    is_profile_image = models.BooleanField(default=0)
    is_todo_image = models.BooleanField(default=0)
    photos = models.ImageField(upload_to='img/uploaded', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s, %s' % (self.user, self.is_profile_image)

    class Meta:
        verbose_name_plural = 'Image'