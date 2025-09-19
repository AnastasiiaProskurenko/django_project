from rest_framework.serializers import ModelSerializer
from project.models import Tag


"""4.14Сериализатор на получение всех тегов
1. Создайте новый файл tags для хранение сериализаторов.
2. Импортируйте класс ModelSerializer.
3. Напишите сериализатор для получения всех тегов.
"""

class AllTagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','title']