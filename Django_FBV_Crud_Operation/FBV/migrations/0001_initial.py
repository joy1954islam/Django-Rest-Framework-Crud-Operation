# Generated by Django 3.1.3 on 2020-11-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200, verbose_name='Student ID')),
                ('student_age', models.IntegerField(verbose_name='Student Age')),
                ('student_name', models.CharField(max_length=150, verbose_name='Student Name')),
                ('student_email', models.EmailField(max_length=254, verbose_name='Student Email')),
                ('student_amount', models.FloatField(verbose_name='Student Amount')),
                ('student_address', models.TextField(verbose_name='Student Address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
