import pickle 
from tqdm import tqdm 
from collections import defaultdict
import json 


def main():
    paper_author_map: dict[int, list[dict]] = defaultdict(list) 
    
    with open('/home/Dataset/MAG/mag_20211108/mag/PaperAuthorAffiliations.txt', 'r') as fp:
        for line in tqdm(fp, total=7_3158_7019):
            columns = line.split('\t') 
            paper_id = int(columns[0])
            author_id = int(columns[1])
            try:
                affiliation_id = int(columns[2])
            except ValueError:
                affiliation_id = None 
            author_seq = int(columns[3])
            
            paper_author_map[paper_id].append(
                dict(
                    author_id = author_id,
                    affiliation_id = affiliation_id,
                    author_seq = author_seq, 
                )
            )
            
    with open('./output/paper_author_mapping.json', 'w') as fp:
        for paper_id, author_list in tqdm(paper_author_map.items()):
            json_str = json.dumps(
                dict(
                    paper_id = paper_id, 
                    author_list = author_list,  
                )
            ).strip() 
            
            print(json_str, file=fp)


if __name__ == '__main__':
    main() 
