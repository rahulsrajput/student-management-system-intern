# Generated by Django 4.1 on 2022-10-04 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstaffs',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='notificationstaffs',
            name='stafff_id',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='studentresult',
            name='subject_id',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.DeleteModel(
            name='FeedBackStaffs',
        ),
        migrations.DeleteModel(
            name='FeedBackStudent',
        ),
        migrations.DeleteModel(
            name='NotificationStaffs',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
        migrations.DeleteModel(
            name='StudentResult',
        ),
    ]
