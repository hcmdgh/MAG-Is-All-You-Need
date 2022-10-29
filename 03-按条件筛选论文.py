from tqdm import tqdm 
import json 
from typing import Any, Optional
import sys 
import csv 
import os 
import multiprocessing as mp 
import time 

# 领域
L0_FIELD_ID = 41008148
L1_FIELD_IDS = {154945302, 31972630, 31258907, 9390403, 11413529, 161191863, 136764020, 44154836, 79403827, 56739046, 178980831, 49774154, 124101348, 38652104, 23123220, 121684516, 77088390, 107457646, 120314980, 119857082, 2522767166, 76155785, 28490314, 149635348, 80444323, 204321447, 111919701, 115903868, 199360897, 108827166} 

# 年份
YEAR_RANGE = range(0, 9999)

# 引用数
CITATION_THRESHOLD = 5 


def filter_papers(path: str) -> list[str]:
    chosen_paper_list = [] 
    
    with open(path, 'r', encoding='utf-8') as r:
        for line in r:
            line = line.strip() 
            paper = json.loads(line)
            
            paper_id = paper['id'] 
            paper_year = paper['year']
            paper_journal_id = paper['journal_id']
            paper_conference_id = paper['conference_id'] 
            paper_field_ids = set(paper['field_ids'])
            paper_citation_count = paper['citation_count']
            
            # 按领域筛选
            if not (paper_field_ids & L1_FIELD_IDS):
                continue
            
            # 按年份筛选
            if paper_year not in YEAR_RANGE:
                continue
            
            # 按引用数筛选
            if not paper_citation_count or paper_citation_count < CITATION_THRESHOLD:
                continue
            
            # 必须是期刊或会议论文
            if not paper_journal_id and not paper_conference_id:
                continue
            
            chosen_paper_list.append(line)
            
    # print(f"【筛选完毕】{path}")

    return chosen_paper_list 


def main():
    start_time = time.time()
    
    print(f"筛选领域数：{len(L1_FIELD_IDS)}")

    file_paths = [] 
    
    for year in YEAR_RANGE:
        file_path = f"./output/paper_in_field_year/paper_field_{L0_FIELD_ID}_year_{year}.json"
        
        if os.path.isfile(file_path):
            file_paths.append(file_path)

    pool = mp.Pool(processes=16)
    
    process_result_dict = dict() 
    
    for file_path in file_paths:
        process_result = pool.apply_async(filter_papers, kwds=dict(path=file_path))
        process_result_dict[file_path] = process_result 
        
    chosen_paper_cnt = 0 
        
    with open('./output/chosen_paper.json', 'w', encoding='utf-8') as fp:
        with tqdm(process_result_dict.items()) as tqdm_:
            for path, process_result in tqdm_:
                tqdm_.set_description(path)
                
                chosen_paper_list = process_result.get()
                
                for line in chosen_paper_list:
                    chosen_paper_cnt += 1 
                    print(line, file=fp)
        
    pool.close()
    pool.join() 
            
    print(f"筛选后论文数量：{chosen_paper_cnt}")  
    print(f"耗时：{int(time.time() - start_time)} s")


if __name__ == '__main__':
    main() 
