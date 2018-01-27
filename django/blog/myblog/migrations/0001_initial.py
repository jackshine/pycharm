# Generated by Django 2.0.1 on 2018-01-27 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='标题')),
                ('body', models.TextField(verbose_name='标题内容')),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField(blank=True)),
                ('excerpt', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别')),
                ('regtime', models.DateTimeField(verbose_name='注册时间')),
                ('delflag', models.IntegerField(choices=[(0, '普通用户'), (1, '高级用户')], default=1, verbose_name='用户类型标记')),
            ],
        ),
        migrations.AddField(
            model_name='daily',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.UserInfo'),
        ),
        migrations.AddField(
            model_name='daily',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Category'),
        ),
        migrations.AddField(
            model_name='daily',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myblog.Tag'),
        ),
    ]
