from .models import Post,Topic
from rest_framework.serializers import ModelSerializer

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields =["id", "content", "image","flags","seeds","creator","active","created","updated","topic"]

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields =["id", "name"]