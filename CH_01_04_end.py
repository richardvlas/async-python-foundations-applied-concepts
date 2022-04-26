import asyncio
from datetime import datetime
import click


async def sleep_and_print(seconds):
    print(f"starting {seconds} sleep 😴")
    await asyncio.sleep(seconds)
    print(f"finished {seconds} sleep ⏰")
    return seconds


async def main():
    # using arguments
    # results = await asyncio.gather(sleep_and_print(3), sleep_and_print(6))

    # alternatively you can add things to the gather function programatically
    # comment results on line 15 before uncomenting the code on next lines
    coroutines_list  = []
    for i in range(1, 11):
        # sleep_and_print is not going to execute on the next line but
        # first when I dump it into the gather utility which accepts arguments
        # but not list therefore the use of * 
        coroutines_list.append(sleep_and_print(i))
    results = await asyncio.gather(*coroutines_list)
    print(results)
    

start = datetime.now()
asyncio.run(main())
click.secho(f"{datetime.now()-start}", bold=True, bg="blue", fg="white")
