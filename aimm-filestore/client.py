import requests

'''
File server client implementation
'''
class FSClient:
    def __init__(self, host, port, access_key, access_secret, secure=True):
        self.host = host
        self.port = int(port)
        self.access_key = str(access_key)
        self.access_secret = str(access_secret)

        self.headers = {"X-Access-Key": self.access_key,
                        "X-Access-Secret": self.access_secret}

        self.protocol = "http"
        if secure:
            self.protocol = "https"

        self.url = "{}://{}:{}".format(self.protocol, self.host, self.port)

    '''
    Uploads a file under a specific key
    '''
    def store(self, key, file):
        f = open(file, 'rb')
        data = f.read()
        headers = self.headers
        headers["Content-Type"] = "application/octet-stream"
        res = requests.post(url="{}/store/{}".format(self.url, key), data=data, headers=headers)
        if res.status_code != 200:
            raise Exception(res.text)

        f.close()
        return True

    '''
    Downloads the binary content and stores in a file
    '''
    def retrieve(self, key, file):
        res = requests.get(url="{}/retrieve/{}".format(self.url, key), headers=self.headers)

        if res.status_code != 200:
            raise Exception(res.text)
        else:
            data = res.content
            f = open(file, 'wb')
            f.write(data)
            f.close()

        return file

    def list(self):
        res = requests.get(url="{}/list".format(self.url), headers=self.headers)

        if res.status_code != 200:
            raise Exception(res.text)
        else:
            return res.json()


    def delete(self, key):
        res = requests.delete(url="{}/delete/{}".format(self.url, key), headers=self.headers)

        if res.status_code != 200:
            raise Exception(res.text)

        return True



