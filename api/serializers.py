
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.  parsers    import JSONParser   ?
from blog.models import Blog

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ' __all__ '

class BlogModel():
    def __init__(self, title, text):
        self.title = title
        self.text = text


class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=55)
    text = serializers.CharField(max_length=400)


def encode():
    model = BlogModel('anton', 'beautiful')
    model_sr = BlogSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)



def decode():
    stream = io.BytesIO(b'{"title":"anton", "text": "beautiful"}')
    data = JSONParser().parse(stream)
    serializer = BlogSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)