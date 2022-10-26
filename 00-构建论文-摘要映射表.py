from tqdm import tqdm 
import json 

PATH_LIST = [
    '/home/Dataset/MAG/mag_20211108/nlp/PaperAbstractsInvertedIndex.txt.1',
    '/home/Dataset/MAG/mag_20211108/nlp/PaperAbstractsInvertedIndex.txt.2',
    '/home/Dataset/MAG/mag_20211108/nlp/PaperAbstractsInvertedIndex.txt.3',
    '/home/Dataset/MAG/mag_20211108/nlp/PaperAbstractsInvertedIndex.txt.4',
    '/home/Dataset/MAG/mag_20211108/nlp/PaperAbstractsInvertedIndex.txt.5',
]


def main():
    paper_id_set = set() 
    
    with open('./output/paper_abstract_mapping.tsv', 'w', encoding='utf-8') as w:
        for path in tqdm(PATH_LIST):
            with open(path, 'r', encoding='utf-8') as r:
                for line in tqdm(r):
                    paper_id, paper_abstract_dict = line.split('\t')
                    paper_id = int(paper_id)
                    paper_abstract_dict = json.loads(paper_abstract_dict)

                    assert paper_id not in paper_id_set
                    paper_id_set.add(paper_id)
                    
                    word_cnt = paper_abstract_dict['IndexLength']
                    word_list = [''] * word_cnt 
                    
                    for word, idxs in paper_abstract_dict['InvertedIndex'].items():
                        for idx in idxs:
                            word_list[idx] = word 
                            
                    abstract = ' '.join(word_list)

                    json_str = json.dumps(
                        dict(
                            paper_id = paper_id, 
                            abstract = abstract, 
                        ),
                        ensure_ascii = False, 
                    ).strip() 
                    
                    print(json_str, file=w)


if __name__ == '__main__':
    main() 
