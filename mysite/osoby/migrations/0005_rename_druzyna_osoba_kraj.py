# Generated by Django 4.1.3 on 2022-11-23 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osoby', '0004_osoba_wlasciciel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='osoba',
            old_name='druzyna',
            new_name='kraj',
        ),
    ]
