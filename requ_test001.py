import requests
import json
import unittest
from bs4 import BeautifulSoup

class Git_hub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/63.0.3239.84 Safari/537.36',
            "Accept-Language": "en-US,en;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
        }
        payload = {'username': 'hostpost114@gmail.com', 'password': 'li*******'}
        cls.s = requests.Session()
        cls.s.post('http://www.github.com/login', data=payload)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_re001(self):
        response = self.s.get('https://github.com/hostpost114/Fist')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response.status_code)
        print(soup.title.string)
        print(response.url)
        self.assertEqual(response.url,'https://github.com/hostpost114/Fist')

    def test_re002(self):
        response = self.s.get('https://github.com/hostpost114/Fist/blob/master/1231api')
        soup = BeautifulSoup(response.text, 'html.parser')
        print(response.status_code)
        print(soup.title.string)
    def test_re003(self):
        payload = {'username': 'hostpost', 'pas': 'lixia'}
        response=self.s.get('http://httpbin.org/get',params=payload)
        print(response.json()['args']['pas'])
        print(response.text)
        print(response.headers)
        print(response.cookies)
        self.assertEqual(response.json()['args']['pas'], 'lixia')
    def test_re004(self):
        response=requests.get("http://www.baidu.com")
        print(response.url)
        response.encoding = response.apparent_encoding  #更改编码格式，设置为和浏览器一样的格式
        print(response.text)


    @classmethod
    def tearDownClass(cls):
        print("test....................over")

if __name__ == "__main__":
    unittest.main()
