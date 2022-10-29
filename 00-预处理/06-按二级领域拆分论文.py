import csv 
import json 
from tqdm import tqdm 


def main():
    L1_field_id_set = set() 
    
    with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r', encoding='utf-8') as fp:
        reader = csv.reader(fp, delimiter='\t')

        for row in reader:
            field_id = int(row[0])
            field_level = int(row[5])
            
            if field_level == 1:
                L1_field_id_set.add(field_id)
                
    assert len(L1_field_id_set) == 292 

    fp_dict = {
        field_id: open(f"./output/paper_in_field/paper_in_field_{field_id}.json", 'w', encoding='utf-8')
        for field_id in L1_field_id_set
    }
    fp_dict[-1] = open("./output/paper_in_field/paper_unrelated.json", 'w', encoding='utf-8')
    
    with open('./output/paper_with_field_citation_author.json', 'r', encoding='utf-8') as fp:
        for line in tqdm(fp, total=2_6945_1039):
            line = line.strip() 
            paper = json.loads(line)
            field_ids = set(paper['field_ids']) 

            if field_ids & L1_field_id_set:
                for field_id in field_ids & L1_field_id_set:
                    fp = fp_dict[field_id]
                    print(line, file=fp)
            else:
                print(line, file=fp_dict[-1])
            
    for fp in fp_dict.values():
        fp.close()         
             

if __name__ == '__main__':
    main() 
