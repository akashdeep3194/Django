from rest_framework.serializers import ModelSerializer
from todov1.models.models import Todos

class TodosSerializer(ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'
