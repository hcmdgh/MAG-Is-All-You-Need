from tqdm import tqdm 
import json 
from typing import Any 

MAG_PAPER_CNT = 2_6945_1039

# 领域
FIELD_IDS = {154945302, 31972630, 31258907, 9390403, 11413529, 161191863, 136764020, 44154836, 79403827, 56739046, 178980831, 49774154, 124101348, 38652104, 23123220, 121684516, 77088390, 107457646, 120314980, 119857082, 2522767166, 76155785, 28490314, 149635348, 80444323, 204321447, 111919701, 115903868, 199360897, 108827166} 

# 年份
YEAR_RANGE = range(0, 9999)

# 引用数
CITATION_THRESHOLD = 5 


def main():
    print(f"筛选领域数：{len(FIELD_IDS)}")

    chosen_paper_cnt = 0 

    with open('./output/chosen_paper.json', 'w', encoding='utf-8') as w:
        with open('./output/paper_with_field_citation_author.json', 'r', encoding='utf-8') as r:
            for line in tqdm(r, total=MAG_PAPER_CNT):
                line = line.strip()
                paper = json.loads(line)

                paper_id = paper['id']
                paper_year = paper['year']
                paper_journal_id = paper['journal_id']
                paper_conference_id = paper['conference_id']
                paper_field_ids = set(paper['field_ids']) 
                paper_citation_count = paper['citation_count']
                
                # 按领域筛选
                if not (paper_field_ids & FIELD_IDS):
                    continue
                
                # 按年份筛选
                if paper_year not in YEAR_RANGE:
                    continue
                
                # 按引用数筛选
                if paper_citation_count < CITATION_THRESHOLD:
                    continue
                
                # 必须是期刊或会议论文
                if not paper_journal_id and not paper_conference_id:
                    continue
                
                print(line, file=w)
                chosen_paper_cnt += 1 
        
    print(f"筛选前论文数量：{MAG_PAPER_CNT}")  
    print(f"筛选后论文数量：{chosen_paper_cnt}")  


if __name__ == '__main__':
    main() 
