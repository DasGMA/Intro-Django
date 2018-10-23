from rest_framework import serializers, viewsets
from .models import PersonalBlog

class PersonalBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalBlog
        fields = ('title', 'body')

class PersonalBlogViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBlogSerializer
    queryset = PersonalBlog.objects.all()