
from rest_framework import serializer 
from models import Post
    
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= post
        fields= '__all__'