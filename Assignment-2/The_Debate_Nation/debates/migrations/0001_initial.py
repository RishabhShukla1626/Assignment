# Generated by Django 4.1.3 on 2022-11-27 17:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debates',
            fields=[
                ('debate_title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('vote_total', models.IntegerField(default=0, null=True)),
                ('vote_ratio', models.IntegerField(default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('debate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debates.debates')),
            ],
        ),
        migrations.CreateModel(
            name='Arguments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField()),
                ('opinion', models.CharField(choices=[('AGAINST', 'Against'), ('SUPPORT', 'Support')], default='AGAINST', max_length=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('debate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='debates.debates')),
            ],
        ),
    ]
