from twisted.web.client import getPage,defer
from twisted.internet import reactor


def all_done(ret):
    print(ret)
    reactor.close()

def parse_page(ret):
    ret= ret.result()
    print(ret)


if __name__ =="__main__":
    urls=[1,2,3,4,5,6,7,8,9]

    tasks=[]
    for url in urls:
        obj=getPage(url)
        obj.addCallback(parse_page)
        tasks.append(obj)

    defer.DeferredList(tasks).addBoth(all_done)
    reactor.run()


