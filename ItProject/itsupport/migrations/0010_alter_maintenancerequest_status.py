# Generated by Django 5.0.7 on 2024-07-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsupport', '0009_alter_maintenancerequest_status_ithelp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='status',
            field=models.CharField(choices=[('مفتوح', 'sendit'), ('تحت الإجراء', 'pending'), ('منتهي', 'completed')], default='مفتوح', max_length=20),
        ),
    ]
