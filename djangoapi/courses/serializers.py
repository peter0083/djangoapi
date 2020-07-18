from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer): # serializers.HyperLinkedModelSerializer is the superclass
    class Meta: # a class container for metadata
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')