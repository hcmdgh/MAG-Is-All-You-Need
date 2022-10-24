from prettytable import PrettyTable
from tqdm import tqdm 


def main():
    field_list = [] 
    
    with open('/home/Dataset/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r') as fp:
        for line in tqdm(fp):
            columns = line.split('\t')
            id = int(columns[0])
            field_name = columns[3].strip() 
            level = int(columns[5])
            paper_count = int(columns[6])
            
            if level == 0:
                field_list.append(
                    dict(
                        id = id, 
                        field_name = field_name,
                        paper_count = paper_count, 
                    )
                )

    field_list.sort(key=lambda x: -x['paper_count'])
    
    table = PrettyTable(
        field_names = ['ID', 'Field Name', 'Paper Count'],
    )
    
    for item in field_list:
        table.add_row([item['id'], item['field_name'], item['paper_count']])

    print(table)
    

if __name__ == '__main__':
    main() 
