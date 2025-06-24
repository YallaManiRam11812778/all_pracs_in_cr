# from pydantic import BaseModel, StringConstraints, SecretStr, ValidationError, Field, ConfigDict
# from typing import Annotated
# from datetime import datetime

# class MEI_INVOICE_EXCEPTIONS(BaseModel):
#     FinancialYear : Annotated[str, StringConstraints(max_length=10,min_length=10)]
#     date : datetime
#     special : str = Field(pattern=r"^[^а-яА-ЯёЁ]*$")
#     password : SecretStr|None
#     invoice_period : list[dict] = Field(min_items=2,max_items=3)
#     model_config = ConfigDict(
#         extra='forbid')
    
# def validation(data:dict):
#     try:
#         MEI_INVOICE_EXCEPTIONS.model_validate(data)
#     except ValidationError as e:
#         for error in e.errors():
#             print(error,">"*100)
# validation(data={"FinancialYear":"7845385","special":"a%#@#$%^&*/bc","password":None,"date":"2024-04-26T17:47:49.2Z","invoice_period":[{"av":""},{"v":""},{"a":""}]})

# ['FinancialYear', 'ReferenceNumber', 'SupplyType', 'InvoiceType', 'InvoiceNumber', 'eInvoiceDateandTime', 'eInvoiceVersion', 'OriginaleInvoiceReferenceNumber', 'InvoiceCurrencyCode', 'CurrencyExchangeRate', 'FrequencyofBilling', 'BillingPeriod', 'SupplierCode', 'SupplierName', 'SupplierTIN', 'SupplierRegistration', 'SupplierMyKadNumber', 'PassportNumber', 'SupplierSSTRegistrationNumber', 'SupplierTourismTaxRegistrationNumber', 'SupplierMSICCode', 'SupplierBusinessActivityDescription', 'SupplierAddressField1', 'SupplierAddressField2', 'SupplierAddressField3', 'SupplierPostalCode', 'SupplierCity', 'SupplierState', 'SupplierCountry', 'SupplierContactNumber', 'Supplieremail', 'BuyerCode', 'BuyerName', 'BuyerTIN', 'BuyerMyKadNumber', 'BuyerPassportNumber', 'BuyerRegistration', 'BuyerSSTRegistrationNumber', 'BuyerAddressField1', 'BuyerAddressField2', 'BuyerAddressField3', 'BuyerPostalCode', 'BuyerCity', 'BuyerState', 'BuyerCountry', 'BuyerContactNumber', 'Buyeremail', 'ShippingRecipientsName', 'ShippingRecipientTIN', 'ShippingMyKadNumber', 'ShippingPassportNumber', 'ShippingRegistration', 'ShippingAddressField1', 'ShippingAddressField2', 'ShippingAddressField3', 'ShippingPostalCode', 'ShippingCity', 'ShippingState', 'ShippingCountry', 'IncoTerms', 'ProductTariffCode', 'FTAInformation', 'AuthorisationNumberforCertifiedExporter', 'ReferenceNumberofCustomsFormNo.1,9,', 'ReferenceNumberofCustomsFormNo2', 'CountryofOrigin', 'DetailsofOtherCharges', 'TotalInvoiceAmount', 'TotalTaxableAmount', 'TotalTaxAmount', 'TotalDiscountAmount', 'RoundingofAmount', 'PrepaidAmount', 'AmounttobePaid', 'LineItemIdentifier', 'ItemCode', 'Classification', 'DescriptionofProductorService', 'UnitPrice', 'TaxType', 'TaxRate', 'TaxAmount', 'DetailsofTaxExemption', 'AmountExemptedfromTax', 'SubTotal', 'TotalExcludingTax', 'TotalIncludingTax', 'Quantity', 'Measurement', 'DiscountRate', 'DiscountAmount', 'PaymentMode', 'SupplierBankAccountNumber', 'PaymentTerms', 'PaymentAmount', 'PaymentDate', 'PaymentReferenceNumber', 'BillReferenceNumber']
from pydantic import BaseModel, ValidationError, Field, ConfigDict,EmailStr
from typing import List
from datetime import date

class Payment_Details(BaseModel):
    PaymentMode : str = Field(pattern=r"^[0-9]+$")
    SupplierBankAccountNumber : str = Field(pattern=r"^[0-9\-]+$")
    PaymentTerms : str 
    PaymentAmount : str = Field(pattern=r"^[0-9]+$|^[0-9]+\.[0-9]{2}$")
    PaymentDate : str = Field(date,pattern=r"\d{2}/\d{2}/\d{4}$")
    PaymentReferenceNumber : str = Field(pattern=r"^[A-Za-z0-9]+$")
    BillReferenceNumber : int


