from ofdfermaapi import FermaTestApi
from ofdfermaapi.objects import *


#api = FermaTestApi('fermatest1', 'Hjsf3321klsadfAA')
api = FermaTestApi('fermatest2', 'Go2999483Mb')

item1 = Item(label='Подгузники размер S',
             price=200,
             quantity=2,
             amount=400,
             vat='Vat0',
             measure='PIECE',
             payment_method=1,
             payment_type=1)

payment_item1 = PaymentItem(payment_type=1, sum=2650)

cashier1 = Cashier(name='Иванова К.С.', inn='123456789')

client_info1 = ClientInfo(name='Иванов Иван Иванович', inn='123456789')

customer_receipt = CustomerReceipt(taxation_system='Common',
                                   email='moskvichyov.p@gmail.com',
                                   phone='+79031272714',
                                   payment_type=1,
                                   bill_address='Пресненская набережная, Башня Федерация',
                                   client_info=client_info1,
                                   items=[item1],
                                   payment_items=[payment_item1],
                                   cashier=cashier1)

request = Request(inn='3245001416',
                  p_type='Income',
                  customer_receipt=customer_receipt)

response = api.send_receipt(request)

print(response.text)
