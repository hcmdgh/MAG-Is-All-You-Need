from util import * 

FIELD_IDS = {154945302, 31972630, 31258907, 9390403, 11413529, 161191863, 136764020, 44154836, 79403827, 56739046, 178980831, 49774154, 124101348, 38652104, 23123220, 121684516, 77088390, 107457646, 120314980, 119857082, 2522767166, 76155785, 28490314, 149635348, 80444323, 204321447, 111919701, 115903868, 199360897, 108827166} 
YEAR_RANGE = range(0, 9999)
CITATION_THRESHOLD = 3 


def main():
    print(f"筛选领域数：{len(FIELD_IDS)}")

    paper_field_map: dict[int, list[int]] = dict() 
    
    with open('./output/paper_field_mapping.tsv', 'r') as fp:
        for line in tqdm(fp):
            paper_id, field_ids = line.split('\t')
            paper_id = int(paper_id)
            field_ids = [int(x) for x in field_ids.split(',')]
            paper_field_map[paper_id] = field_ids 
            
    chosen_paper_list: list[dict[str, Any]] = []

    for paper in iterate_papers():
        paper_id = paper['id']
        paper_year = paper['year']
        paper_doc_type = paper['doc_type']
        paper_journal_id = paper['journal_id']
        paper_conference_id = paper['conference_id']
        
        if paper_year not in YEAR_RANGE:
            continue
        
        if not paper_journal_id and not paper_conference_id:
            continue
        
        paper_field_ids = set(paper_field_map.get(paper_id, [])) 
        if not (paper_field_ids & FIELD_IDS):
            continue
            
        chosen_paper_list.append(paper)   
        
    print(f"按照领域、年份筛选后的论文数量：{len(chosen_paper_list)}")         
        

if __name__ == '__main__':
    main() 
