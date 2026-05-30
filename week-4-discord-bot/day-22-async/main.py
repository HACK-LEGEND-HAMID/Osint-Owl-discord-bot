#Day 22: Sync Demo 
import time

start = time.time()  # ⏱️ Timer start

print("1️⃣ First task started")
time.sleep(3)
print("✅ First task done (3 sec)")

print("2️⃣ Second task started")
time.sleep(2)
print("✅ Second task done (2 sec)")

print("3️⃣ Third task started")
time.sleep(1)
print("✅ Third task done (1 sec)")

end = time.time()  # ⏱️ Timer stop

total = end - start
print(f"\n⏱️ Total time: {total:.1f} seconds")
