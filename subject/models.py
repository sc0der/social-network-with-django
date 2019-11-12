from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название предмета')
    time = models.DateField(auto_now_add=True, verbose_name='Вақти дохилкунии фан')

    def __str__(self):
            return self.name

    class Meta:
        verbose_name_plural = 'Предметы'
        verbose_name = 'Предмет'
        ordering = ['name']