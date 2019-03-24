# Generated by Django 2.1.7 on 2019-03-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('effect', models.TextField()),
                ('level', models.IntegerField()),
                ('type', models.IntegerField()),
                ('parents', models.ManyToManyField(related_name='children', to='perks.Perk')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='perk',
            name='trees',
            field=models.ManyToManyField(related_name='perks', to='perks.Tree'),
        ),
    ]
