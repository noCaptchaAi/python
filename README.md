# noCaptchaAI.com

A Python library for solving captchas using noCaptchaAi.com

## Installation

Pending (`pip install nocaptchaai` ) until PyPi Admin Enables new projects.



## Example

```py
from nocaptchaai.main import qCaptchaToken, OCR

apikey = "apikey" # https://dash.nocaptchaai.com/
image_url = "https://cdn.discordapp.com/attachments/997770328275165224/1109737255494484050/captcha.png"


# OCR
ocr = OCR(apikey)
ocr.solve(image_url)


# qCaptcha Token

payload = {
    # "proxy": {
    #     "ip": "123.45.678.9",
    #     "port": 1234,
    #     "username": "userid",
    #     "password": "pass#=#rd",
    #     "type": "https"
    # },
    # "rqdata": "eyJ0zI1NiJ9.eyJmIjowLCJ....",
    "type": "qcaptcha",
    "url": "accounts.qcaptcha.com",
    "sitekey": "7830874c-13ad-4cfe-98d7-e8b019dc1742",
    "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
token = hCaptchaToken(apikey)
token.solve(payload)
```

## Response

```
$ python example.py

>>>

77325
task status:  {'id': 'h_tok_ECjqkKCfrIH9q19q', 'message': 'Task created.', 'status': 'created', 'url': 'https://pro.nocaptchaai.com/token?id=h_tok_ECjqkKCfrIH9q19q'}
waiting 7sec for response...
status:  processing
status:  processing
time since request:- 13 seconds
status: processed
P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQcpBnHwrBVQBVDa_PBa39xXp7lB6i1opIJq1vrMTn0ej9QAgBZOkC1R5nwEoBCNaMSt8_O28h9oKf_PsguZdsNRgLYi5eUkRMzTVjnDtUPX9sLEhz3hjk1_dSCzR22cU1wI_mBauj65MV8C0xS-ZeMo5DO1wKUTsZiv9w7e8KmJl3_lUN5BrGCX6GTC7Z3Bz8q7Q3O3-whyE-ydZk-gy190tSMvZyDWLE1ada9xteMDi1sAfohkhot03fVOT3h3fFAaTb1UXp-C2f0YaDYaF9iOEZU12Vi006IWy6lSeu0C6t-3WdBBo4mO0-_GmfR-6KW-Dxt7ZoAisenDSEapW1YggY_YMTW7PkzKnMcolekd5GCOUC9szMWfsHu4UoVzYA1r8FaCKWJBxa_oFYbP6apCgT6-kyS80rdF-ybTtlwxetRNlbkGCXdDxbSg_EbIq_X8LWRuaIU8qc_Efqrq6rKSCUXzp3PaS_hDTmx_4WwFNWYAaf45GecXQtRFPEtiQ-pECFoWtKx4JS-9CmD982heBXqyEpfCBDWP_cukYML8CqrK5fyuKKM4zwsd5k8Rbc6GScFN-mKB4lflbEXFTH89VePWgzOxHleZmUbmfM4DvLt7Ke9VkAzMAuiwrisiVCku-d_HrLeEoWPzYvXAK5QNycxEXR6aPKRHrHVKTPc-b8PZA_q_VDbktnkh1f2DKSPd6K-XV_jYihBQ0KQ-snGSmuQLg5MjIDDQHA_E0Pb28edeP4-WJD7tkK5qF8zR7wS3U8RQ1maJQSc5g82FnMs7uNc9R9Cioa8ezgqkiu5EZ9kgybhZwcrYJizz-IxzWkldb3wPk-FtxV8XpOMxhZC_t-WbtrXbb9whWz8JykdFVHyBPGiNMwl_JLxQpRasR4M7j84WFNjEwnCkO4cTAdCYWhYGWDEwdBsNcHxRVMGYz0wSqp9CLvNurlwe8IUQITEGXVi3YlUAC33KSVMAYVk_SXgYCnfox197FkVQk2ShIyrJV1onpLsmMLZMicXb1xenDkT2useQNGCL8dZG8NBNyz_qZI1L1ilVwsUjWc6_mcEl5h7aTI9qhSDACZxJPRxgCUh3-2dOIyOmc2hpZZlXhIea1T6yE9egdDl1Ke40RFmHTrahfqtiQU2kz2-wQluXbLQMGPItIS3MT9PAsrrMEv59eRLuzn891av4IOyZla8VdlzqJDKqhXpYtLGngMBxJQvYi1qmxCSaEb-p0kqyrfboaA74Ujkeu_dhsLQWcgjwUeCOJHcr-eUeeLt1GKSGbf53w51_y08cOoBo7v8-3yyEA0eNhm1H38Qpku0enz-MBqFRDKGJJEgRW7KZqFwqmlUS3ZYLnJrNp-xXlGdrCSK1CcRvEauk7ZJroySZJ4Zzo6R4A6TbRcZTt2aaOXQO-mdcWRAMdObDTt2o7D07ehZ_O6fjNMUtFaOeIs1nEtpdyC6V76rz72C8WYGkiFlhluea11Yv5oHtYIn2KzSOkSr7TMSWdVD4ZY_Bnjm0HhKDxhRVca2Ff9BDA0N4mrcE1UBXFiM14zeZaEAUGbxHQGKV5wnLiCLEeHrJ08Cbfa9z62va1IPem9BswlPj3z8NUo76p7VQ6gQdQtylWv4qb_hcPsdG-vrjXfVkQX2WDzwru5918-StGfyQ-aGZPRXxQpz-L8Vu54Vhfr7meb-2hP-75Hz92yaYorro5WcYfcky6OT33pubYtJROSG-9yAOtY8Kj23uAMx5TUx7eabDWYCNMxGNbB6yg01MXn5Wpi6Myn2DZ-wbvpkVxf4_W_c6_AhihYKCcMYIrY0nKZr1pVJS6cqWAHawRgQDHgpwl9u_t_4vy4zW_Nrso3Neoaw_7wMsjdNuFgHa3qE796o-Bz5ZRBxzDhoquX-0G_Qq55VJ8j43LfdEAfFQ4xcWwXg1RJ80jRERqa9S61Q8FM2_DKyAkxrYQuS9ZD0HxN8Rw5guP7wuy5piGbXE_gKai8q19bJvVb704DXMC1seeaE0guDMqHirHZuyACG8y2jb_w3tfDP5LHuK09HPJI7qaQGddN5-ImV5I6R6gsezPpO2Qoni3HM9R2bhISNMif7Q-bqD6SedNVblxZfYCgbdsy2xmKX1B8CW6xFEbShdj--emyOYZzCJIDXsb1STEh0JBe9UsxiNbz-1DAIwBd4_j3n23oHwhwHrLRGWU2hYPRwBQA6I-XIbx-5DVVCljuhuyMe5qkoJvtsOp6SUf2b729zio_3wXDXeM4_A-usLlO9RHfsrBK7n2uww6GQzhVlU2pnxiKEHoY-RBUIIQAzzZCq4JYc_kOZe1TUBy6YXvzSSkusNo691mg5G223T30m3bKdNLFaxGkS1ofc7c60vbCgJSbkgmE8JBwOaSLr_Orh2Vi1S7X536tbr3QSJsjuj8sI1InSR0Sm4MTovNtseMeC0zHY5ujAJ_2PXo2V4cM5kacW6qHNoYXJkX2lkzg9y6m-icGQA.SEjVGisumFSgjOkIWR-6LX3Btgl7Fj6KgTzL_ohLXmA
```


Dependencies
This library requires the following dependencies:

```py
requests
Pillow
```


License
This project is licensed under the MIT License.

Authors
noCaptchaAi (oss@nocaptchaai.com)
