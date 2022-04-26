from pprint import pprint
import asyncio
import json

import aiohttp

URIS = (
    "https://api.github.com/orgs/python",
    "https://api.github.com/orgs/django",
    "https://api.github.com/orgs/pallets",
)


def write_to_file(data):
    with open("repo_data.json", "w") as jf:
        json.dump(data, jf)


async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.json()
        return {"name": data["name"], "avatar_url": data["avatar_url"]}


async def main():
    async with aiohttp.ClientSession() as session:
        """
        1. use 'await asyncio.gather' and 'fetch' to get repo names and avatar_urls
        2. use 'write_to_file' to create a json file with the results
        3. text your code
            a. 'cd CH_02_03'
            b. 'python create_json.py' # To check that all works fine and 
                                       # then type the next line with any port e.g. 3000
            c. 'python -m http.server 3000'
        """
        data = await asyncio.gather(*[fetch(session, uri) for uri in URIS])
        print("DATA: --------------")
        print(data)
        print("END DATA: --------------")
        write_to_file(data)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
#asyncio.run(main())
