# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onfido', '0010_convert_raw_fields_to_jsonb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='status',
            field=models.CharField(blank=True, choices=[(b'Check', ((b'in_progress', b'In progress'), (b'awaiting_applicant', b'Awaiting applicant'), (b'complete', b'Complete'), (b'withdrawn', b'Withdrawn'), (b'paused', b'Paused'), (b'reopened', b'Reopened'))), (b'Report', ((b'awaiting_data', b'Awaiting data'), (b'awaiting_approval', b'Awaiting approval'), (b'complete', b'Complete'), (b'withdrawn', b'Withdrawn'), (b'paused', b'Paused'), (b'cancelled', b'Cancelled')))], db_index=True, help_text='The current state of the check / report (from API).', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(blank=True, choices=[(b'Check', ((b'in_progress', b'In progress'), (b'awaiting_applicant', b'Awaiting applicant'), (b'complete', b'Complete'), (b'withdrawn', b'Withdrawn'), (b'paused', b'Paused'), (b'reopened', b'Reopened'))), (b'Report', ((b'awaiting_data', b'Awaiting data'), (b'awaiting_approval', b'Awaiting approval'), (b'complete', b'Complete'), (b'withdrawn', b'Withdrawn'), (b'paused', b'Paused'), (b'cancelled', b'Cancelled')))], db_index=True, help_text='The current state of the check / report (from API).', max_length=20, null=True),
        ),
    ]
