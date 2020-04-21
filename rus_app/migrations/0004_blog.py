# Generated by Django 2.2.12 on 2020-04-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rus_app', '0003_gallery_show_in_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(blank=True, default=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(blank=True, max_length=500)),
                ('picture', models.ImageField(upload_to='blog')),
                ('preview_text', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('show_on_main_page', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
