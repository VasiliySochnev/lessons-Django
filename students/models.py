from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.name

# class Student(django.db.models.Model):
#     first_name = django.db.models.CharField(max_length=150, verbose_name='Имя')
#     last_name = django.db.models.CharField(max_length=150, verbose_name='Фамилия', unique=True)
#
#     age = django.db.models.IntegerField(help_text='Введите возраст студента')
#     is_active = django.db.models.BooleanField(default=True)
#     descriptions = django.db.models.TextField(null=True, blank=True)
#     created_at = django.db.models.DateTimeField(auto_now=True)
#     image = django.db.models.ImageField(upload_to='photos/', verbose_name='Фотография')
#     group = django.db.models.ForeignKey(Group, on_delete=django.db.models.DO_NOTHING, related_name='students')
#     profile = django.db.models.OneToOneField(Profile, on_delete=django.db.models.CASCADE)
#     tags = django.db.models.ManyToManyField(Tag)
#
#     STATUS_CHOICES = [
#         ('darft', 'Draft'),
#         ('published', 'Published')
#     ]
#     status = django.db.models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
#
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta():
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#         ordering = ['last_name']
#         db_table = 'custom_table_name'
