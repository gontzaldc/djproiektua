from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Posta(models.Model):

    usuario = models.ForeignKey('auth.user', on_delete=models.CASCADE,)
    titulua = models.CharField(max_length=200)
    testua = models.TextField()
    sortutako_data = models.DateTimeField(default=timezone.now())
    publikatutako_data = models.DateTimeField(blank=True, null=True)
    publikatuta=models.BooleanField(True)
    image = models.FileField(upload_to='img', null=True, verbose_name="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return u'%s' % self.title

'''class auth_user(models.Model):
    username = models.ForeignKey('auth.user', on_delete=models.CASCADE,)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    password = models.TextField()'''