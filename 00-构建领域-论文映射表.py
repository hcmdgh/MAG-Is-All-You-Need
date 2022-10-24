import pickle 
from tqdm import tqdm 
from collections import defaultdict
import json 


def main():
    paper_field_map: dict[int, set[int]] = defaultdict(set)
    field_paper_map: dict[int, set[int]] = defaultdict(set)
    
    with open('/home/Dataset/MAG/mag_20211108/advanced/PaperFieldsOfStudy.txt', 'r') as fp:
        for line in tqdm(fp, total=15_4656_1902):
            columns = line.split('\t') 
            paper_id = int(columns[0])
            field_id = int(columns[1])

            paper_field_map[paper_id].add(field_id)
            field_paper_map[field_id].add(paper_id)

    with open('./output/paper_field_mapping.json', 'w') as fp:
        for paper_id, field_ids in tqdm(paper_field_map.items()):
            json_str = json.dumps(
                dict(
                    paper_id = paper_id, 
                    field_ids = list(field_ids), 
                )
            ).strip() 
            
            print(json_str, file=fp)
            
    with open('./output/field_paper_mapping.json', 'w') as fp:
        for field_id, paper_ids in tqdm(field_paper_map.items()):
            json_str = json.dumps(
                dict(
                    field_id = field_id, 
                    paper_ids = list(paper_ids), 
                )
            ).strip() 
            
            print(json_str, file=fp)
            
            
if __name__ == '__main__':
    main() 
