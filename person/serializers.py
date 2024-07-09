from rest_framework import serializers
from rest_framework.response import Response

from .models import Person


class PoetSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# from rest_framework import serializers
# from rest_framework.response import Response
#
# from .models import Person
#
#
# class PoetSerializers(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     class Meta:
#         model = Person
#         fields = "__all__"
#
