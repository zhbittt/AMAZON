import asyncio
import requests

def all_done():
    pass

def parse_page(ret):
    ret= ret.result()
    print(ret)

@asyncio.coroutine
def down_page(url):
    yield from requests.get(url)

if __name__ =="__main__":

    tasks=[]
    urls=[1,2,3,4,5,6,7]

    for url in urls:
        tasks.append(down_page(url))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()