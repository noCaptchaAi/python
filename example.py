from nocaptchaai.main import hCaptchaToken, OCR

apikey = "apikey"
image_url = "https://cdn.discordapp.com/attachments/997770328275165224/1109737255494484050/captcha.png"


# OCR
ocr = OCR(apikey)
ocr.solve(image_url)


# hCaptcha Token

payload = {
    # "proxy": {
    #     "ip": "123.45.678.9",
    #     "port": 1234,
    #     "username": "userid",
    #     "password": "pass#=#rd",
    #     "type": "https"
    # },
    # "rqdata": "eyJ0zI1NiJ9.eyJmIjowLCJ....",
    "type": "hcaptcha",
    "url": "accounts.hcaptcha.com",
    "sitekey": "7830874c-13ad-4cfe-98d7-e8b019dc1742",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
token = hCaptchaToken(apikey)
token.solve(payload)
