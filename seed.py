import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from django.utils import timezone
from django.db.models.functions.datetime import datetime
import calendar
from django.db.models import Count,Avg
from project.models import Project, Task, Tag, ProjectFile, PriorityProject, StatusProject
from random import random
from datetime import timedelta
from django.contrib.auth.admin import User
from django.core.paginator import Paginator


def create_tag():
    tags_list = [Tag(title='Backend'),
              Tag(title='Frontend'),
              Tag(title='Q&A'),
              Tag(title='Design'),
              Tag(title='DevOPS')]
    Tag.objects.bulk_create(tags_list)


#create_tag()

def create_projects():
    projects = [
        Project(title="Project 1", description="Project 1"),
        Project(title="Project 2", description="Project 2"),
        Project(title="Project 3", description="Project 3"),
        Project(title="Project 4", description="Project 4"),
        Project(title="Project 5", description="Project 5"),
    ]

    Project.objects.bulk_create(projects)

#create_projects()

"""
Импортируйте модели Project, ProjectFile
2. Создайте несколько записей файлов для каждого из существующих проектов.
3. Для каждого объекта проекта, созданного ранее, добавьте объекты созданных файлов
методом add().
4. Убедитесь, что данные были созданы и сохранены в базу данных."""
def create_project_files():
    project_files = [
        ProjectFile(name="File_1", file="File_1.txt"),
        ProjectFile(name="File_2", file="File_2.txt"),
        ProjectFile(name="File_3", file="File_3.txt"),
        ProjectFile(name="File_4", file="File_4.txt"),
        ProjectFile(name="File_5", file="File_5.txt"),
        ProjectFile(name="File_6", file="File_6.txt"),
    ]
    ProjectFile.objects.bulk_create(project_files)

# create_project_files()
# project1 = Project.objects.get(title="Project 1")
# project_file1 = ProjectFile.objects.get(name="File_6")
# print(project1.title, project1.description)
# print(project_file1.file, project_file1.name)
# project1.files.add(project_file1)
# project_file3 = ProjectFile.objects.get(name="File_3")
# project1.files.add(project_file3)
# print(project1.title, project1.description, project1.files.first(), project1.files.last())

"""
Импортируйте модель Пользователя (User), которого по умолчанию предлагает Django.
2. Создайте пять разных пользователей:
○ Backend
○ Frontend
○ DevOPS
○ Q&A
○ Designer
3. Убедитесь, что все они сохранены в базу данных."""
from django.contrib.auth.models import User
# user_backend = User.objects.create(username='Backend', password='123')
# user_frontend = User.objects.create(username='Frontend', password='123')
# user_designer = User.objects.create(username='Designer', password='123')
# user_qa = User.objects.create(username='QA', password='123')
# user_devops = User.objects.create(username='DevOps', password='123')
# user_backend = User.objects.get(username='Backend')
# user_frontend = User.objects.get(username='Frontend')
# user_designer = User.objects.get(username='Designer')
# user_qa = User.objects.get(username='QA')
# user_devops = User.objects.get(username='DevOps')
# print(user_backend.id, user_frontend.id, user_designer.id, user_qa.id, user_devops.id)

"""
Импортируйте модель Task.
2. Для каждого проекта создайте задачи. По одной-две для каждого тега.
3. Для foreignkey полей передаём объекты, которые мы создавали ранее.
4. Убедитесь, что данные были созданы и сохранены в базу данных.
title = models.CharField(unique=True, verbose_name='Title', validators=[MinLengthValidator(10)])
    PriorityProject = models.CharField(max_length=15, choices=PriorityProject.choices, verbose_name='PriorityProject')
    assigned_to
"""
project1 = Project.objects.get(title="Project 1")
user_backend = User.objects.get(username='Backend')
user_frontend = User.objects.get(username='Frontend')
tag_backend = Tag.objects.get(title="Backend")
tag_fronted = Tag.objects.get(title="Frontend")
# task1 = Task.objects.create(title="Task 1", description="Task 1111111", status=StatusProject.NEW, priority=PriorityProject.MEDIUM,
#                             project=project1, due_date=timezone.now(),assigned=user_backend)
# task1.tags.add(tag_backend)