class Invoice_Item_details(BaseModel):
    LineItemIdentifier : int
    Classification : str = Field(pattern=r"^[0-9]+$")
    DescriptionofProductorService : str
    UnitPrice : str = Field(pattern=r"^([0-9]+\.[0-9]{2})$")
    TaxType : str = Field(pattern=r"^[0-9]+$")
    TaxRate : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")
    TaxAmount : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")
    DetailsofTaxExemption : str = Field(pattern=r"^[A-Za-z0-9\-]+$")
    AmountExemptedfromTax : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")
    Subtotal : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")
    TotalExcludingTax : float
    TotalIncludingTax : float
    Quantity : float
    Measurement : int
    DiscountRate : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")
    DiscountAmount : str = Field(pattern=r"^[0-9]+$|^([0-9]+\.[0-9]{2})$")


class Invoice_Details(BaseModel):
    FinancialYear : int
    ReferenceNumber : str 
    SupplyType : str 
    InvoiceType : int
    InvoiceNumber : str 
    IRBMLink : str 
    IRBMNumber : str 
    IRBMUniqueIdentifierNumber : int
    eInvoiceDateandTime : str = Field(date,pattern=r"\d{2}/\d{2}/\d{4}$")
    eInvoiceVersion : str = Field(pattern=r"^[0-9\.]+$")
    OriginaleInvoiceReferenceNumber : str = Field(pattern=r"^[0-9]+$")
    InvoiceCurrencyCode : str = Field(pattern=r"^[A-Za-z0-9]+$")
    CurrencyExchangeRate : str = Field(pattern=r"^[0-9]+$")
    FrequencyofBilling : str = Field(pattern=r"^[0-9]+$")
    BillingPeriod: str = Field(pattern = r"(^$)|^[A-Za-z0-9\-]+$" )
    SupplierCode: str 
    SupplierName: str 
    SupplierTIN: str = Field(pattern=r"^[A-Za-z0-9]+$")
    SupplierRegistration: str = Field(pattern=r"^[A-Za-z0-9]+$")
    SupplierMyKadNumber: str = Field(pattern=r"^[0-9]+$")
    PassportNumber : str = Field(pattern=r"^[A-Za-z0-9]+$")
    SupplierSSTRegistrationNumber : str = Field(pattern = r"^[A-Za-z0-9\-]+$" )
    SupplierTourismTaxRegistrationNumber : str = Field(pattern = r"^[A-Za-z0-9\-]+$" )
    SupplierMSICCode : str = Field(pattern=r"^[0-9]+$")
    SupplierBusinessActivityDescription : str 
    SupplierAddressField1 : str 
    SupplierAddressField2 : str 
    SupplierAddressField3 : str 
    SupplierPostalCode : str 
    SupplierCity : str 
    SupplierState : str 
    SupplierCountry : str 
    SupplierContactNumber : str = Field(pattern=r"^[0-9]+$")
    Supplieremail : EmailStr
    BuyerCode : str 
    BuyerName : str 
    BuyerTIN : str = Field(pattern=r"^[A-Za-z0-9]+$")
    BuyerMyKadNumber : int
    BuyerPassportNumber : str = Field(pattern=r"^[A-Za-z0-9]+$")
    BuyerRegistration: str = Field(pattern=r"^[A-Za-z0-9]+$")
    BuyerSSTRegistrationNumber : str = Field(pattern = r"^[A-Za-z0-9\-]+$" )
    Buyeremail : EmailStr
    BuyerAddressField1 : str 
    BuyerAddressField2 : str 
    BuyerAddressField3 : str 
    BuyerPostalCode : str 
    BuyerCity : str 
    BuyerState : str 
    BuyerCountry : str 
    BuyerContactNumber : str = Field(pattern=r"^[0-9]+$")
    ShippingRecipientsName : str 
    ShippingRecipientTIN : str 
    ShippingMyKadNumber : int
    ShippingPassportNumber : int
    ShippingRegistration : str 
    ShippingReferenceNumber : str 
    ShippingAddressField1 : str 
    ShippingAddressField2 : str 
    ShippingAddressField3 : str 
    ShippingPostalCode : int
    ShippingCity : str 
    ShippingState : str
    ShippingCountry : str 
    IncoTerms : str 
    ProductTariffCode : str 
    FTAInformation : str 
    AuthorisationNumberforCertifiedExporter : str 
    ReferenceNumberofCustomsFormNo2 : str 
    CountryofOrigin : str
    DetailsofOtherCharges : str 
    TotalInvoiceAmount : int
    TotalTaxableAmount : int
    TotalTaxAmount : int
    TotalDiscountAmount : int 
    RoundingofAmount : int
    PrepaidAmount : int
    AmounttobePaid : int
    InvoiceLineItemDetails : List[Invoice_Item_details]
    PaymentDetails : List[Payment_Details]
    model_config = ConfigDict(
        extra='allow') # allow, ignore, forbid


class Invoice(BaseModel):
    data : List[Invoice_Details]


def validation():
    try:
        a = Invoice.model_validate({'data':data})
    except ValidationError as e:
        for error in e.errors():
            print(error,">"*100)

