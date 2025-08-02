from django.db import models
import os

def essay_upload_path(instance, filename):
    return f"essays/student_{instance.essay.student_id}/{filename}"

class Essay(models.Model):
    student_id = models.IntegerField()
    college_name = models.CharField(max_length=255)
    question_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.college_name} - {self.question_title}"

class EssayVersion(models.Model):
    essay = models.ForeignKey(Essay, related_name='versions', on_delete=models.CASCADE)
    content = models.FileField(upload_to=essay_upload_path)
    scorecard = models.JSONField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    