#import json
#key_word_list = ['서울 횟집','인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
#page_num = 5
'''
#for key_word in key_word_list:
    with open(f'./Crawling2/naver_{key_word}_review_dic_page{page_num}.json','r', encoding ='utf-8') as f:
        review_dic = json.load(f)
    print(len(review_dic))
'''
#key_word = key_word_list[-1]
#with open(f'./Crawling2/naver_{key_word}_review_dic_page{page_num}.json', 'r', encoding='utf-8') as f:
#    review_dic = json.load(f)

#print(review_dic.keys())
#print(len(review_dic))
import pickle
import json
#with open('./mango_dict.pickle','rb') as f:
#    mango_dict = pickle.load(f)
#with open('./mango_dict.json','w', encoding='utf-8') as f:
#    json.dump(mango_dict, f, indent=4, ensure_ascii=False)

#print(mango_dict)

with open('./mango_dict.json','r', encoding='utf-8') as f:
    mango_dict = json.load(f)
mango_dict




