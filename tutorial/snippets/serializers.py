from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Author


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
	model = Author
        fields = ('id','first_name','last_name','email')

