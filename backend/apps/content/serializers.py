from rest_framework import serializers
from .models import ContentDocument,ContentVersion
class ContentVersionSerializer(serializers.ModelSerializer):
 class Meta: model=ContentVersion; fields='__all__'
class ContentDocumentSerializer(serializers.ModelSerializer):
 versions=ContentVersionSerializer(many=True,read_only=True)
 class Meta: model=ContentDocument; fields='__all__'; read_only_fields=['author','version']
