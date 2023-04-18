# Generated by Django 4.1.2 on 2022-10-18 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edl',
            name='edl_type',
            field=models.CharField(choices=[('url', 'URL'), ('domain', 'Domain'), ('ip_address', 'IP Address')], max_length=20),
        ),
        migrations.CreateModel(
            name='EdlEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_value', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('valid_until', models.DateTimeField(default=None)),
                ('edl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edl.edl')),
            ],
        ),
    ]