data=[
    {
    "FinancialYear": "2024",
    "ReferenceNumber": "TEST-INVOICE-0127",
    "SupplyType": "B2B",
    "InvoiceType": "01",
    "InvoiceNumber": "TEST-INVOICE-0127",
    "IRBMLink": "",
    "IRBMNumber": "",
    "IRBMUniqueIdentifierNumber": "16",
    "eInvoiceDateandTime": "13/10/2009",
    "eInvoiceVersion": "10",
    "OriginaleInvoiceReferenceNumber": "567",
    "InvoiceCurrencyCode": "MYR",
    "CurrencyExchangeRate": "10",
    "FrequencyofBilling": "01",
    "BillingPeriod": "",
    "SupplierCode": "",
    "SupplierName": "AMS Setia Jaya Sdn. Bhd",
    "SupplierTIN": "C25845632022",
    "SupplierRegistration": "201901234567",
    "SupplierMyKadNumber": "16",
    "PassportNumber": "097",
    "SupplierSSTRegistrationNumber": "Supplier23",
    "SupplierTourismTaxRegistrationNumber": "Supplier23",
    "SupplierMSICCode": "10712",
    "SupplierBusinessActivityDescription": "Manufacturing of Automotive parts",
    "SupplierAddressField1": "Seller Address Field 1 | Medan Alamat Penjual 1",
    "SupplierAddressField2": "Seller Address Field 2 | Medan Alamat Penjual 2",
    "SupplierAddressField3": "Seller Address Field 3 | Medan Alamat Penjual 3",
    "SupplierPostalCode": "10003 | 10003",
    "SupplierCity": "Kuala Lumpur | Kuala Lumpur",
    "SupplierState": "MA",
    "SupplierCountry": "SAU",
    "SupplierContactNumber": "60312345645",
    "Supplieremail": "gen@supplier.com",
    "BuyerCode": "",
    "BuyerName": "Setia Jay Sdn. Bhd",
    "BuyerTIN": "C25845632022",
    "BuyerMyKadNumber": "1234",
    "BuyerPassportNumber": "0987",
    "BuyerRegistration": "Buyer23",
    "BuyerSSTRegistrationNumber": "Buyer23",
    "Buyeremail": "eneral.ams@supplier.com",
    "BuyerAddressField1": "Buyer Address Field 1 | Medan Alamat Pembeli 1",
    "BuyerAddressField2": "Buyer Address Field 2 | Medan Alamat Pembeli 2",
    "BuyerAddressField3": "Buyer Address Field 3 | Medan Alamat Pembeli 3",
    "BuyerPostalCode": "10003 | 10003",
    "BuyerCity": "Kuala Lumpur | Kuala Lumpur",
    "BuyerState": "MA",
    "BuyerCountry": "SAU",
    "BuyerContactNumber": "60312345645",
    "ShippingRecipientsName": "",
    "ShippingRecipientTIN": "",
    "ShippingMyKadNumber": "1234",
    "ShippingPassportNumber": "0987",
    "ShippingRegistration": "Buyer23",
    "ShippingReferenceNumber": "",
    "ShippingAddressField1": "Address Field 1",
    "ShippingAddressField2": "Address Field 2",
    "ShippingAddressField3": "Address Field 3",
    "ShippingPostalCode": "10003",
    "ShippingCity": "Malayasia",
    "ShippingState": "MA",
    "ShippingCountry": "SAU",
    "IncoTerms": "",
    "ProductTariffCode": "",
    "FTAInformation": "",
    "AuthorisationNumberforCertifiedExporter": "",
    "ReferenceNumberofCustomsFormNo2": "",
    "CountryofOrigin": "",
    "DetailsofOtherCharges": "",
    "TotalInvoiceAmount": "44",
    "TotalTaxableAmount": "86",
    "TotalTaxAmount": "87",
    "TotalDiscountAmount": "45",
    "RoundingofAmount": "134",
    "PrepaidAmount": "67",
    "AmounttobePaid": "45",
    "InvoiceLineItemDetails": [
      {
        "LineItemIdentifier": "1",
        "Classification": "001",
        "DescriptionofProductorService": "Automotive products - Exhaust",
        "UnitPrice": "100.00",
        "TaxType": "01",
        "TaxRate": "07",
        "TaxAmount": "10",
        "DetailsofTaxExemption": "129",
        "AmountExemptedfromTax": "78",
        "Subtotal": "23",
        "TotalExcludingTax": "999.00",
        "TotalIncludingTax": "1000.00",
        "Quantity": "10.00",
        "Measurement": "10",
        "DiscountRate": "0",
        "DiscountAmount": "109"
      }
    ],
    "PaymentDetails": [
      {
        "PaymentMode": "1",
        "SupplierBankAccountNumber": "1269",
        "PaymentTerms": "PaymentTerms",
        "PaymentAmount": "100",
        "PaymentDate": "12/12/2023",
        "PaymentReferenceNumber": "1",
        "BillReferenceNumber": "12"
      }
    ]
  }
]
validation()