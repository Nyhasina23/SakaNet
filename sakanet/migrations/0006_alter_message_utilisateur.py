# Generated by Django 3.2.5 on 2021-08-14 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sakanet', '0005_alter_message_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='utilisateur',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]