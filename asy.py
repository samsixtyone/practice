import asyncio
import sys

async def main(num_tasks):
    tasks = []

    for task_id in range(num_tasks):
        tasks.append(asyncio.sleep(10))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_tasks = int(sys.argv[1])
    asyncio.run(main(num_tasks))
