from PIL import Image
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class Person(AbstractUser):
    gender = (
        ('M','Мард'),
        ('Z', 'Зан' ),
    )

    persons = (
        ('student', 'Студент'),
        ('teacher', 'Предодаватель'),
    )
    UNIs = [
        ('Шаҳри Душанбе', (
            ('tmt', 'Донишгоҳи миллии Тоҷикистон'),                
            ('ttt', 'Донишгоҳи техниии Тоҷикистон ба номи М.С. Осими'),
            ('dat', 'Донишгоҳи аграрии Тоҷикистон ба номи Ш.Шоҳтемур'),
            ('dtt', 'Донишгощи давлатии Тиббии Тоҷикистон ба номи Абуалӣ ибни Сино '),
            ('dot', 'Донишгоҳи омӯзгории Тоҷикистон ба номи С.Айнӣ'),
            ('dtijt', 'Донишгоҳи давлатии тиҷорати Тоҷикистон'),
            ('dtekht', 'Донишоҳи технологии Тоҷикистон'),
            ('dslavt', 'Донишгоҳи (Славянии) Россия ва Тоҷикистон'),
            ('ddmwit', 'Донишгоҳи давлатии молия ва иқтисоди Тоҷикистон'),
            ('dswkh', 'Донишкадаи соҳибкорӣ ва хизмат'),
            ('ddzt', 'Донишкадаи давлатии забонҳои Тоҷикистон ба номи С. Улуғзода'),
            ('dtijt', 'Донишкадаи тарбияи ҷисмонии Тоҷикистон ба номи С. Раҳимов'),
            ('ddfwst', 'Донишкадаи давлатии фарҳанг ва санъати  Тоҷикистон ба номи М. Турсунзода'),
            ('ddit', 'Донишкадаи исломии Тоҷикистон ба номи Имоми Аъзам'),
            ('ddstt', 'Донишкадаи давлатии санъати тасвирӣ ва дизайни Тоҷикистон'),
            ('didorpt', 'Донишкадаи идоракунии давлатии назди Президенти Ҷумҳурии Тоҷикистон '),
            ('fddmdd', 'Филиали Донишгоҳи давлатии Москва ба номи М.В. Ломоносов дар ш.Душанбе'),
            ('fddmdd', 'Филиали "Донишгоҳи миллии тадқиқотӣ"-и Донишкадаи энергетикии  Москва  дар ш.Душанбе'),
            ('fdmtmcis', 'Филиали Донишгоҳи миллии тадқиқотии технологӣ "МИСиС" дар ш.Душанбе'),
            )
         ),
        ('Вилояти Суғд', (
            ('1', 'Донишгоҳи давлатии Хуҷанд ба номи Б.Ғафуров'),
            ('2', 'Донишгоҳи давлатии ҳуқуқ, бизнес ва сиёсати Тоҷикистон'),
            ('3', 'Донишкадаи кӯҳӣ-металургии Тоҷикистон'),
            ('4', 'Донишкадаи омӯзгории Тоҷикистон дар ш.Панҷакент'),
            ('5', 'Донишкадаи политехникии Донишгоҳи техниии Тоҷикистон ба номи М.С. Осими дар ш.Хуҷанд'),
            ('6', 'Филиали Донишгоҳи технологии Тоҷикистон дар ш.Исфара'),

            )
         ),
        ('Вилояти Хатлон', (
            ('1', 'Донишгоҳи давлатии Кӯлоб ба номи А.Рӯдакӣ'),
            ('2', 'Донишгоҳи давлатии Бохтар ба номи Н.Хусрав'),
            ('3', 'Донишгоҳи давлатии Данғара'),
            ('4', 'Донишгоҳи давлатии тиббии Хатлон'),
            ('5', 'Донишкадаи энергетикии Тоҷикистон'),
            ('6', 'Донишкадаи технология ва менеҷменти инноватсионӣ дар ш.Кӯлоб'),
            
            )
         ),
        ('ВМКБ', (
            ('1', 'Донишгоҳи давлатии Хоруғ ба номи М.Назаршоев'),
            ('2', 'Донишгоҳи Осиёи Марказӣ'),
               
            )
         ),
    ]
    username = models.CharField(max_length=20, unique=True, verbose_name='логин' )
    f_name = models.CharField(max_length=20, verbose_name="Имя")
    l_name = models.CharField(max_length=18, verbose_name="Фамилия")
    password = models.CharField(max_length=12, verbose_name="Пароль")
    unis = models.CharField(max_length=128,choices=UNIs, verbose_name='Университет')
    person = models.CharField(max_length=128,choices=persons, verbose_name="кто Вы")
    email = models.EmailField(max_length=50, verbose_name="Email")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    city = models.CharField(max_length = 50, verbose_name="Местоположение")
    gen = models.CharField(max_length=128,choices=gender, verbose_name="Род")
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name="Аватар" )
    admin = models.BooleanField(default=False)
    friend = models.ManyToManyField('self', blank=True)
    skills = models.CharField(max_length=128)
    slug = models.SlugField()
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('user_detail', args=[self.username])



    def image_img(self):
        if self.avatar:
            return self.avatar.url

    
    class Meta:
        db_table = 'Accounts'
        managed = True
        verbose_name = 'Пользовалель'
        verbose_name_plural = 'Пользователи'
    
class Friend(models.Model):
    dusts = models.ManyToManyField(Person, related_name="mydest")
    current_user = models.ForeignKey(Person, related_name='owner', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return "From {}, to {}".format(self.current_user.username, self.dusts.username)
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)
    
    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.dusts.remove(new_friend)
        
    def __str__(self):
        return str(self.current_user)