# task2 = Task.objects.create(title="Task 2", description="Task 22222222", status=StatusProject.IN_PROGRESS, priority=PriorityProject.LOW,
#                             project=project1, due_date=timezone.now(), assigned=user_frontend)
# task2.tags.add(tag_fronted)
project2 = Project.objects.get(title="Project 2")
user_qa = User.objects.get(username='QA')
user_devops = User.objects.get(username='DevOps')
tag_qa = Tag.objects.get(title="Q&A")
tag_devops = Tag.objects.get(title="DevOPS")
# task3 = Task.objects.create(title="Task 3", description="Task 3333333", status=StatusProject.NEW, priority=PriorityProject.MEDIUM,
#                          project=project2, due_date=timezone.now(), assigned=user_devops)
# task3.tags.add(tag_devops)
# task3.tags.add(tag_qa)
"""
1. Получите все объекты тегов.
2. У каждого объекта созданных задач обратитесь к полю тегов через точку.
3. У поля ManyToMany (tags) вызовите метод add и передайте ему объект тега.
○ Объект тега будет зависеть от того, какой title будет в задаче, например:
(‘Добавить новый эндпоинтʼ - Backend tag, ‘Обновить страницу ответа 404ʼ - Frontend tag)

"""
task1=Task.objects.get(title="Task 1")
# task1.tags.add(tag_devops)
# task1.tags.add(tag_fronted)

task2=Task.objects.get(title="Task 2")
# task2.tags.add(tag_backend)
# task2.tags.add(tag_qa)

"""
1. Импортируйте модели тегов Tag.
2. Напишите запрос, который позволит получить список всех тегов.
3. Выведите имя каждого тега.
4. Получите самый первый тег.
5. Получите самый последний тег.
6. Получите кол-во всех тегов.
"""

#print(*Tag.objects.all(), sep="\n")
# print(Tag.objects.first())
# print(Tag.objects.last(), sep="\n")
# print(Tag.objects.count(), sep="\n")

"""8
1. Напишите запрос, который будет искать тэг по определённому имени
2. Проверьте наличие такого тега методом, который выдаёт True или False на наличие объекта
"""
#tag_proverca = Tag.objects.filter(title="Backend").exists()
# print(Tag.objects.filter(title="Backend").exists())
#
# print(Tag.objects.filter(title="Byckend").exists())

"""9
 Напишите запрос, который позволит получить теги, у которых в имени будет совпадение по
переданной строке, например: “...Tagˮ
2. Выведите имена всех этих тегов.
"""

# tag_prov = Tag.objects.filter(title__icontains="end")
# print(*tag_prov, sep="\n")

"""
10
1. Импортируйте модуль datetime и модель Project.
2. Создайте объект даты, по которой нужно сделать поиск.
3. Напишите запрос, который позволит получить список проектов, которые равны или старше
переданной даты создания.
4. Выведите имена таких проектов.
"""

date =timezone.datetime(2025,9,11).astimezone()

#print(date)

project_date = Project.objects.filter(created_at__gte=date)
#print(*project_date, sep="\n")

"""11
Использование Q-класса для комбинированных условий
1. Импортируйте модель Project.
2. Напишите запрос, который позволит получить необходимые проекты:
    ○ Реализуйте фильтрацию, которая будет проходить два условия:
        ■ Проекты, равные или больше указанной даты
        ■ Проекты, у которых в имени есть строка ‘TIʼ
3. Выведите имена таких проектов."""
from django.db.models import Q

project_neob = Project.objects.filter(Q(created_at__gte=date) & Q(title__icontains="ro"))
#print(*project_neob,sep="\n")

"""12 Получение списка всех файлов для проекта
1. Напишите запрос, который позволит получить список всех файлов, которые привязаны к
конкретному проекту. Поиск произведите по имени проекта.
2. Выведите только пути к каждому файлу
"""

# for item in Project.objects.all():
#     #print(item.title)
#     for file in item.files.all():
#         print(file.file.url, sep="\n")
#         print("-"*20)


"""13Фильтрация задач по статусу и приоритету
1. Напишите запрос, который поможет получить только те задачи, у которых:
    ○ Статус “newˮ
    ○ Приоритетность “Urgentˮ
2. Выведите информацию по каждой такой задаче:
    ○ Название
    ○ Статус
    ○ Приоритетность
    ○ Дата, когда задача должна быть сдана
    ○ Email сотрудника, за которым закреплена эта задача
"""

task_f = Task.objects.filter(
    Q(status=StatusProject.NEW) &
    Q(priority=PriorityProject.MEDIUM)
)
#print(*task_f, sep="\n")

# for item in task_f:
#     print(item.title, item.status, item.priority, item.due_date, item.assigned.email, sep="\n")

