import json
key_word_list = ['서울 횟집','인천 횟집', '부산 횟집', '대구 횟집', '광주 횟집', '대전 횟집', '울산 횟집']
# 빈 딕셔너리
last = {}
for key_word in key_word_list:
    for page_num in range(1,7):
        with open(f'./naver_review_with_rank/naver_{key_word}_review_dic_page{page_num}.json', 'r', encoding='utf-8') as f:
             #타겟 파일을 로드하고
             current = json.load(f)
             print('{}_{} : '.format(key_word,page_num) , len(current))
             # 계속 저장 시킬 딕셔너리에 업데이트
             last.update(current)

with open(f'./naver_횟집_by_metropolitan2.json', 'w', encoding='utf-8') as f:
    json.dump(last, f, indent=4, ensure_ascii=False)


print('총 매장 개수', len(last))


