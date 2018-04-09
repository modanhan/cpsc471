# Generated by Django 2.0.4 on 2018-04-09 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('Language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]