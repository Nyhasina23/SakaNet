# Generated by Django 3.2.4 on 2021-07-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sakanet', '0005_alter_message_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sakanet.utilisateur'),
        ),
    ]
