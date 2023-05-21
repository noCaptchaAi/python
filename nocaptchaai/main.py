import requests
import time
import base64
from PIL import Image
from io import BytesIO


class hCaptchaToken:
    def __init__(self, apikey):
        self.apikey = apikey
        self.token_api = "https://token.nocaptchaai.com/token"
        self.headers = {"Content-Type": "application/json",
                        "apikey": self.apikey}

    def solve(self, payload):
        response = requests.post(
            self.token_api, json=payload, headers=self.headers)
        response_json = response.json()
        startTime = time.time()

        print("task status: ", response_json)
        print("waiting 7sec for response...")
        time.sleep(7)

        while True:
            sts = requests.get(
                response_json["url"], headers=self.headers).json()
            if sts["status"] == "processed" or sts["status"] == "failed":
                print(
                    f'time since request:- {int(time.time() - startTime)} seconds')
                print(f'status: {sts["status"]}\n{sts["token"]}')
                break

            print("status: ", sts["status"])
            time.sleep(2)


class OCR:
    def __init__(self, apikey):
        self.apikey = apikey
        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.apikey
        }

    def image_to_base64(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img_buffer = BytesIO()
        img.save(img_buffer, format='PNG')
        return base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    def solve(self, image_url):
        payload = {
            "method": "ocr",
            "image": self.image_to_base64(image_url)
        }

        try:
            response = requests.post(
                "https://pro.nocaptchaai.com/solve", json=payload, headers=self.headers)
            data = response.json()
            print(data['solution'])
        except Exception as error:
            print(f"Fetch error: {error}")
