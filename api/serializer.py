

from course.models import Course
from student.models import Student
from rest_framework import serializers
from teacher.models import Teacher
from classes.models import Class_Period


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Period
        fields = "__all__"

