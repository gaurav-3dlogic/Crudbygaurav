# Generated by Django 3.0.7 on 2022-04-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gaurav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=100)),
                ('upassword', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'gaurav',
            },
        ),
    ]