# Generated by Django 4.1.7 on 2023-03-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0004_conversation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='conversationmessage',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
