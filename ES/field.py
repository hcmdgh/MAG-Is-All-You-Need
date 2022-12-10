from es_util import * 
import csv 
from tqdm import tqdm 
from typing import Optional 


def parse_str(s: str) -> Optional[str]:
    s = s.strip() 
    
    if s:
        return s 
    else:
        return None 
    
    
def parse_int(s: str) -> Optional[int]:
    s = s.strip() 
    
    if s:
        return int(s)  
    else:
        return None 


def main():
    client = ESClient(
        host = 'localhost',
        port = 10000,
        password = '6GYZTyH6D3fR4Y', 
    )

    index = client.get_index('mag_field')
    index.delete_index()

    index.create_mapping(
        dict(
            id = ESType.LONG,
            rank = ESType.LONG,
            normalized_name = ESType.KEYWORD_TEXT,
            display_name = ESType.KEYWORD_TEXT,
            main_type = ESType.KEYWORD,
            level = ESType.LONG,
            paper_count = ESType.LONG,
            paper_family_count = ESType.LONG,
            citation_count = ESType.LONG,
            created_date = ESType.KEYWORD,
        )
    )
    
    entry_list = [] 
    
    with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp.readlines()):
            cols = line.split('\t')
            
            entry = dict(
                _id = int(cols[0]),
                id = int(cols[0]),
                rank = parse_int(cols[1]),
                normalized_name = parse_str(cols[2]),
                display_name = parse_str(cols[3]),
                main_type = parse_str(cols[4]),
                level = parse_int(cols[5]),
                paper_count = parse_int(cols[6]),
                paper_family_count = parse_int(cols[7]),
                citation_count = parse_int(cols[8]),
                created_date = parse_str(cols[9]),
            )
            
            entry_list.append(entry)
            
    index.bulk_insert(entry_list)
            
            
if __name__ == '__main__':
    main() 
