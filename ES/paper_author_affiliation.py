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
    with open('/storage/GengHao/MAG/mag_20211108/mag/PaperAuthorAffiliations.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            cols = line.split('\t')
            
            entry = dict(
                paper_id = parse_int(cols[0]),
                author_id = parse_int(cols[1]),
                affiliation_id = parse_int(cols[2]),
                author_sequence_number = parse_int(cols[3]),
                original_author = parse_str(cols[4]),
                original_affiliation = parse_str(cols[5]),
            )

            yield entry 
            

def main():
    client = ESClient(
        host = 'localhost',
        port = 10000,
        password = '6GYZTyH6D3fR4Y', 
    )

    index = client.get_index('mag_paper_author_affiliation')
    index.delete_index()

    index.create_mapping(
        dict(
            paper_id = ESType.LONG,
            author_id = ESType.LONG,
            affiliation_id = ESType.LONG,
            author_sequence_number = ESType.LONG,
            original_author = ESType.KEYWORD_TEXT,
            original_affiliation = ESType.KEYWORD_TEXT,
        )
    )
    
    index.bulk_insert(read_file(), total=7_3158_7019)
            
            
if __name__ == '__main__':
    main() 
