# Generated by Django 5.0.7 on 2024-07-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_managers_user_full_name_user_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tin_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]