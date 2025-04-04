import threading
from transactions.models import Account
from transactions.views import transfer_funds_transaction, transfer_funds

# This test simulates concurrent fund transfers between two accounts.

# Reset balances
Account.objects.filter(id=1).update(balance=1000)
Account.objects.filter(id=2).update(balance=1000)

# Launch 10 threads
threads = []
for _ in range(10):
    t = threading.Thread(target=transfer_funds, args=(1, 2, 100))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Check results
a = Account.objects.get(id=1)
b = Account.objects.get(id=2)
print(f"Sender: ${a.balance}, Receiver: ${b.balance}")
