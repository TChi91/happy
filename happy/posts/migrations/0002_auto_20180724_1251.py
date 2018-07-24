# Generated by Django 2.0.7 on 2018-07-24 12:51

from django.db import migrations, models
import posts.models
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mediafile',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.content_file_name, validators=[posts.validators.validate_file_extension_and_size]),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]
