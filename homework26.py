import asyncio

async def task1():
    print('F1 start')
    await asyncio.sleep(1)
    print("F1 finish")

async def task2():
    print('F2 start')
    await asyncio.sleep(3)
    print("F2 finish")

async def task3():
    print('F3 start')
    await asyncio.sleep(2)
    print("F3 finish")

async def task_caller():
    await asyncio.gather(
        task2(),
        task3(),
        task1()
    ) 

asyncio.run(task_caller())

# functions start in order that they were written and end by whom was faster