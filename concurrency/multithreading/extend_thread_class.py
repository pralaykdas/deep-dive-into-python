# Extend the Thread class

from threading import Thread
import urllib.request

class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url

    def run(self) -> bool:
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)
        return True

def main():
    urls = [
        'https://httpstat.us/200',
        'https://httpstat.us/400'
    ]

    threads = [HttpRequestThread(url) for url in urls]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

if __name__ == "__main__":
    main()
