import pymysql 
from pymysql.cursors import DictCursor
import os 
import csv 
from tqdm import tqdm 

conn = pymysql.connect(
    host = 'localhost',
    port = 12345,
    user = 'root',
    password = os.getenv('MYSQL_PASSWORD', ''),
    database = 'MAG',
    charset = 'utf8mb4',
    cursorclass = DictCursor,
    autocommit = True, 
)

with conn:
    with conn.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS MAG.field")
        cursor.execute("""
            CREATE TABLE MAG.field (
                id BIGINT PRIMARY KEY,
                `rank` BIGINT, 
                normalized_name TEXT, 
                display_name TEXT, 
                main_type TEXT, 
                level BIGINT, 
                paper_count BIGINT, 
                paper_family_count BIGINT, 
                citation_count BIGINT, 
                created_date TEXT
            );
        """)

        with open('/storage/GengHao/MAG/mag_20211108/advanced/FieldsOfStudy.txt', 'r', encoding='utf-8') as fp:
            reader = csv.reader(fp, delimiter='\t')
    
            for row in tqdm(reader):
                cursor.execute(
                    f"INSERT INTO MAG.field VALUES ({', '.join(['%s'] * len(row))})",
                    list(row), 
                )
