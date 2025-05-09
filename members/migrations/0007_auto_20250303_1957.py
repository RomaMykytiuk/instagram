# Generated by Django 5.1.2 on 2025-03-03 17:31

from django.db import migrations

def populate_username(apps,shema_editor):
    User = apps.get_model("members", "User")
    for user in User.objects.all():
        if not user.username:
            base_username = user.email.split("@")[0]
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            user.username=username
            user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_user_username'),
    ]

    operations = [
        migrations.RunPython(populate_username),
    ]
