############################################################
# Write a code in python to run two coroutine concurrently for infinite time.
#1st coroutine will print number starting from 0.
#2nd coroutine will print the duration after each 3 seconds.
############################################################

import asyncio

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_coroutines())


async def start_coroutines():
    tasks = [asyncio.ensure_future(each_coroutine()) for each_coroutine in (first_coroutine, second_coroutine)]
    await asyncio.wait(tasks)


async def first_coroutine():
    count = 0
    while True:
        print(f"{count} seconds have passed")
        await asyncio.sleep(3)
        count += 3


async def second_coroutine():
        count = 0
        while True:
            print(f"{count}")
            # added this sleep so that output wouln't be too fast to read.
            await asyncio.sleep(0.45)
            count +=1


if __name__ == "__main__":
    main()