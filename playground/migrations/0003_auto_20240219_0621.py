# Generated by Django 2.2.3 on 2024-02-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_auto_20240218_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.AlterField(
            model_name='signupdata',
            name='user_id',
            field=models.CharField(max_length=500),
        ),
    ]