"""14 Обновление статуса задачи
1. Напишите запрос, который поможет получить конкретную задачу
2. Обратитесь к полю статуса и обновите его на новое значение, например “pendingˮ. Сделайте это
через метод update().
"""
task_st = Task.objects.filter(title="Task 1")
task_st.update(status=StatusProject.PENDING)

#print(task_st)

"""15Получение задач через комбинацию условий
 Напишите запрос, который будет содержать в себе прохождение одной из комбинаций:
    ○ статус и приоритетность
    ○ прохождение несовпадения по тегу
2. Выведите название этих задач, проект и email разработчиков.
"""
task_f = Task.objects.filter(
    (Q(status=StatusProject.NEW) &  Q(priority=PriorityProject.MEDIUM))
    | ~Q(tags__title="Frontend")
)
# for item in task_f:
#     print(item.title, item.status, item.priority, item.due_date, item.assigned.email, sep="\n")
"""16 Обновление приоритета задач
1. Импортируйте модель Task.
2. Импортируйте F класс.
3. Обновите приоритет задач, которые должны быть выполнены в следующем месяце, на "Critical".
Используйте F-класс.
"""
from django.db.models import F

#task_cr = Task.objects.filter(due_date__month=F('created_at__month')+1).update(priority=PriorityProject.VERY_HIGH)

"""17Увеличение даты выполнения всех задач на неделю
1. Импортируйте модуль timedelta из библиотеки datetime.
2. Импортируйте модель Task.
3. Обновите все объекты задач по полю due_date на + 1 неделю. Используйте F-класс.
"""
# task_cr = Task.objects.update(due_date=F('due_date') + timedelta(weeks=1))
# print(task_cr)

"""18Фильтрация задач, у которых нет прикрепленного разработчика
1. Импортируйте модель Task.
2. Напишите запрос, который поможет профильтровать по lookups полю те задачи, у которых нет
назначенного разработчика.
3. Выведите название таких задач и название проекта для этих задач.
"""

task_user = Task.objects.filter(assigned__isnull=True)
# for item in task_user:
#     print(item.title, item.status, item.priority, item.due_date, sep="\n")

"""19 Получение задач
1. Импортируйте модель Task.
2. Напишите запрос, который поможет отфильтровать задачи через конкретный тэг.
    ○ Запрос должен быть написан с использованием lookups полей
    ○ Запрос должен начинаться с модели Task, через эту модель нужно получить доступ к
    конкретному тэгу.
3. Выведите информацию по каждой задаче:
    ○ Имя задачи
    ○ Статус задачи
    ○ Приоритет задачи
    ○ Имя проекта этой задачи
"""
task_tag = Task.objects.filter(tags__title="Backend")

# for item in task_tag:
#     print(item.title, item.status, item.priority, item.due_date, sep="\n")
#     print("-"*20)


"""20 Получение проектов
Необходимо получить все проекты, связанные с файлами, созданными в определенный период (последняя
неделя).
1. Импортируйте модели Project, ProjectFile.
2. Создайте переменную с датой периода создания файлов (от текущего дня 7 дней)
3. Напишите первый запрос, который поможет получить те файлы, которые должны быть больше, или
равны полученной дате по полю создания этого файла
4. Напишите запрос, который поможет получить только те проекты, у которых есть те файлы, что мы
получили предыдущим запросом.
5. Выведите информацию об этих проектах: имя проекта и дата создания.
"""

week_ago = timezone.now()-timedelta(weeks=1)

pr_file = ProjectFile.objects.filter(created_at__gte=week_ago)
pr_week_ag = Project.objects.filter(files__in=pr_file)
# for item in pr_week_ag:
#     print(item.title, item.created_at,  sep="\n")
#     print("-"*20)

"""21 Массовое обновление статуса задач
1. Импортируйте модель Task.
2. Напишите запрос, который отфильтрует задачи по определённому статусу (‘newʼ).
3. Для всех полученных задач обновите поле status на новое значение ‘in_progressʼ.
4. У модели вызовите метод, который позволит массово применить обновления.
5. Посмотрите результат, выведите поле статуса у всех задач.
"""

# tasks_new = (Task.objects.filter(status=StatusProject.NEW))
# for t in tasks_new:
#     t.status = StatusProject.IN_PROGRESS
# Task.objects.bulk_update(tasks_new,['status'])
#
# print(*Task.objects.all(), sep="\n")

