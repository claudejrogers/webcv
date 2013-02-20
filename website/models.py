from datetime import date
from django.db import models
from personal.settings import MEDIA_ROOT, MEDIA_URL


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(blank=True, max_length=100)
    title = models.CharField(blank=True, max_length=200)
    lab = models.CharField(blank=True, max_length=200)
    institution = models.CharField(blank=True, max_length=200)
    division = models.CharField(blank=True, max_length=200)
    address1 = models.CharField(blank=True, max_length=200)
    address2 = models.CharField(blank=True, max_length=200)

    class Meta:
        ordering = ['last_name', 'first_name', 'middle_initial']

    def __unicode__(self):
        return u"{0}, {1} {2}".format(self.last_name,
                                      self.first_name,
                                      self.middle_initial)


class Journal(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return u"{0}".format(self.name)


class Article(models.Model):
    title = models.CharField(max_length=500)
    journal = models.ForeignKey(Journal)
    year = models.IntegerField()
    volume = models.CharField(max_length=100)
    start_page = models.CharField(max_length=100)
    end_page = models.CharField(blank=True, max_length=100)
    issue = models.CharField(blank=True, max_length=100)
    abstract = models.TextField(blank=True)
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to=MEDIA_ROOT)
    authors = models.ManyToManyField(Author, through='AuthorOrder')
    date_published = models.DateField(default=date.today())

    class Meta:
        ordering = ['-date_published', 'journal', 'volume', 'issue']

    def ordered_author_list(self):
        return [ao.author for ao in self.authororder_set.order_by(
            'author_number'
        )]

    def image_link(self):
        return self.image.url.replace(MEDIA_ROOT, MEDIA_URL)

    def __unicode__(self):
        issue = "({0})".format(self.issue) if self.issue else ''
        return u"{0}, {1}, {2}{3}, {4}--{5}".format(
            self.journal.name,
            self.year,
            self.volume,
            issue,
            self.start_page,
            self.end_page
        )


class AuthorOrder(models.Model):
    author = models.ForeignKey(Author)
    article = models.ForeignKey(Article)
    author_number = models.IntegerField()

    class Meta:
        ordering = ['article', 'author_number']

    def __unicode__(self):
        return u"{0}. {1}, {2} {3}: {4}".format(
            self.author_number,
            self.author.last_name,
            self.author.first_name,
            self.author.middle_initial,
            self.article.__unicode__()
        )


class Carousel(models.Model):
    image = models.ImageField(upload_to=MEDIA_ROOT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    number = models.SmallIntegerField()

    class Meta:
        ordering = ['number']

    def image_link(self):
        return self.image.url.replace(MEDIA_ROOT, MEDIA_URL)

    def __unicode__(self):
        blurb = ' '.join(self.title.split()[:2])
        return u"{0}: {1}".format(self.number, blurb)
