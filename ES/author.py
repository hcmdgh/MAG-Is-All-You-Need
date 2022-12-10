from es_util import * 
import csv 
from tqdm import tqdm 
from typing import Optional, Iterator, Any 


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
    
    
def read_file() -> Iterator[dict[str, Any]]:
    with open('/storage/GengHao/MAG/mag_20211108/mag/Authors.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            cols = line.split('\t')
            
            entry = dict(
                _id = int(cols[0]),
                id = int(cols[0]),
                rank = parse_int(cols[1]),
                normalized_name = parse_str(cols[2]),
                display_name = parse_str(cols[3]),
                last_known_affiliation_id = parse_int(cols[4]),
                paper_count = parse_int(cols[5]),
                paper_family_count = parse_int(cols[6]),
                citation_count = parse_int(cols[7]),
                created_date = parse_str(cols[8]),
            )

            yield entry 
            

def main():
    client = ESClient(
        host = 'localhost',
        port = 10000,
        password = '6GYZTyH6D3fR4Y', 
    )

    index = client.get_index('mag_author')
    index.delete_index()

    index.create_mapping(
        dict(
            id = ESType.LONG,
            rank = ESType.LONG,
            normalized_name = ESType.KEYWORD_TEXT,
            display_name = ESType.KEYWORD_TEXT,
            last_known_affiliation_id = ESType.LONG,
            paper_count = ESType.LONG,
            paper_family_count = ESType.LONG,
            citation_count = ESType.LONG,
            created_date = ESType.KEYWORD,
        )
    )
    
    index.bulk_insert(read_file(), total=2_8005_0502)
            
            
if __name__ == '__main__':
    main() 
