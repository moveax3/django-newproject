# Generated by Django 2.0 on 2018-01-05 12:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('targets', '0004_auto_20180105_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('Новая', 'Новая'), ('В работе', 'В работе'), ('Готово', 'Готово')], default='Новая', max_length=100, no_check_for_status=True)),
                ('status_working_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when={'В работе'})),
                ('status_complete_at', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when={'Готово'})),
                ('title', models.CharField(max_length=128, verbose_name='Задача')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_blocked', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tasks.Task', verbose_name='Блокируется')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tasks.Task', verbose_name='Родительская задача')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='targets.Target', verbose_name='Цель')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
