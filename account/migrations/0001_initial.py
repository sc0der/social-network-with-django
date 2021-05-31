# Generated by Django 2.2.6 on 2019-10-27 08:07

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='логин')),
                ('f_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('l_name', models.CharField(max_length=18, verbose_name='Фамилия')),
                ('password', models.CharField(max_length=12, verbose_name='Пароль')),
                ('unis', models.CharField(choices=[('Шаҳри Душанбе', (('tmt', 'Донишгоҳи миллии Тоҷикистон'), ('ttt', 'Донишгоҳи техниии Тоҷикистон ба номи М.С. Осими'), ('dat', 'Донишгоҳи аграрии Тоҷикистон ба номи Ш.Шоҳтемур'), ('dtt', 'Донишгощи давлатии Тиббии Тоҷикистон ба номи Абуалӣ ибни Сино '), ('dot', 'Донишгоҳи омӯзгории Тоҷикистон ба номи С.Айнӣ'), ('dtijt', 'Донишгоҳи давлатии тиҷорати Тоҷикистон'), ('dtekht', 'Донишоҳи технологии Тоҷикистон'), ('dslavt', 'Донишгоҳи (Славянии) Россия ва Тоҷикистон'), ('ddmwit', 'Донишгоҳи давлатии молия ва иқтисоди Тоҷикистон'), ('dswkh', 'Донишкадаи соҳибкорӣ ва хизмат'), ('ddzt', 'Донишкадаи давлатии забонҳои Тоҷикистон ба номи С. Улуғзода'), ('dtijt', 'Донишкадаи тарбияи ҷисмонии Тоҷикистон ба номи С. Раҳимов'), ('ddfwst', 'Донишкадаи давлатии фарҳанг ва санъати  Тоҷикистон ба номи М. Турсунзода'), ('ddit', 'Донишкадаи исломии Тоҷикистон ба номи Имоми Аъзам'), ('ddstt', 'Донишкадаи давлатии санъати тасвирӣ ва дизайни Тоҷикистон'), ('didorpt', 'Донишкадаи идоракунии давлатии назди Президенти Ҷумҳурии Тоҷикистон '), ('fddmdd', 'Филиали Донишгоҳи давлатии Москва ба номи М.В. Ломоносов дар ш.Душанбе'), ('fddmdd', 'Филиали "Донишгоҳи миллии тадқиқотӣ"-и Донишкадаи энергетикии  Москва  дар ш.Душанбе'), ('fdmtmcis', 'Филиали Донишгоҳи миллии тадқиқотии технологӣ "МИСиС" дар ш.Душанбе'))), ('Вилояти Суғд', (('1', 'Донишгоҳи давлатии Хуҷанд ба номи Б.Ғафуров'), ('2', 'Донишгоҳи давлатии ҳуқуқ, бизнес ва сиёсати Тоҷикистон'), ('3', 'Донишкадаи кӯҳӣ-металургии Тоҷикистон'), ('4', 'Донишкадаи омӯзгории Тоҷикистон дар ш.Панҷакент'), ('5', 'Донишкадаи политехникии Донишгоҳи техниии Тоҷикистон ба номи М.С. Осими дар ш.Хуҷанд'), ('6', 'Филиали Донишгоҳи технологии Тоҷикистон дар ш.Исфара'))), ('Вилояти Хатлон', (('1', 'Донишгоҳи давлатии Кӯлоб ба номи А.Рӯдакӣ'), ('2', 'Донишгоҳи давлатии Бохтар ба номи Н.Хусрав'), ('3', 'Донишгоҳи давлатии Данғара'), ('4', 'Донишгоҳи давлатии тиббии Хатлон'), ('5', 'Донишкадаи энергетикии Тоҷикистон'), ('6', 'Донишкадаи технология ва менеҷменти инноватсионӣ дар ш.Кӯлоб'))), ('ВМКБ', (('1', 'Донишгоҳи давлатии Хоруғ ба номи М.Назаршоев'), ('2', 'Донишгоҳи Осиёи Марказӣ')))], max_length=128, verbose_name='Университет')),
                ('person', models.CharField(choices=[('student', 'Студент'), ('teacher', 'Предодаватель')], max_length=128, verbose_name='кто Вы')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(max_length=50, verbose_name='Местоположение')),
                ('gen', models.CharField(choices=[('M', 'Мард'), ('Z', 'Зан')], max_length=128, verbose_name='Род')),
                ('avatar', models.ImageField(blank=True, default='media/users/tj.png', null=True, upload_to='users/', verbose_name='Аватар')),
                ('admin', models.BooleanField(default=False)),
                ('skills', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('friend', models.ManyToManyField(blank=True, related_name='_person_friend_+', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользовалель',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'Accounts',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('dusts', models.ManyToManyField(related_name='mydest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]