# Generated by Django 4.0 on 2022-01-12 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Хэштег',
                'verbose_name_plural': 'Хэштеги',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Категория новости',
                'verbose_name_plural': 'Категории новостей',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=4096)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media/images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.newscategory')),
                ('hash_tags', models.ManyToManyField(to='News.HashTags')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
