# Generated by Django 2.2.7 on 2019-11-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]