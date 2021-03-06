# Generated by Django 2.0.2 on 2018-04-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'applicant',
                'verbose_name_plural': 'applicantes',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_no', models.CharField(max_length=100, unique=True, verbose_name='case_no')),
                ('details', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'case',
                'verbose_name_plural': 'cases',
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
            name='Defendent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='defendent_case', to='casems.Case')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='case_defendent', to='contacts.Person')),
            ],
            options={
                'verbose_name': 'defendant',
                'verbose_name_plural': 'defendants',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_no', models.CharField(max_length=100, unique=True)),
                ('docs_location', models.CharField(blank=True, max_length=200, null=True)),
                ('case', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='case_file', to='casems.Case')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_no', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rake',
            fields=[
                ('rake_no', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_no', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('room_name', models.CharField(blank=True, max_length=100, null=True)),
                ('room_details', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('shelf_no', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('shelf_details', models.TextField(blank=True, max_length=200, null=True)),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='casems.Room')),
            ],
        ),
        migrations.AddField(
            model_name='rake',
            name='shelf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='casems.Shelf'),
        ),
        migrations.AddField(
            model_name='folder',
            name='rake',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='casems.Rake'),
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casems.Folder'),
        ),
        migrations.AddField(
            model_name='file',
            name='rake',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casems.Rake'),
        ),
        migrations.AddField(
            model_name='case',
            name='case_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casems.CaseType'),
        ),
        migrations.AddField(
            model_name='case',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='casems.CaseStatus'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='applicant_case', to='casems.Case'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='case_applicant', to='contacts.Person'),
        ),
    ]
