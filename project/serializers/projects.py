from rest_framework.serializers import ModelSerializer
from project.models import Project, Task

"""4.10 Первый сериализатор для проектов
1. Установите модуль djangorestframework.
2. Добавить этот модуль в файл requirements.txt.
3. Добавить этот модуль в список установленных приложений в файле settings.py.
4. Создать новый пакет serializers, в котором создать первый файл - projects
5. Импортируйте класс ModelSerializer.
6. Напишите первый сериализатор, который будет обрабатывать поля id и name для проекта,
выдавая общую базу для вывода всех проектов.
"""

class ProjectsSerializers(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title']

"""4.11 Первое представление для отображения списка всех проектов
1. Импортируйте ранее написанный сериализатор в файл, где будет реализовываться первое
представление.
2. Импортируйте дополнительные методы и классы:
○ Request из rest_framework (для типизации объекта запроса)
○ JsonResponse из django (для возврата и типизации ответов)
○ Status из rest_framework (для указания статусов ответов)
○ Api_view из rest_framework.decorators (для конкретики обрабатываемых методов)
○ Модель Project (для запросов к таблице проектов в базе данных)
3. Напишите функцию, которая будет обрабатывать GET запросы для получения списка всех проектов
из Базы данных.
4. Зарегистрировать эту функцию в списке эндпоинтов в файле urls.py
5. Проверьте работу готового эндпоинта.
"""

"""4.12Сериализатор для модели задач (Task)
1. Создайте новый файл для сериализаторов задач.
2. Импортируйте класс ModelSerializer.
3. Напишите сериализатор для модели Task с полями id, name, status, priority для получения общей
информации о задачах.
"""
class TasksListSerializers(ModelSerializer):
    class Meta:
        model=Task
        fields = [
            'id', 'title', 'status', 'priority'
        ]











