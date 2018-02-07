from concurrent.futures import ThreadPoolExecutor

def parse_page(ret):
    ret= ret.result()
    print(ret)

def down_page(url):

    return url

if __name__ =="__main__":
    pool = ThreadPoolExecutor(10)

    urls=["1","2","3","4","5","6"]

    for url in urls:
        pool.submit(down_page,url).add_done_callback(parse_page)

    pool.shutdown(wait=True)