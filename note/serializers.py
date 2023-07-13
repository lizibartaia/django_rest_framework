from rest_framework import serializers
from django.contrib.auth.models import User
from note.models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password"]


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Note
        fields = ["id","title","body","slug","user"]