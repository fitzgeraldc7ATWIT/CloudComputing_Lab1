import unittest
import requests
import json

from Lab2.lab2Main import CollegeStudentInput


class MyTestCase(unittest.TestCase):
    def test_getRoot(self):
        url = "http://localhost:8080/"
        response = requests.get(url)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getTime(self):
        url = "http://localhost:8080/time"
        response = requests.get(url)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getAnimal(self):
        url = "http://localhost:8080/animal/{name}"
        response = requests.get(url)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getColor(self):
        url = "http://localhost:8080/color/{name}"
        response = requests.get(url)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_postCollegeStudent(self):
        url = "http://localhost:8080/college-student"
        info =  {
            "name": "string",
            "age": 0,
            "year": 0,
            "major": "string"
        }
        response = requests.post(url, json=info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getQuery(self): #query string, might need to change test
        url = "http://localhost:8080/query"
        info = {
            "name": "string",
            "age": 0,
            "country": "string",
        }
        response = requests.get(url, info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_postCar(self):
        url = "http://localhost:8080/car"
        info = {
            "make": "string",
            "model": "string",
            "year": 0,
        }
        response = requests.post(url, json=info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getSports(self): #query string, might need to change test
        url = "http://localhost:8080/sports"
        info = {
            "name": "string"
        }
        response = requests.get(url, info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getBook(self): #query string, might need to change test
        url = "http://localhost:8080/book"
        info = {
            "genre": "string",
            "book": "string"
        }
        response = requests.get(url, info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getHometown(self): #query string, might need to change test
        url = "http://localhost:8080/hometown"
        info = {
            "highschool": "string",
            "town": "string"
        }
        response = requests.get(url, info)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getHeaders(self):
        url = "http://localhost:8080/headers/"
        headers = {
            "Content-Type": "application/json",
            "X-Custom-header": "CustomValue",
            "user_email": "ColeF",
            "my-val": "my_value"
        }
        response = requests.get(url=url, headers=headers)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)

    def test_getCookie(self):
        url = "http://localhost:8080/read_cookie"
        response = requests.get(url)

        print("Status Code: ", response.status_code)
        print("Response Body: ", response.json())
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
