from django.db import models
# from django.utils.text import slugify
import datetime
# from django.core.files.images import ImageFile
from django.urls import reverse
from subject.models import Subject
from account.models import Person
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

        
class Savolho(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name='Заголовка')
    savol = models.TextField(verbose_name='Вопрос')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Нашр шуд")
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE, verbose_name='Фан')
    author = models.ForeignKey(Person, on_delete = models.CASCADE )
    image = models.ImageField(upload_to='from_questions/', null=True, blank=True, verbose_name='рисунок')
    likes = models.ManyToManyField(Person, related_name="likes", blank=True)
    slug = models.SlugField(unique = True)
    class Meta:
        ordering = ('-published',)
    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
      
    def snippet(self):
        return self.savol[:50]

    
    def image_img(self):
        return self.image
    
    def get_absolute_url(self):
        return reverse('savolho_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        title = self.title
        year = str(datetime.datetime.now().date().year)

        # month = str(datetime.datetime.now().date().month)
        month = str(datetime.datetime.now().date().strftime("%m"))

        # day = str(datetime.datetime.now().date().day)
        day = str(datetime.datetime.now().date().strftime("%d"))

        # hour = str(datetime.datetime.now().hour)
        hour = str(datetime.datetime.now().strftime("%H"))

        # minute = str(datetime.datetime.now().minute)
        minute = str(datetime.datetime.now().strftime("%M"))

        # second = str(datetime.datetime.now().second)
        second = str(datetime.datetime.now().strftime("%S"))

        time = year + ' ' + month + ' ' + day + \
            ' ' + hour + ' ' + minute + ' ' + second

        self.slug = slugify(title + ' ' + time)
        super(Savolho, self).save(*args, **kwargs)

def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)
# class Profile(models.Model):
#     user_post = models.ForeignKey(Savolho, on_delete=models.CASCADE)
#     user_prof = models.ForeignKey(Person, on_delete=models.CASCADE)
    