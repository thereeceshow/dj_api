from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'age', 'courses']


class InstructorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Instructor
    fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'name', 'instructor']



class GradeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Grade
    fields = ['id', 'score', 'course', 'student']


    