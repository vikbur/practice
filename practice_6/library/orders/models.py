from django.db import models
from books.models import *
from datetime import datetime
from utils.models import TimeStampedModel


# Create your models here.
class Customer(TimeStampedModel):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    address = models.TextField()
    is_approved = models.BooleanField()
    email = models.EmailField('Email')

    def __unicode__(self):
        return u'%s %s' % (
            self.lastName, self.firstName)


class Order(TimeStampedModel):
    itemId = models.ForeignKey(Book)
    create = models.DateField(default=datetime.now())
    customer = models.ForeignKey(Customer, null=True)
