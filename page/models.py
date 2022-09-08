from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(max_length=1000)
    start =  models.DateTimeField(auto_now_add=True)
    proposed_finish_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=(('pending', 'PENDING'),('ongoing','ONGOING'),('finished','COMPLETED')))

    def __str__(self) -> str:
        return self.name 

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='task' )
    description = models.TextField(max_length=1000)
    start =  models.DateTimeField(auto_now_add=True)
    proposed_finish_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=(('pending', 'PENDING'),('ongoing','ONGOING'), ('finished','COMPLETED')))
    assigned_to = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



