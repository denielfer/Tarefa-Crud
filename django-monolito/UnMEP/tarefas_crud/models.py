from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descrição = models.TextField()
    data = models.DateField()
    class status_choice(models.TextChoices):
        Pendente = 'p'
        Executando = 'e'
        Concluída = 'c'
    status = models.CharField(
        max_length=2,
        choices=status_choice,
        default=status_choice.Pendente, #por default a tarefa entra como pendente
    )