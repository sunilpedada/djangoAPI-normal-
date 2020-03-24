# Generated by Django 2.2.7 on 2020-03-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeesDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('eaddress', models.TextField()),
                ('ephone_number', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]