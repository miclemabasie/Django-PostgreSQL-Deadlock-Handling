from transactions.models import Account


def transfer_funds(sender_id, receiver_id, amount):
    sender = Account.objects.get(id=sender_id)
    receiver = Account.objects.get(id=receiver_id)

    if sender.balance < amount:
        raise ValueError("Insufficient funds")

    sender.balance -= amount
    receiver.balance += amount

    sender.save()  # Autocommit
    receiver.save()  # Autocommit


from django.db import transaction


def transfer_funds_transaction(sender_id, receiver_id, amount):
    with transaction.atomic():  # Explicit transaction
        sender = Account.objects.get(id=sender_id)
        receiver = Account.objects.get(id=receiver_id)

        if sender.balance < amount:
            raise ValueError("Insufficient funds")

        sender.balance -= amount
        receiver.balance += amount

        sender.save()
        receiver.save()


from django.db import transaction, DatabaseError
import time
import random


def assign_sender_receiver(accounts, sender_id):
    """Helper to order accounts consistently."""
    sender = accounts[0] if accounts[0].id == sender_id else accounts[1]
    receiver = accounts[1] if sender == accounts[0] else accounts[0]
    return sender, receiver


def transfer_funds_robust(sender_id, receiver_id, amount, max_retries=5):
    for attempt in range(max_retries):
        try:
            with transaction.atomic():
                # 1. Lock rows IN ORDER to prevent deadlocks
                accounts = (
                    Account.objects.filter(id__in=[sender_id, receiver_id])
                    .order_by("id")
                    .select_for_update()
                )

                sender, receiver = assign_sender_receiver(accounts, sender_id)

                if sender.balance < amount:
                    raise ValueError("Insufficient funds")

                # 2. Atomic update
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()
            return
        except DatabaseError:
            # 3. Exponential backoff
            sleep_time = (2**attempt) + random.uniform(0, 1)
            time.sleep(sleep_time)
    raise Exception("Transfer failed after maximum retries.")
