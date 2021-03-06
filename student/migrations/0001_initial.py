# Generated by Django 3.0.8 on 2020-07-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('std_class', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
        ),
    ]
