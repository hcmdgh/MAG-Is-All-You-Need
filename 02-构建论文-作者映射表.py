import pickle 
from tqdm import tqdm 
from collections import defaultdict
import json 


def main():
    paper_author_map: dict[int, list[dict[str, int]]] = defaultdict(list) 
    
    with open('/home/Dataset/MAG/mag_20211108/mag/PaperReferences.txt', 'r') as fp:
        for line in tqdm(fp, total=19_3203_0797):
            columns = line.split('\t') 


if __name__ == '__main__':
    pass 
