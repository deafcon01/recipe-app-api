from operator import imod
from rest_framework import serializers
from core.models import Tag

class TagSerializer(serializers.ModelSerializer):
    """Serializers for Tag Object"""
    class Meta:
        model=Tag
        fields=('id','name')
        read_only_fields=('id',)
