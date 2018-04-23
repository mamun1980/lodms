# Generated by Django 2.0.2 on 2018-04-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_no', models.CharField(max_length=50, unique=True)),
                ('details', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'permissions': (('can_view_case', 'Can view case'),),
            },
        ),
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('priority', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_no', models.CharField(max_length=100, unique=True)),
                ('docs_location', models.CharField(blank=True, max_length=200, null=True)),
                ('case', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_file', to='testapp.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('room_details', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='case_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='testapp.CaseType'),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='testapp.CaseStatus'),
        ),
        migrations.CreateModel(
            name='FileDocs',
            fields=[
            ],
            options={
                'verbose_name': 'File Doc',
                'verbose_name_plural': 'File Docs',
                'proxy': True,
                'indexes': [],
            },
            bases=('testapp.file',),
        ),
    ]
