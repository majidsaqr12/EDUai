# Generated by Django 5.1.2 on 2024-11-15 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_arabic_created_at_biology_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Arabic',
        ),
        migrations.DeleteModel(
            name='Biology',
        ),
        migrations.DeleteModel(
            name='Chemistry',
        ),
        migrations.DeleteModel(
            name='English',
        ),
        migrations.DeleteModel(
            name='French',
        ),
        migrations.DeleteModel(
            name='Geography',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Mathematics',
        ),
        migrations.DeleteModel(
            name='Physics',
        ),
        migrations.DeleteModel(
            name='Science',
        ),
    ]
