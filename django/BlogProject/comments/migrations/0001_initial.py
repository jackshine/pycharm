# Generated by Django 2.0.1 on 2018-01-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('pdid', models.IntegerField()),
                ('comment', models.CharField(max_length=200, verbose_name='评论内容')),
                ('commenttime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('flag', models.IntegerField()),
                ('nickname', models.CharField(max_length=50, null=True, verbose_name='昵称')),
            ],
        ),
    ]
