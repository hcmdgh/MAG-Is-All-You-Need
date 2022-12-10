from es_util import * 
import csv 
from tqdm import tqdm 
from typing import Optional, Any 


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

    index = client.get_index('mag_rich_field')
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

            parent_fields = ESType.KEYWORD,
            parent_field_ids = ESType.LONG,
        )
    )
    
    parent_field_id_map: dict[int, int] = dict() 
    
    with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldOfStudyChildren.txt', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp.readlines()):
            cols = line.split('\t')
            field_id = int(cols[0])
            child_field_id = int(cols[1])
            
            assert child_field_id not in parent_field_id_map or parent_field_id_map[child_field_id] != field_id
            parent_field_id_map[child_field_id] = field_id

    field_map: dict[int, dict[str, Any]] = dict() 
    
    with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp.readlines()):
            cols = line.split('\t')

            field_id = int(cols[0])
            entry = dict(
                _id = field_id,
                id = field_id,
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
            
            assert field_id not in field_map
            field_map[field_id] = entry 
            
    for field_id, entry in tqdm(field_map.items()):
        parent_fields = []
        parent_field_ids = []
        
        _field_id = field_id 
        
        while True:
            parent_field_ids.insert(0, _field_id)
            parent_fields.insert(0, field_map[_field_id]['display_name'])
            
            if _field_id not in parent_field_id_map:
                break 
            
            _field_id = parent_field_id_map[_field_id]
            
        entry['parent_field_ids'] = parent_field_ids
        entry['parent_fields'] = parent_fields
        
    index.bulk_insert(list(field_map.values()))
            
            
if __name__ == '__main__':
    main() 
