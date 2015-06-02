from django.db import models
from django.contrib.auth.models import User


class Media(models.Model):

    amount_comments = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)

    name = models.CharField(max_length=40)
    link = models.CharField(max_length=255)

    platforms = models.CharField(max_length=30)
    categories = models.CharField(max_length=255)

    alexa_rank = models.CharField(max_length=15)
    link_to_alexa_rank = models.CharField(max_length=255)

    language = models.CharField(max_length=2)
    amount_journalists = models.CharField(max_length=5)

    email = models.CharField(max_length=100)
    link_to_submit = models.CharField(max_length=255)

    link_to_twitter = models.CharField(max_length=100)
    amount_twitter_followers = models.CharField(max_length=15)

    link_to_facebook = models.CharField(max_length=100)
    amount_facebook_likes = models.CharField('Facebook', max_length=15)

    def platforms_as_list(self):
        return self.platforms.split(',')

    def __str__(self):
        return self.name


class MediaVersion(models.Model):

    media = models.ForeignKey('Media')
    field = models.CharField(max_length=100)

    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)

    def __str__(self):
        return "In " + self.media.name + " in "
        + self.field + " from " + self.old_value + " to " + self.new_value


class MediaMeta(models.Model):

    name = models.CharField(max_length=40)
    link = models.CharField(max_length=255)

    platforms = models.CharField(max_length=30, blank=True)
    categories = models.CharField(max_length=255, blank=True)

    alexa_rank = models.CharField(max_length=15, blank=True)
    language = models.CharField(max_length=2, blank=True)
    amount_journalists = models.CharField(max_length=5, blank=True)

    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class MediaComment(models.Model):

    media = models.ForeignKey('Media')

    author = models.ForeignKey(User, blank=True, null=True)
    text = models.TextField()

    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "In " + self.media.name + " by " + self.author.username


class Journalist(models.Model):

    media = models.ForeignKey('Media')

    slug = models.SlugField(unique=True)

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    categories = models.CharField(max_length=255)

    link_to_twitter = models.CharField(max_length=100)
    amount_twitter_followers = models.CharField(max_length=15)

    link_to_linkedin = models.CharField(max_length=100)

    activity = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " in " + self.media.name


class JournalistVersion(models.Model):

    journalist = models.ForeignKey('Journalist')
    field = models.CharField(max_length=100)

    old_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)

    def __str__(self):
        return "In " + self.journalist.name + " in "
        + self.field + " from " + self.old_value + " to " + self.new_value


class JournalistMeta(models.Model):

    media = models.ForeignKey('Media')

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, blank=True)
    categories = models.CharField(max_length=255, blank=True)

    link_to_twitter = models.CharField(max_length=100, blank=True)
    link_to_linkedin = models.CharField(max_length=100, blank=True)

    activity = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name + " in " + self.media.name


class JournalistArticle(models.Model):

    journalist = models.ForeignKey('Journalist')

    title = models.CharField(max_length=100)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title + " by " + self.journalist.name


class JournalistArticleMeta(models.Model):

    journalist = models.ForeignKey('Journalist')
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title + " by " + self.journalist.name


class JournalistComment(models.Model):

    journalist = models.ForeignKey('Journalist')

    author = models.ForeignKey(User, blank=True, null=True)
    text = models.TextField()

    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "In " + self.journalist + " by " + self.author