"""22Массовое обновление даты выполнения задач
1. Импортируйте модель Task.
2. Импортируйте модуль timedelta из библиотеки datetime и F класс.
3. Получите список задач со статусом ‘in_progressʼ.
4. Для каждого полученного объекта измените дату для завершения задачи, увеличив её на 3 дня от
той даты, что в задаче указана.
5. У модели Task вызовите метод, который поможет массово обновить данные.
"""

# task_22 = Task.objects.filter(status=StatusProject.IN_PROGRESS)
# for ta in task_22:
#     ta.due_date = F('due_date')+timedelta(days=3)
# Task.objects.bulk_update(task_22, ['due_date'])

"""23Фильтрация проектов по дате создания и количеству файлов
1. Импортируйте класс Count для подсчёта кол-ва файлов.
2. Импортируйте модуль timezone из фреймворка django.
3. Импортируйте модель Project.
4. Создайте переменную в которой будет храниться искомая дата проекта, например “2023-07-07ˮ.
5. Напишите запрос, который будет фильтровать проекты по следующим параметрам:
    ○ Дата создания должна быть больше той даты, что мы получили ранее
    ○ Кол-во файлов для проекта должно быть больше, или равно переданному, например трём
"""


# day_search=timezone.datetime(2025,9,8).astimezone()
# number=1
# for project in Project.objects.all():
#     count_f=project.files.count()
#     if count_f >= number and (project.created_at>=day_search.date()):
#         print(project)

"""24Комбинированная фильтрация задач
1. Импортируйте модель Task.
2. Импортируйте класс Q и модуль datetime из фреймворка django
3. Импортируйте модуль timezone из Django и библиотеку calendar(базовая).
4. Напишите функцию, которая будет высчитывать конец месяца от текущей даты.
5. Напишите запрос, который будет фильтровать задачи по нескольким условиям:
    ○ Приоритет задачи или “Criticalˮ или “Urgentˮ
    ○ Дата, когда задача должна быть закрыта(due_date) - дата конца месяца с текущей даты
"""
# today=timezone.now()
#
# def days_for_month_end():
#     today = timezone.now()
#     amount_of_days = calendar.monthrange(today.year, today.month)[1]
#     date = datetime(
#         year=today.year,
#         month=today.month,
#         day=amount_of_days,
#     )
#     return date.astimezone()
# end_day=days_for_month_end()
#
# tasks_f=Task.objects.filter(Q(priority=PriorityProject.MEDIUM) | Q(priority=PriorityProject.LOW) , due_date__lte=end_day)
#
# print(tasks_f)

"""25Исключение задач с определенными статусами
1. Импортируйте модель Task.
2. Импортируйте класс Q.
3. Напишите запрос, который будет получать все задачи, кроме тех, что будут переданы в фильтр,
например: “pendingˮ и “closedˮ
"""
task_not = Task.objects.filter(~Q(status=StatusProject.PENDING) & ~Q(status=StatusProject.CLOSED))
#print(*task_not, sep="\n")

"""26 Обновление приоритета задач
1. Импортируйте модель Task.
2. Импортируйте F класс, модуль timezone из фреймворка Django, модуль datetime.
3. Создайте переменную, где будет храниться определённая дата (месяц назад относительно текущей
даты).
4. Напишите запрос, который будет получать все задачи из конкретного проекта, например “TIGERˮ,
которые были созданы месяц назад.
5. Обновите приоритетность таких задач на самую высокую.
"""

today = timezone.now()-timedelta(days=30)


"""4.1Проекты за текущий месяц
1. Импортируйте модель Project.
2. Импортируйте модуль timezone из django.
3. Напишите запрос, который выдаст только те проекты, которые были созданы в текущем
месяце (месяц брать от даты текущего дня).
4. Если есть хоть один проект - выведите информацию:
    ○ Название проекта
    ○ Полная дата его создания
"""

project_month=Project.objects.filter(created_at__month=timezone.now().month)
#print(projekt_month)

# if project_month:
#     n=1
#     for i in project_month:
#                 print(f"{n}. {i.title} - {i.created_at}.")
#                 n+=1

"""4.2Файлы проектов в день недели
1. Импортируйте модель ProjectFile.
2. Импортируйте класс ExtractWeekDay из django.
3. Напишите запрос, который будет получать список файлов за определённый день, например
понедельник:
    ○ Для выборки конкретного значения по полю даты создания используйте класс ExtractWeekDay.
    ○ Для упрощения работы с таким значением задайте для него новое, не заявленное в модели поле,
    например weekday.
    ○ Проведите фильтрацию по этому новому полю.
4. Если файлов не было найдено - выведите сообщение “Empty Dataˮ, если был найден хоть один файл -
выведите информацию о нём:
    ○ Название файла
    ○ Путь к файлу, где он сохранён
"""
from django.db.models.functions import ExtractWeekDay

