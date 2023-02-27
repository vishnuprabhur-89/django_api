# Generated by Django 4.1.7 on 2023-02-27 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_field_sum_subject_total_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rollNo',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='computer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='english',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='maths',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='science',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='social',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='studentRollNo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
