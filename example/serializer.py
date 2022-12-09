from rest_framework import serializers
from .models import Blog

from .models import LANGUAGE_CHOICES


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=30)
    author = serializers.CharField(required=False, allow_blank=True, max_length=30)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100, style={'base_template': 'textarea.html'})
    is_published = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get('description', instance.description)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'created', 'author', 'description', 'is_published', 'language']