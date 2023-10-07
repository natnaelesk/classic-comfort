# Generated by Django 3.2.12 on 2023-09-05 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='shose/static/shose/images')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('trend', models.BooleanField()),
                ('price', models.IntegerField()),
                ('det', models.CharField(max_length=150)),
                ('like', models.BooleanField()),
                ('collection', models.CharField(max_length=50)),
                ('photo_extra_1', models.ImageField(upload_to='shose/static/shose/images')),
                ('photo_extra_2', models.ImageField(upload_to='shose/static/shose/images')),
                ('photo_extra_3', models.ImageField(upload_to='shose/static/shose/images')),
                ('photo_extra_4', models.ImageField(upload_to='shose/static/shose/images')),
            ],
        ),
    ]
