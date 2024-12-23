from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

    class Meta():
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        ordering = ['name']


class Student(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField()
    year = models.CharField(max_length=6, choices=YEAR_IN_SCHOOL_CHOICES, default=FIRST_YEAR, verbose_name='Курс')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='Группа')
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta():
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']

# class Group(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
#     def __str__(self):
#         return self.name

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
#         ('draft', 'Draft'),
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
