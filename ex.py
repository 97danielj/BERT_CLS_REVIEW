import json
key_word_list = ['서울 횟집','인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
#page_num_ex = 3

for page_num in range(1,7):
    for key_word in key_word_list:
        print(f'key_word : {key_word}, page_num : {page_num}')
        with open(f'naver/naver_{key_word}_review_dic_page{page_num}.json', 'r', encoding ='utf-8') as f:
            review_dic = json.load(f)
        print(len(review_dic))
'''
for key_word in key_word_list:
    with open(f'./naver/naver_{key_word}_review_dic_page{page_num_ex}.json', 'r', encoding='utf-8') as f:
        review_dic = json.load(f)
    print(len(review_dic))
    print(review_dic.keys())
'''

