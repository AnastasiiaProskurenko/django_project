from rest_framework.serializers import ModelSerializer
from project.models import Project

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
        name = Project
        fields = ['id','title']
