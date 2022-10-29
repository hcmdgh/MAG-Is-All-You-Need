import json
import csv  
from tqdm import tqdm 
from pprint import pprint 

PAPER_FIELDS = [
    'id', 
    'rank',
    'doi',
    'doc_type',
    'title', 
    'original_title', 
    'book_title', 
    'year',
    'date',  
    'online_date',
    'publisher',
    'journal_id',
    'conference_id',
    'conference_instance_id',
    'volume',
    'issue',
    'first_page',
    'last_page',
    'reference_count',
    'citation_count', 
    'estimated_citation',
    'original_venue', 
    'family_id',
    'family_rank',
    'doc_sub_types', 
    'created_date', 
    
    'field_ids',  
    'cite_paper_ids',  
    'cited_paper_ids', 
    'author_list',    
]


def main():
    with open('./output/paper_enriched.tsv', 'w', encoding='utf-8') as w:
        writer = csv.DictWriter(w, delimiter='\t', fieldnames=PAPER_FIELDS)
        writer.writeheader()
        
        with open('./output/paper_with_field_citation_author.json', 'r', encoding='utf-8') as r:
            for line in tqdm(r, total=2_6945_1039):
                paper = json.loads(line)
            
                field_ids = paper['field_ids']
                cite_paper_ids = paper['cite_paper_ids']
                cited_paper_ids = paper['cited_paper_ids']
                author_list = paper['author_list']
                
                field_ids = ','.join(str(x) for x in field_ids)
                cite_paper_ids = ','.join(str(x) for x in cite_paper_ids)
                cited_paper_ids = ','.join(str(x) for x in cited_paper_ids)
                
                s_list = [] 
                for author in author_list:
                    author_id = author['author_id']
                    affiliation_id = author['affiliation_id']
                    author_seq = author['author_seq']
                    
                    s = '|'.join(str(x) if x else '' for x in [author_id, affiliation_id, author_seq])
                    s_list.append(s)
                    
                paper['field_ids'] = field_ids
                paper['cite_paper_ids'] = cite_paper_ids
                paper['cited_paper_ids'] = cited_paper_ids
                paper['author_list'] = ','.join(s_list)
                
                writer.writerow(paper)

            
if __name__ == '__main__':
    main() 
