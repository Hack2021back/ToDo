from rest_framework.serializers import (
    ModelSerializer,
    # HyperlinkedIdentityField,
)
from to_do_app.models import ToDoList

class ToDoListAllSerialzer(ModelSerializer):

    class Meta:
        model = ToDoList
        fields = [
            "id",
            "task",
            "description",
            "start_data",
            "end_data",
            "start_time",
            "end_time",
            "priority",
        ]


