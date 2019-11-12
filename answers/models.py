from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Person
from questions.models import Savolho
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Savolho, on_delete=models.CASCADE)
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    text = models.TextField( verbose_name="Добавить ответ")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField( blank=True)
    likes = models.ManyToManyField(Person, related_name = "like")
    class Meta:
        ordering = ('-created_date',)
        
    def get_absolute_url(self):
        return reverse('savolho_detail', args=[self.slug])
    
    def total_comment(self):
        return self.text.count()
    
    def children(self):
        return Comment.objects.filter(parent=self)
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
           
    def save(self, *args, **kwargs):
        title = self.post.title
        self.slug = slugify(title)
        super(Comment, self).save(*args, **kwargs)
   
    def likes(self):
        return self.likes
    
    def total_likes(self):
        return self.likes.count()