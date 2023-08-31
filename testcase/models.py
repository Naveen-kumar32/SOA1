from django.db import models




class SOA(models.Model):    

    id	= models.IntegerField(primary_key=True)
    Branch	= models.CharField(max_length=100)
    PONo	= models.CharField(max_length=100)
    POIssuedby	= models.CharField(max_length=100)
    ClientName	= models.CharField(max_length=100)
    ClientGroup	= models.CharField(max_length=100)
    Shipname	= models.CharField(max_length=100)
    POAmount	= models.CharField(max_length=100)
    InvoiceNo	= models.CharField(max_length=100)
    InvoiceDate	= models.CharField(max_length=100)
    Duedate	= models.CharField(max_length=100)
    Freight	= models.CharField(max_length=100)
    Invoiceamount   = models.CharField(max_length=100)
    SgdValue	= models.CharField(max_length=100)
    GstScope	= models.CharField(max_length=100)
    currency1	= models.CharField(max_length=100) 
    Invamtcreditnote	= models.CharField(max_length=100)
    standardrated	= models.CharField(max_length=100)
    GstPaid	= models.CharField(max_length=100)
    paymentstatus	= models.CharField(max_length=100)
    newstatus	= models.CharField(max_length=100)
    transactioncode	= models.CharField(max_length=100)
    areceiveddate	= models.CharField(max_length=100)
    a2ndpaymentReceiveddate	= models.CharField(max_length=100)
    receivedamount	= models.CharField(max_length=100)
    receivedamountCurrency	= models.CharField(max_length=100)
    dc	= models.CharField(max_length=100)
    discountcurrency	= models.CharField(max_length=100)
    Invcurrency	= models.CharField(max_length=100)
    outstandingBalance	= models.CharField(max_length=100)
    supt = models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'final'
