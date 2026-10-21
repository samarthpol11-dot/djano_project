from django.conf import settings
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Question(models.Model):
    lesson = models.ForeignKey(Lesson, related_name="questions", on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    grade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="exam_submissions",
        on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(Lesson, related_name="submissions", on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    total_score = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} — {self.lesson} ({self.score}/{self.total_score})"
