#Day 22: Async Demo 
import asyncio
import time

async def task(name, sec):
    print(f"🟢 {name} started")
    await asyncio.sleep(sec)
    print(f"✅ {name} done ({sec} sec)")
    return f"{name} completed"

async def main():
    results = await asyncio.gather(
        task("First", 3),
        task("Second", 2),
        task("Third", 1)
    )
    return results

start = time.time()  
results = asyncio.run(main())
end = time.time()

total = end - start
print(f"\n⏱️ Total time: {total:.1f} seconds")
