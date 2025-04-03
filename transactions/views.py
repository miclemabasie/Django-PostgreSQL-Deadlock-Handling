from django.shortcuts import render
from transactions.models import Account


def transfer_funds(sender_id, receiver_id, amount):
    sender = Account.objects.get(id=sender_id)
    receiver = Account.objects.get(id=receiver_id)

    if sender.balance < amount:
        raise ValueError("Insufficient funds")

    sender.balance -= amount
    receiver.balance += amount
        
    sender.save()
    receiver.save()


# from django.db import transaction
# from transactions.models import Account

# def transfer_funds_naive(sender_id, receiver_id, amount):
#     # 🔥 Wrap in a transaction to hold locks longer
#     with transaction.atomic():
#         sender = Account.objects.get(id=sender_id)
#         receiver = Account.objects.get(id=receiver_id)
        
#         if sender.balance < amount:
#             raise ValueError("Insufficient funds")
        
#         sender.balance -= amount
#         receiver.balance += amount
        
#         sender.save()
#         receiver.save()