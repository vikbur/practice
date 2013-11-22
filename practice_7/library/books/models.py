from django.db import models
from django.db import connection
import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from utils.models import TimeStampedModel


# Create your models here.
class Author(TimeStampedModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(null=True, blank=True)
    birthyear = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return "/library/authors/{}/".format(self.id)


class Book(TimeStampedModel):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())
    description=models.TextField('Description')

    class Meta(object):
        verbose_name=u'Kniga'
        verbose_name_plural=u'Knigi'

    def get_absolute_url(self):
        cur = connection.cursor()
        cur.execute(
            "SELECT id FROM books_book WHERE title = %s",
            [self.title])
        return '/library/books/%s/' % cur.fetchall()[0]

    #def get_absolute_url(self):
    #    return "/library/books/%i/" % self.id

    def __unicode__(self):
        return self.title


class Publisher(TimeStampedModel):
    title = models.CharField(max_length=32)
    address = models.TextField()
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    website = models.URLField()

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.website)


class BooksImage(TimeStampedModel):
    small = models.ImageField(upload_to="images/small")
    big = models.ImageField(upload_to="images/big", null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")
    book = models.ForeignKey(Book)

    def getcover(self):
        return self.__cover

    def setcover(self, cover):
        self.__cover = cover

    cover = property(getcover, setcover)

    def __unicode__(self):
        return u'%s' % self.book

    def images_cnt(self):
        cnt=0
        if self.small:
            cnt+=1
        if self.big:
            cnt+=1
        return(cnt)

    def cover(self):
        if self.small:
            return '<img src="%s">' %(self.small.url)
        return None

    cover.allow_tags=True
