import pickle 
from tqdm import tqdm 
from collections import defaultdict
import json 


def main():
    paper_id_set: set[int] = set() 
    paper_cite_map: dict[int, set[int]] = defaultdict(set)
    paper_cited_map: dict[int, set[int]] = defaultdict(set)
    
    with open('/home/Dataset/MAG/mag_20211108/mag/PaperReferences.txt', 'r') as fp:
        for line in tqdm(fp, total=19_3203_0797):
            columns = line.split('\t') 
            paper_id = int(columns[0])
            paper_ref_id = int(columns[1])

            paper_id_set.add(paper_id)
            paper_id_set.add(paper_ref_id)
            
            paper_cite_map[paper_id].add(paper_ref_id)
            paper_cited_map[paper_ref_id].add(paper_id)

    with open('./output/paper_citation_mapping.json', 'w') as fp:
        for paper_id in tqdm(paper_id_set):
            cite_ids = list(paper_cite_map[paper_id])
            cited_ids = list(paper_cited_map[paper_id])
            
            json_str = json.dumps(
                dict(
                    paper_id = paper_id, 
                    cite_ids = cite_ids,
                    cited_ids = cited_ids,
                )
            ).strip()
            
            print(json_str, file=fp)
            
            
if __name__ == '__main__':
    main() 
