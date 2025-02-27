# Generated by Django 5.1.3 on 2025-02-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('ALIADO', 'Aliado'), ('INIMIGO', 'Inimigo')], max_length=7)),
                ('pv', models.IntegerField()),
                ('forca', models.IntegerField()),
                ('magia', models.IntegerField()),
                ('resistencia', models.IntegerField()),
                ('agilidade', models.IntegerField()),
                ('sorte', models.IntegerField()),
                ('defesa', models.IntegerField()),
                ('armadura', models.IntegerField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='personagens/')),
            ],
        ),
    ]
