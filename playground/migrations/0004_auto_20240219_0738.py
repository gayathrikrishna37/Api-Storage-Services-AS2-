# Generated by Django 2.2.3 on 2024-02-19 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0003_auto_20240219_0621'),
    ]

    operations = [
        migrations.CreateModel(
            name='AS2_bucket_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket_name', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField()),
                ('updation_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AS2_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.RemoveField(
            model_name='signupdata',
            name='user_id',
        ),
        migrations.AddField(
            model_name='as2_bucket_db',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.DataModel'),
        ),
    ]
