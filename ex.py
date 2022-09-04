import json
with open('./Crawling2/naver_울산 횟집_review_dic_page1.json', encoding ='utf-8') as f:
    review_dic = json.load(f)


print(review_dic.keys())
print(len(review_dic))
print(review_dic['부산횟집'])


