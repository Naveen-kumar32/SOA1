# Generated by Django 4.2.2 on 2023-06-14 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testcase', '0002_alter_testdata_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdata',
            options={'managed': True},
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='InvoiceAmountcreditnote',
            new_name='Invamtcreditnote',
        ),
        migrations.RenameField(
            model_name='testdata',
            old_name='InvAmount',
            new_name='Invoiceamount',
        ),
    ]