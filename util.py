from tqdm import tqdm 
from typing import Iterator, Any, Optional 


def parse_int(obj) -> Optional[int]:
    try:
        return int(obj)
    except Exception:
        return None 


def iterate_papers() -> Iterator[dict[str, Any]]:
    with open('/home/Dataset/MAG/mag_20211108/mag/Papers.txt', 'r') as fp:
        for line in tqdm(fp, total=2_6945_1039):
            columns = line.split('\t')
            
            yield dict(
                id = int(columns[0]),
                rank = parse_int(columns[1]),
                doi = columns[2].strip(),
                doc_type = columns[3].strip(),
                title = columns[5].strip(),
                year = parse_int(columns[7]), 
                journal_id = parse_int(columns[11]), 
                conference_id = parse_int(columns[12]), 
                citation_count = parse_int(columns[19]),  
            )
