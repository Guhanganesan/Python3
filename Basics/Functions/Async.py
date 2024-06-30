"""
Asyncio is a Python library that is used for concurrent programming, including the use of async iterator in Python. 
It is not multi-threading or multi-processing. Asyncio is used as a foundation for multiple Python asynchronous frameworks that provide 
high-performance network and web servers, database connection libraries, distributed task queues, etc
"""
import asyncio
 
async def fn():
     
    print("one")
    await asyncio.sleep(1)
    await fn2() # Note here......
    print('four')
    await asyncio.sleep(1)
    print('five')
    await asyncio.sleep(1)
 
async def fn2():
    await asyncio.sleep(1)
    print("two")
    await asyncio.sleep(1)
    print("three")
asyncio.run(fn())
"""
one 
two
three
four
five"""

import asyncio


async def func1():
	print("Function 1 started..")
	await asyncio.sleep(2)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(3)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(1)
	print("Function 3 Ended")


async def main():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")


asyncio.run(main())

"""
Function 1 Started
Function 2 Started 
Function 3 Started'
Function 3 Ended
Function 1 Ended 
Function 2 Ended
Mian Ended

Ref: https://www.geeksforgeeks.org/asyncio-in-python/?ref=lbp
"""
