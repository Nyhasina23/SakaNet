# Generated by Django 3.2.5 on 2021-09-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sakanet', '0013_discussion_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='liste_message',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='utilisateur',
        ),
        migrations.AlterField(
            model_name='message',
            name='discussion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='utilisateur',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
