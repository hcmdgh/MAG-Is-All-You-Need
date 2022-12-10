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
    with open('/storage/GengHao/MAG/mag_20211108/mag/Papers.txt', 'r', encoding='utf-8') as fp:
        for line in fp:
            cols = line.split('\t')
            
            entry = dict(
                _id = int(cols[0]),
                id = int(cols[0]),
                rank = parse_int(cols[1]),
                doi = parse_str(cols[2]),
                doc_type = parse_str(cols[3]),
                paper_title = parse_str(cols[4]),
                original_title = parse_str(cols[5]),
                book_title = parse_str(cols[6]),
                year = parse_int(cols[7]),
                date = parse_str(cols[8]),
                online_date = parse_str(cols[9]), 
                publisher = parse_str(cols[10]),
                journal_id = parse_int(cols[11]),
                conference_series_id = parse_int(cols[12]),
                conference_instance_id = parse_int(cols[13]),
                volume = parse_str(cols[14]),
                issue = parse_str(cols[15]),
                first_page = parse_str(cols[16]),
                last_page = parse_str(cols[17]),
                reference_count = parse_int(cols[18]),
                citation_count = parse_int(cols[19]),
                estimated_citation = parse_int(cols[20]),
                original_venue = parse_str(cols[21]),
                family_id = parse_int(cols[22]),
                family_rank = parse_int(cols[23]),
                doc_sub_types = parse_str(cols[24]),
                created_date = parse_str(cols[25]),
            )

            yield entry 
            

def main():
    client = ESClient(
        host = 'localhost',
        port = 10000,
        password = '6GYZTyH6D3fR4Y', 
    )

    index = client.get_index('mag_paper')
    index.delete_index()

    index.create_mapping(
        dict(
            id = ESType.LONG,
            rank = ESType.LONG,
            doi = ESType.KEYWORD,
            doc_type = ESType.KEYWORD,
            paper_title = ESType.KEYWORD_TEXT, 
            original_title = ESType.KEYWORD_TEXT, 
            book_title = ESType.KEYWORD_TEXT, 
            year = ESType.LONG,
            date = ESType.KEYWORD, 
            online_date = ESType.KEYWORD, 
            publisher = ESType.KEYWORD_TEXT,
            journal_id = ESType.LONG,
            conference_series_id = ESType.LONG,
            conference_instance_id = ESType.LONG,
            volume = ESType.KEYWORD, 
            issue = ESType.KEYWORD, 
            first_page = ESType.KEYWORD, 
            last_page = ESType.KEYWORD, 
            reference_count = ESType.LONG,
            citation_count = ESType.LONG,
            estimated_citation = ESType.LONG,
            original_venue = ESType.KEYWORD_TEXT, 
            family_id = ESType.LONG,
            family_rank = ESType.LONG,
            doc_sub_types = ESType.KEYWORD, 
            created_date = ESType.KEYWORD,
        )
    )
    
    index.bulk_insert(read_file(), total=2_6945_1039)
            
            
if __name__ == '__main__':
    main() 
