import uuid


class Request(object):
    def __init__(self, inn, p_type, customer_receipt, invoice_id=None, callback_url=None):
        self.data = {
            "Inn": inn,
            "Type": p_type,
            "InvoiceId": str(uuid.uuid4()) if invoice_id is None else invoice_id,
            "CustomerReceipt": customer_receipt.data
        }
        if callback_url is not None:
            self.data["CallbackUrl"] = callback_url


class CustomerReceipt(object):
    def __init__(self, taxation_system, email, phone, payment_type, bill_address, client_info, items, payment_items, \
                 cashier, automatic_device_number=None, payment_agent_info=None):
        self.data = {
            "TaxationSystem": taxation_system,
            "Email": email,
            "Phone": phone,
            "AutomaticDeviceNumber": automatic_device_number,
            "PaymentType": payment_type,
            "PaymentAgentInfo": payment_agent_info,
            "BillAddress": bill_address,
            "ClientInfo": client_info.data,
            "Items": [item.data for item in items],
            "PaymentItems": [p_item.data for p_item in payment_items],
            "CustomUserProperty": None,
            "Cashier": cashier.data
        }


class Item(object):
    def __init__(self, label, price, quantity, amount, vat, measure, payment_method, payment_type, \
                 marking_code_structured=None, marking_code=None, origin_country_code="643", \
                 customs_declaration_number=None, payment_agent_info=None):
        self.data = {
            "Label": label,
            "Price": price,
            "Quantity": quantity,
            "Amount": amount,
            "Vat": vat,
            "Measure": measure,
            "PaymentMethod": payment_method,
            "PaymentType": payment_type,
            "MarkingCodeStructured": marking_code_structured,
            "MarkingCode": marking_code,
            "OriginCountryCode": origin_country_code,
            "CustomsDeclarationNumber": customs_declaration_number,
            "PaymentAgentInfo": payment_agent_info
        }


class PaymentItem(object):
    def __init__(self, payment_type, sum):
        self.data = {
            "PaymentType": payment_type,
            "Sum": sum
        }


class Cashier(object):
    def __init__(self, name, inn):
        self.data = {
            "Name": name,
            "Inn": inn
        }


class ClientInfo(object):
    def __init__(self, name, inn):
        self.data = {
            "Name": name,
            "Inn": inn,
        }
