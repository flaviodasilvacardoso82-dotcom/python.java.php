from datetime import datetime, timedelta


hora = datetime.now()
print(hora)

print(f'{datetime.now() + timedelta(minutes=10)}')
