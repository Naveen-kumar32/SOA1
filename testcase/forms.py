from django import forms
from .models import SOA 

# from django.core.validators import RegexValidator
# from django.contrib.admin import widgets


class SOAForm(forms.ModelForm):   
    class Meta:
        model = SOA

        # fields = ['ID','Branch','PONo','POIssuedby','ClientName','ClientGroup','Shipname','POAmount','InvoiceNo','InvoiceDate','Duedate','Freight','InvAmount','SGDValue','GSTScope','Currency1','InvoiceAmountcreditnote','Standardrated','GSTPaid','PaymentStatus','NewStatus','Transactioncode','aReceiveddate','a2ndPaymentReceiveddate','Receivedamount','ReceivedamountCurrency','Discount','DiscountCurrency','InvCurrency','OutstandingBalance','Supt']
        fields = ['id','Branch','PONo','POIssuedby', 'ClientName','ClientGroup','Shipname', 'POAmount', 'InvoiceNo', 'InvoiceDate', 'Duedate','Freight', 'Invoiceamount', 'SgdValue', 'GstScope', 'currency1', 'Invamtcreditnote', 'standardrated', 'GstPaid', 'paymentstatus', 'newstatus', 'transactioncode', 'areceiveddate', 'a2ndpaymentReceiveddate', 'receivedamount', 'receivedamountCurrency', 'dc', 'discountcurrency', 'Invcurrency', 'outstandingBalance', 'supt']
    # Apply the regex validator to the ClientName field
    # ClientName = forms.CharField(validators=[alphanumeric_validator])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name not in ['id']:
                field.required = False