week_days_project=ProjectFile.objects.annotate(weeksday= ExtractWeekDay('created_at')).filter(weeksday=5)

# if week_days_project:
#     n=1
#     for i in week_days_project:
#                 print(f"{n}. {i.name} - {i.created_at}.")
#                 n+=1

"""4.3 Общее количество проектов
1. Импортируйте модель Project.
2. Напишите запрос, который будет считать количество всех проектов, которые есть в базе данных.
3. Выведите количество всех проектов в консоль.
"""
print(Project.objects.all().count())

def total_project():
    return Project.objects.all().count()

"""4.4 Количество файлов для каждого проекта
1. Импортируйте модель Project.
2. Импортируйте класс Count из django.
3. Напишите запрос, который будет считать количество файлов для каждого проекта персонально.
4. Выведите информацию о количестве файлов для каждого проекта.
"""
def countsfiles_per_project():
    count_f=Project.objects.annotate(count_of_files=Count("files"))
    for i in count_f:
        print(f"{i.title} - {i.count_of_files}")
    #print(count_f[0].__dict__)

"""4.5 Среднее количество задач на каждом проекте
1. Импортируйте модель Project.
2. Импортируйте класс AVG из django.
3. Напишите запрос, который сможет для каждого проекта выведите среднее количество задач.
4. Выведите полученные данные.
"""

def project_avg_task():
    avg_tasks_in_pr=Project.objects.annotate(avg_t_p=Avg('tasks__id'))
    for item in avg_tasks_in_pr:
        print(f"{item.title} - {item.avg_t_p}")

"""4.6 Количество задач для каждого пользователя
1. Импортируйте модель User из django.
2. Импортируйте класс Count из django.
3. Напишите запрос, который получит из базы данных количество задач для каждого пользователя.
4. В запросе укажите, что хотим работать только с конкретными полями:
    ○ Username
    ○ Наше собственно созданное поле count_of_tasks
5. Выведите как результат никнейм разработчика и количество прикреплённых за ним задач.
"""

def count_user_in_task():
    count_users=User.objects.annotate(count_u_t=Count('tasks__id'))
    for item in count_users:
        print(f"{item.username} - {item.count_u_t}")

"""4.7 Сортировка задач по приоритету и дате выполнения
1. Импортируйте модель Task.
2. Напишите запрос, который сможет отсортировать все задачи по нескольким полям:
    ○ Приоритет задачи
    ○ Дата к которой задача должна быть выполнена
3. Выведите название задачи, приоритет и дату завершения.
"""

def sort_task():
    sorted_tasks=Task.objects.order_by('priority', 'due_date')
    for item in sorted_tasks:
        print(f"{item.title}:\t\t\t{item.priority}\t\t - {item.due_date}.")

"""4.8 Сортировка пользователей по количеству задач
1. Импортируйте модель User из django.
2. Напишите запрос, который будет сортировать всех пользователей исходя из того,
как много у каждого задач.
3. Отсортируйте от самого загруженного сотрудника, к самому свободному по задачам.
4. Конкретизируйте запрос таким образом, чтобы в него включались только поля:
    ○ Username
    ○ Count_of_tasks
5. Выведите все данные в консоль.
"""

def sort_count_user_in_task():
    sorted_count_users=User.objects.annotate(count_u_t=Count('tasks__id')).order_by('-count_u_t')
    for item in sorted_count_users:
        print(f"{item.username} - {item.count_u_t}")

"""4.9 Пагинация для задач
1. Импортируйте модель Task.
2. Импортируйте класс Paginator.
3. Напишите запрос для получения всех задач.
4. Реализуйте пагинацию для того, чтобы в рамках одной страницы отображалось ровно 10 задач,
не более.
5. Выведите данные об этих 10-ти задачах:
    ○ Название
    ○ Статус
    ○ Приоритетность
    ○ Username разработчика
"""

def paginator_task():
    pag_task=Task.objects.all()
    start,stop,step = 0,10,10
    while stop < len(pag_task):
        part=pag_task[start:stop]
        for item in part:
            print(f"{item.title} : {item.status}, {item.priority}, {item.username}")
        start,stop =stop,stop+step





