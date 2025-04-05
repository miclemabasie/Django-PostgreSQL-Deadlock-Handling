# Preventing Django Deadlocks & Race Conditions  
*A practical guide to handling high-concurrency transactions in Django + PostgreSQL.*  

## Overview  
This project demonstrates how to prevent data corruption and deadlocks in Django applications using:  
- **Atomic transactions**  
- **Row-level locking**  
- **Exponential backoff retries**  

## Features  
- 🧪 Thread stress tests for race conditions.  
- 📊 Benchmark comparisons (naive vs. robust implementations).  
- 📜 PostgreSQL log analysis for deadlock detection.  

## Installation  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/miclemabasie/Django-PostgreSQL-Deadlock-Handling.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Run migrations:  
   ```bash  
   python manage.py migrate  
   ```  

## Usage  
### Simulate a Race Condition  
```bash  
python manage.py runscript simulate_race_condition  
```  
**Expected Output**:  
```  
[NAIVE] Sender: $400, Receiver: $1600  # 😱 Data loss!  
```  

### Run the Robust Solution  
```bash  
python manage.py runscript simulate_robust_transfer  
```  
**Expected Output**:  
```  
[ROBUST] Sender: $0, Receiver: $2000  # ✅ Consistent!  
```  

## Technical Deep Dive  
### Key Components  
1. **Atomic Transactions**  
   - Ensures all operations succeed or fail together.  
2. **select_for_update()**  
   - Locks rows to prevent concurrent modifications.  
3. **Exponential Backoff**  
   - Retries failed transactions with increasing delays.  

## Contributing  
Pull requests welcome! For major changes, open an issue first.  

## License  
MIT  
