from prettytable import PrettyTable
from tqdm import tqdm 

TOP_FIELD_ID = 41008148


def main():
    field_id_set = set()  
    
    with open('/home/Dataset/MAG/mag_20211108/advanced/FieldOfStudyChildren.txt', 'r') as fp:
        for line in tqdm(fp):
            columns = line.split('\t')
            field_id = int(columns[0])
            child_field_id = int(columns[1])

            if field_id == TOP_FIELD_ID:
                field_id_set.add(child_field_id)
    
    field_list = [] 
    
    with open('/home/Dataset/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r') as fp:
        for line in tqdm(fp):
            columns = line.split('\t')
            field_id = int(columns[0])
            field_name = columns[3].strip() 
            field_level = int(columns[5])
            paper_count = int(columns[6])
            
            if field_id in field_id_set:
                assert field_level == 1 
                
                field_list.append(
                    dict(
                        field_id = field_id, 
                        field_name = field_name,
                        paper_count = paper_count, 
                    )
                )

    field_list.sort(key=lambda x: -x['paper_count'])
    
    table = PrettyTable(
        field_names = ['ID', 'Field Name', 'Paper Count'],
    )
    
    for item in field_list:
        table.add_row([item['field_id'], item['field_name'], item['paper_count']])

    print(table)
    
    print(f"二级领域总数：{len(field_list)}")
    

if __name__ == '__main__':
    main() 
