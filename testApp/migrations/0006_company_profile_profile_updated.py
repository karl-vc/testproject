# Generated by Django 2.2.4 on 2020-02-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0005_auto_20200207_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_profile',
            name='profile_updated',
            field=models.BooleanField(default=False),
        ),
    ]