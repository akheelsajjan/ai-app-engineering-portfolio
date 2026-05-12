import asyncio
import time


async def fetch_data(name: str, delay: int):
    print(f"Starting {name}")
    
    await asyncio.sleep(delay)
    
    print(f"Finished {name}")
    
    return f"{name} data"


async def main():
    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_data("user-api", 2),
        fetch_data("vector-db", 3),
        fetch_data("llm-call", 4),
    )

    end = time.perf_counter()

    print(results)
    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())