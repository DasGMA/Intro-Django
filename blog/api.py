from rest_framework import serializers, viewsets
from .models import PersonalBlog

class PersonalBlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalBlog
        fields = ('title', 'body')
    
    def create(self, validated_data):
        user = self.context['request'].user
        blog = PersonalBlog.objects.create(user = user, **validated_data)
        return blog

class PersonalBlogViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBlogSerializer
    queryset = PersonalBlog.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalBlog.objects.none()
        else:
            return PersonalBlog.objects.filter(user=user)