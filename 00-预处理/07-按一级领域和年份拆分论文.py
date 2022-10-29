import csv 
import json 
from tqdm import tqdm 
import io 


def main():
    L0_field_id_set = set() 
    
    with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')

        for row in reader:
            field_id = int(row[0])
            field_level = int(row[5])
            
            if field_level == 0:
                L0_field_id_set.add(field_id)
                
    assert len(L0_field_id_set) == 19 

    fp_dict: dict[tuple[int, int], io.TextIOWrapper] = dict()
    fp_dict[-1, -1] = open('./output/paper_in_field_year/paper_unrelated.json', 'w', encoding='utf-8')
    
    with open('./output/paper_with_field_citation_author.json', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp, total=2_6945_1039):
            line = line.strip() 
            paper = json.loads(line)
            year = int(paper['year']) if paper['year'] else None 
            field_ids = set(paper['field_ids']) 
            L0_field_ids = field_ids & L0_field_id_set

            if year and L0_field_ids:
                for field_id in L0_field_ids:
                    if (field_id, year) not in fp_dict:
                        fp_dict[field_id, year] = open(f"./output/paper_in_field_year/paper_field_{field_id}_year_{year}.json", 'w', encoding='utf-8')
                    
                    fp = fp_dict[field_id, year]
                    print(line, file=fp, flush=True)
            else:
                print(line, file=fp_dict[-1, -1], flush=True)
            
    for fp in fp_dict.values():
        fp.close()         
             

if __name__ == '__main__':
    main() 
