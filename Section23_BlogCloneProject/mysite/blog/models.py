from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now) # IMPORTANT: Here, the DateTimeField default receives the REFERENCE to the function!
                                                              # you shall NOT give the timezone.now(), but timezone.now
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        # we will have a list of comments and some will be approved and others will not
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})
        # this is like: go to the 'post_detail' view and inject the content of the post which has the primary key pk

    def __str__(self):
        return self.title()

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #default is that I have not approved the comment yet
                                                          # this approved_comment is used in the function approve_comments, under the filter
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    # since the comments are going to be approved only by super users on the website,
    #when the comment is written and posted, the user will be taken to the page with all
    #post listed.

    def get_absolute_url(self):
        return reverse('post_list')
