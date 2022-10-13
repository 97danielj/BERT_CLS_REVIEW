import json
key_word_list = ['서울 횟집','인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
#page_num = 5

for page_num in range(1,4):
    for key_word in key_word_list:
        with open(f'./naver_review_with_rank/naver_{key_word}_review_dic_page{page_num}.json','r', encoding ='utf-8') as f:
            review_dic = json.load(f)
        print(f'키워드 : {key_word}, page : {page_num}')
        print(len(review_dic))

#key_word = key_word_list[-1]
#with open(f'./Crawling2/naver_{key_word}_review_dic_page{page_num}.json', 'r', encoding='utf-8') as f:
    #review_dic = json.load(f)

#print(review_dic.keys())
#print(len(review_dic))



