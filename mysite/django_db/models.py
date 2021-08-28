import datetime

from django.db import models


# Create your models here.
from django.db.models import F


class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    name = models.CharField(max_length=128)
    first_name = models.CharField("person's first name", max_length=30)
    last_name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    age = models.PositiveIntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    def baby_boomer_status(self):
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    class Meta:
        # 按 name 升序排列，并使空值最后排序
        ordering = [F('name').asc(nulls_last=True)]
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='idx_first_name')
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='contains_age')
        ]


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Question(models.Model):
    text = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField(default=None)

    class Meta:
        order_with_respect_to = 'question'


class CommonInfo(models.Model):
    """
    抽象基类
    """

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        """
        子类也可继承父类的 Meta
        """
        abstract = True
        ordering = ['name']


class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False


class Student(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        db_table = 'student'


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


class OrderedPerson(Person):
    class Meta:
        ordering = ['last_name']
        proxy = True
