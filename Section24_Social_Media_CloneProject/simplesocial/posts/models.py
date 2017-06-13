from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import misaka

from groups.models import Group
# Create your models here.
# POSTS MODELS.PY

from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True) # Create_at is the creation date
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        # That way, if someone puts a link in their post, it won't show as brackets
        #and all that machine representation. It will show as a true html
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,
                                              'pk':self.pk})
    class Meta:
        ordering = ['-created_at'] # the '-' is to be in descending order. The newer first
        unique_together = ['user','message'] #Every message is uniquely linkd to the user
