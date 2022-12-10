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
    
    
def parse_float(s: str) -> Optional[float]:
    s = s.strip() 
    
    if s:
        return float(s)  
    else:
        return None 


def main():
    client = ESClient(
        host = 'localhost',
        port = 10000,
        password = '6GYZTyH6D3fR4Y', 
    )

    index = client.get_index('mag_affiliation')
    index.delete_index()

    index.create_mapping(
        dict(
            id = ESType.LONG,
            rank = ESType.LONG,
            normalized_name = ESType.KEYWORD_TEXT,
            display_name = ESType.KEYWORD_TEXT,
            grid_id = ESType.KEYWORD,
            official_page = ESType.KEYWORD,
            wiki_page = ESType.KEYWORD,
            paper_count = ESType.LONG,
            paper_family_count = ESType.LONG,
            citation_count = ESType.LONG,
            iso_3166_code = ESType.KEYWORD,
            latitude = ESType.DOUBLE,
            longitude = ESType.DOUBLE,
            created_date = ESType.KEYWORD,
        )
    )
    
    with open('/storage/GengHao/MAG/mag_20211108/mag/Affiliations.txt', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp.readlines()):
            cols = line.split('\t')
            
            entry = dict(
                _id = int(cols[0]),
                id = int(cols[0]),
                rank = parse_int(cols[1]),
                normalized_name = parse_str(cols[2]),
                display_name = parse_str(cols[3]),
                grid_id = parse_str(cols[4]),
                official_page = parse_str(cols[5]),
                wiki_page = parse_str(cols[6]),
                paper_count = parse_int(cols[7]),
                paper_family_count = parse_int(cols[8]),
                citation_count = parse_int(cols[9]),
                iso_3166_code = parse_str(cols[10]),
                latitude = parse_float(cols[11]),
                longitude = parse_float(cols[12]),
                created_date = parse_str(cols[13]),
            )
            
            index.insert(entry)
            
            
if __name__ == '__main__':
    main() 
