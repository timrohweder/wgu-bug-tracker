# Generated by Django 3.0.1 on 2020-05-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0004_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('Deferred', 'Deferred'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='deferred', max_length=20),
        ),
    ]