from django.db import models
from  django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

class StatusProject(models.TextChoices):
    NEW = ('New', 'New')
    IN_PROGRESS = ('In_progress', 'In_progress')
    COMPLETED = ('Completed', 'Completed')
    CLOSED = ('Closed', 'Closed')
    PENDING = ('Pending', 'Pending')
    BLOCKED = ('Blocked', 'Blocked')

class PriorityProject(models.TextChoices):
    LOW = ('Low', 'Low')
    MEDIUM = ('Medium', 'Medium')
    HIGH = ('High', 'High')
    VERY_HIGH = ('Very High', 'Very High')
    EXTRA = ('Extra','Extra')
    A=("A", "A")
    URGENT = ('Urgent', 'Urgent')



class ProjectFile(models.Model):
    name = models.CharField(max_length=120, verbose_name="Название файла")
    file = models.FileField(upload_to="projects/", verbose_name="Файл")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания файла")

    class Meta:
        verbose_name = "Файл проекта"
        verbose_name_plural = "Файлы проекта"
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.name}- {self.file.url}"


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название проекта", unique=True)
    description = models.TextField(verbose_name="Описание проекта")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания проекта")
    files = models.ManyToManyField(ProjectFile, related_name="projects",verbose_name="Файлы проекта" )########

    class Meta:
        ordering = ['-title']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        unique_together = ['title', 'description']

    @property
    def count_files(self):
        return self.files.count()

    def __str__(self):
        return f"{self.title} от {self.created_at}."



class Tag(models.Model):
    title = models.CharField(verbose_name="Имя тега", unique=True)

    def __str__(self):
        return f"{self.title}"



class Task(models.Model):
    title = models.CharField(unique=True, verbose_name="Название задачи",validators=[MinLengthValidator(10)] )
    description = models.TextField(verbose_name="Описание ", blank=True,null=True)
    status = models.CharField(max_length=15, verbose_name="Статус", choices=StatusProject.choices, default=StatusProject.NEW)
    priority =models.CharField(max_length=15, verbose_name="Приоритет", choices=PriorityProject.choices)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект", related_name="tasks") #######
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания задачи")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(verbose_name="Дата удаления", blank=True, null=True)
    due_date = models.DateTimeField(verbose_name="срок выполнения")
    tags = models.ManyToManyField(Tag, related_name="tasks", verbose_name="Теги" , blank=True)########
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Пользователь", related_name="tasks", blank=True, null=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ['-due_date', '-priority']
        unique_together = ['title', 'project']

    def __str__(self):
        return f"{self.title} от {self.created_at} для проекта {self.project}.Статус {self.status} u {self.priority}. Выполняет {self.assigned}."








