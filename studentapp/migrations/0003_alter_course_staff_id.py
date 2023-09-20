# Generated by Django 4.0.3 on 2022-04-12 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_alter_course_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]