import unittest
import requests
import json

#comment in whichever you want to see

# from incorrect import getPics, storePics
from correct import getPics, storePics


class Tests(unittest.TestCase):

    def setUp(self):
        self.apikey = "live_zhI0ury2bg3t3tkvE78K0VjZT1Dv5yV4rLxbMAmbTgAIjX02lPdK9QEhefrsvAR"
        self.url = "https://api.thecatapi.com/v1/images/search"


#tests that apikey is string
    def test_apikey_string(self):
        self.assertTrue(isinstance(self.apikey, str))

#tests that url is string
    def test_url_string(self):
        self.assertTrue(isinstance(self.url, str))

#test that it is valid URL
    def test_urls_start_with_https(self):
        album = storePics(getPics, 1)  # Pass the getPics function here, not the result
        album_list = json.loads(album)  # Parse the JSON list
        for url in album_list:
            self.assertTrue(url.startswith("https://"), f"URL doesn't start with 'https://': {url}")

#test to make sure the result from "getPics" is an object
    def test_getPics_returns_object(self):
        result = getPics(self.apikey)
        self.assertTrue(isinstance(result, list))
        if result:
            self.assertTrue(isinstance(result[0], dict))

#test to make sure result from "storePics" is an object
    def test_storePics_func_param(self):
        album = storePics(getPics, 1)
        album_list = json.loads(album)  # Parse the JSON list
        self.assertTrue(all(isinstance(url, str) and url.startswith("http") for url in album_list))

#test to make sure it fails IF the result is not a list
    def test_storePics_not_list(self):
        # Simulate a non-list result
        result = "This is not a list"

        # Expect the test to fail because the 'result' is not a list
        with self.assertRaises(TypeError):
            # The code in storePics() will raise a TypeError here
            album = storePics(result, 1)
            json.dumps(album)
if __name__ == '__main__':
    unittest.main()