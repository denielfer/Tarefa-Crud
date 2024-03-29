# Generated by Django 5.0.1 on 2024-01-18 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descrição', models.TextField()),
                ('data', models.DateField()),
                ('status', models.CharField(choices=[('p', 'Pendente'), ('e', 'Executando'), ('c', 'Concluída')], default='p', max_length=2)),
            ],
        ),
    ]
