## 참고 사이트
# https://s1mcoding.tistory.com/82

import os
import openai

# openAPI 공식홈페이지 제공 고유 key
openai.api_key = ""

# completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role" : "user", "content": "챗GPT가 무엇인지 설명"}
#     ]
# )
#
# # 챗GPT가 무엇인지 설명
# print(completion.choices[0].message.content)


question = input("무엇이든 물어보세요: ")
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question}
    ]
)

print(completion.choices[0].message.content)