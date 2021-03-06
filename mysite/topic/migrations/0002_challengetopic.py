# Generated by Django 2.0.4 on 2018-04-08 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('challenge', models.ManyToManyField(to='challenge.Challenge')),
                ('topic', models.ManyToManyField(to='topic.Topic')),
            ],
        ),
    ]
