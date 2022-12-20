from threading import Thread
import asyncio
import time

def f1():
    for i in range(1000):
        print('---')

def f2():
    for i in range(1000):
        print('o')

async def af1():
    for i in range(100):
        print('---')
        await asyncio.sleep(0)

async def af2():
    for i in range(100):
        print('o')
        await asyncio.sleep(0)

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

def main():
    Thread(target = f1).start()
    Thread(target = f2).start()

async def main2():
    t1 = asyncio.create_task(af1())
    t2 = asyncio.create_task(af2())

    await t1
    await t2

async def main3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main2())