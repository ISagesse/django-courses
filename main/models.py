from django.db import models

# Create your models here.

class CourseManage(models.Manager):
    def course_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 5:
            errors['name'] = 'The course name should be more than 5 character'

        if len(post_data['description']) < 15:
            errors['description'] = 'The course description should be more than 15 character'
        
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManage()