# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 06:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_auto_20160128_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='wallet_debit_record2wallet_credit_record',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet'),
        ),
    ]
