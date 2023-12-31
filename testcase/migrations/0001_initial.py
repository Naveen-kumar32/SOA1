# Generated by Django 4.2.2 on 2023-06-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testdata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('SlNo', models.IntegerField()),
                ('Branch', models.CharField(max_length=100)),
                ('PONo', models.CharField(max_length=100)),
                ('POIssuedby', models.CharField(max_length=100)),
                ('ClientName', models.CharField(max_length=100)),
                ('ClientGroup', models.CharField(max_length=100)),
                ('Shipname', models.CharField(max_length=100)),
                ('POAmount', models.CharField(max_length=100)),
                ('InvoiceNo', models.CharField(max_length=100)),
                ('InvoiceDate', models.CharField(max_length=100)),
                ('Duedate', models.CharField(max_length=100)),
                ('Freight', models.CharField(max_length=100)),
                ('InvAmount', models.CharField(max_length=100)),
                ('SgdValue', models.CharField(max_length=100)),
                ('GstScope', models.CharField(max_length=100)),
                ('currency1', models.CharField(max_length=100)),
                ('InvoiceAmountcreditnote', models.CharField(max_length=100)),
                ('standardrated', models.CharField(max_length=100)),
                ('GstPaid', models.CharField(max_length=100)),
                ('paymentstatus', models.CharField(max_length=100)),
                ('newstatus', models.CharField(max_length=100)),
                ('transactioncode', models.CharField(max_length=100)),
                ('areceiveddate', models.CharField(max_length=100)),
                ('a2ndpaymentReceiveddate', models.CharField(max_length=100)),
                ('receivedamount', models.CharField(max_length=100)),
                ('receivedamountCurrency', models.CharField(max_length=100)),
                ('dc', models.CharField(max_length=100)),
                ('discountcurrency', models.CharField(max_length=100)),
                ('Invcurrency', models.CharField(max_length=100)),
                ('outstandingBalance', models.CharField(max_length=100)),
                ('supt', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'test1',
                'managed': False,
            },
        ),
    ]
