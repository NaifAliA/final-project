# Generated by Django 3.1.6 on 2021-02-24 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteesCharis',
            fields=[
                ('id_committees_charis', models.AutoField(primary_key=True, serialize=False)),
                ('name_committees_charis', models.CharField(blank=True, max_length=45, null=True)),
                ('passwords', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'committees_charis',
                'managed': False,
            },
        ),
    ]
