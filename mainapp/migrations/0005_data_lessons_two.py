# Generated by Django 3.2.15 on 2022-09-05 15:40

from django.db import migrations


def forwards_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model('mainapp', 'Lesson')
    Courses = apps.get_model('mainapp', 'Courses')
    # Create model's objects
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=2),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=3),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=4),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=5),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=6),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=7),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=1,
        title='Lesson 1',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=2,
        title='Lesson 2',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=3,
        title='Lesson 3',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=4,
        title='Lesson 4',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=5,
        title='Lesson 5',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=6,
        title='Lesson 6',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=7,
        title='Lesson 7',
        description='Описание урока',
    )
    Lesson.objects.create(
        course=Courses.objects.get(pk=8),
        num=8,
        title='Lesson 8',
        description='Описание урока',
    )


def reverse_func(apps, schema_editor):
    # Get model
    Lesson = apps.get_model('mainapp', 'Lesson')
    # Delete objects
    Lesson.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_data_lessons'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]