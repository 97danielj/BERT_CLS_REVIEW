import json
with open('./Crawling2/naver_서울 횟집_review_dic_page6.json','r', encoding ='utf-8') as f:
    review_dic = json.load(f)


print(review_dic.keys())
print(len(review_dic))
print(review_dic['한영상회'])



