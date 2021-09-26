# Generated by Django 3.2.6 on 2021-09-19 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0002_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='title',
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='Forum.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]