from django.db import models

# Create your models here.
from django.db import models
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title
class Schedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
        ('Saturday', 'Суббота'),
        ('Sunday', 'Воскресенье'),
    ]

    TYPE_CHOICES = [
        ('Lecture', 'Лекция'),
        ('Seminar', 'Семинар'),
        ('Lab', 'Лабораторное занятие'),
    ]

    day = models.CharField(max_length=20, choices=DAY_CHOICES)  # День недели
    start_time = models.TimeField()  # Время начала занятия
    end_time = models.TimeField()  # Время окончания занятия
    subject = models.CharField(max_length=100)  # Название предмета
    teacher = models.CharField(max_length=100)  # ФИО преподавателя
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)  # Тип занятия
    color = models.CharField(max_length=20, default='lightgray')  # Цвет для отображения

    def __str__(self):
        return f'{self.day} {self.start_time} - {self.end_time}: {self.subject}'




