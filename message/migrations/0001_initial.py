# Generated by Django 4.2.2 on 2024-07-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ('id',),
                'permissions': [('can_view_messages', 'can view messages')],
            },
        ),
    ]
