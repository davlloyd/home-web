from django.db import models

class Browser(models.Model):
    version = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.version, self.name)


class Client(models.Model):
    name = models.CharField(max_length=30)
    browser = models.ForeignKey(Browser)
    language = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.browser.name)

    class Meta:
        ordering = ['name']


class Target(models.Model):
    website = models.URLField()

    def __unicode__(self):
        return self.website


class AccessAttempt(models.Model):
    time = models.DateField()
    remoteaddr = models.CharField(max_length=15)
    target = models.ForeignKey(Target)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return u'%s %s %s' % (self.time, self.target.website, self.client)

