import os
import django

# Set the environment variable for Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "postgresDeadlock.settings")

# Manually initialize Django
django.setup()

# Now you can safely import your Django models
from transactions.views import transfer_funds_naive, transfer_funds
from transactions.models import Account
account1 = Account.objects.get(id=1)
account2 = Account.objects.get(id=2)


import threading  

# Launch 10 threads to simulate concurrent transfers  
threads = []  
for _ in range(10):  
    t = threading.Thread(  
        target=transfer_funds,  
        args=(account1.id, account2.id, 100)  
    )  
    threads.append(t)  
    t.start()  

for t in threads:  
    t.join()  