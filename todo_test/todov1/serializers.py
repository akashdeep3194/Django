from rest_framework.serializers import ModelSerializer
from todov1.models.todo_model import Todo


class TodosSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
