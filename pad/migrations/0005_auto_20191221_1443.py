# Generated by Django 2.0.2 on 2019-12-21 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pad', '0004_huancun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='duizhao',
            name='更新时间',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='shujuku',
            name='买家',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shujuku',
            name='价格',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='shujuku',
            name='已卖',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
