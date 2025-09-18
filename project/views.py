from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from project.models import Project,Task,ProjectFile,Tag
from project.serializers.projects import ProjectsSerializers, TasksListSerializers
from project.serializers.tags import AllTagsSerializer

@api_view(['GET'])
def list_projects(request):
    projects = Project.objects.all()
    serializer = ProjectsSerializers(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

"""4.13Отображение для получения списка всех задач
1. Импортируйте модель Task
2. Импортируйте написанный ранее сериализатор AllTasksSerializer
3. Напишите отображение, которое будет выводить JSON данные о всех задачах из базы данных:
    ○ Если при отправке запроса не передавать конкретный проект - выводить все задачи
    ○ Если был указан конкретный проект, например “TIGERˮ - выводить только те задачи, которые
принадлежат этому проекту
"""

@api_view(['GET'])
def all_or_tasks_details(request, name=''):
    if not name:
        tasks = Task.objects.all()
        serializer = TasksListSerializers(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:

        task=Task.objects.filter(project__title=name)
        if task.exists():
            serializer = TasksListSerializers(task, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_204_NO_CONTENT)


"""4.15Отображение для получения всех тегов
1. Импортируйте модель Tag.
2. Импортируйте сериализатор AllTagsSerializer.
3. Напишите функцию, которая будет отображать список всех тегов в формате JSON.
"""

@api_view(['GET'])
def all_tags(request):
    tags = Tag.objects.all()
    if tags.exists():
        serializer = AllTagsSerializer(tags, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response([],status=status.HTTP_204_NO_CONTENT)

"""4.16Отображение для получения тега по id
1. Напишите отображение с принимаемым аргументом tag_id.
2. Проверьте существование такого тега и если он есть - вернуть информацию о нём.
"""

@api_view(['GET'])
def tag_details(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if tag:
        serializer = AllTagsSerializer(tag)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response([],status=status.HTTP_204_NO_CONTENT)

"""4.17
Отображение для обновления информации о теге
1. Поставьте в декоратор api_view() метод для обновления ‘PUTʼ.
2. Напишите запрос, который будет получать конкретный тег по id:
    ○ Реализуйте проверку на получение объекта тега. Если объекта нет - выведите
соответствующее сообщение.
3. Напишите отображение, которое будет принимать из тела запроса новые данные:
    ○ Реализуйте проверку валидации полученных данных.
4. Обновите полученный объект тега новыми данными и сохраните его.
"""
@api_view(['PUT'])
def tag_update(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    if tag:
        serializer = AllTagsSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response([],status=status.HTTP_204_NO_CONTENT)



