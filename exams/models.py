from django.db import models
from  ckeditor.fields import RichTextField
class QuestionTable(models.Model):
    questionID = models.AutoField(primary_key=True)
    Question = RichTextField()
    OptionA = RichTextField()
    OptionB = RichTextField()
    OptionC = RichTextField()
    OptionD = RichTextField()
    RightOption = models.CharField(max_length=1, choices=[
        ('A', 'Option A'), ('B', 'Option B'), ('C', 'Option C'), ('D', 'Option D')
    ])
    Marks = models.IntegerField()
    Remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Q{self.questionID}: {self.Question[:50]}"

class ExamTable(models.Model):
    exam_id = models.AutoField(primary_key=True)
    examName = models.CharField(max_length=255)
    examduration = models.IntegerField(help_text="Duration in minutes")
    cource_id = models.CharField(max_length=100)
    total_no_questions = models.IntegerField()
    # questionarray = models.JSONField(help_text="List of Question IDs")  # We'll store list of question IDs in JSON
    questionarray = models.ManyToManyField(QuestionTable, help_text="Select questions for this exam")
    passmarks = models.IntegerField()
    exam_log = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.examName
