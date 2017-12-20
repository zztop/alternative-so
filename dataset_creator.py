class SoDatasetCreator:
    """Create dataset for SO"""

    def __init__(self):
        pass



    @staticmethod
    def create_dataset(dataset_name):
        '''
        Creates a Line Corpus and generates a SQLITE table so_qa in a SQLITE database names so.db.
        Parameters
        ----------
        dataset_name : string
            name of the corpus
        '''
        from google.cloud import bigquery
        import os
        import sqlite3
        if not os.path.exists(dataset_name):
            os.makedirs(dataset_name)
        with open(os.path.join(dataset_name, dataset_name + '.dat'), 'w+') as dataset_file:
            with open(os.path.join(dataset_name, 'metadata.dat'), 'w+') as metadata_file:
                client = bigquery.Client()
                query_job = client.query("""
            #standardSQL
            SELECT *
            FROM `spherical-voice-182903.so.so_qa`""")
                with sqlite3.connect('so.db') as conn:
                    cursor = conn.cursor()
                    results = query_job.result()
                    insert_script = '''insert into so_qa (id,title,body,question_score,answer_id,answer_body)  values({},'{}','{}',{},{},'{}')'''

                    for row in results:
                        print("{}: {}".format(row.id, row.title))
                        cursor.execute(insert_script.format(
                            row.id, str(row.title).replace("'", "\'\'"), str(row.body).replace("'", "\'\'"), row.question_score, row.answer_id, str(row.answer_body).replace("'", "\'\'")))
                        conn.commit()
                        dataset_file.write(row.title + '\n')
                        metadata_file.write(
                            str(row.id) + '\t' + str(row.question_score) + '\n')

                    for row in cursor.execute('select * from so_qa'):
                        print(row)


    @staticmethod
    def fetch_search_results(searchText, searchType):
        '''
        Method to create an inverted index using the line corpus for SQ
        and search the inverted index.
        Parameters
        ----------
        searchText : str
            text to search
        searchType : str
            Is search type 's' - sorted by Answer Score or 'r' - sorted by serach query Relevance
        '''
        import metapy
        import sqlite3
        idx = metapy.index.make_inverted_index('config.toml')        
        query = metapy.index.Document()
        ranker = metapy.index.OkapiBM25()
        query.content(searchText)
        queryCount = 10
        if searchType == 's':
            queryCount = 20
        scores = ranker.score(idx, query, queryCount)
        results = []
        with sqlite3.connect('so.db') as conn:
            cursor = conn.cursor()
            for score in scores:   
                id = idx.metadata(score[0]).get('index')                
                cursor.execute(f'''select body,answer_body,title from so_qa where id = {id}''')
                row = cursor.fetchone()
                results.append({'id': id,
                                'score': idx.metadata(score[0]).get('score'),
                                'title': row[2],
                                'question': row[0],
                                'answer': row[1],
                                'relevance': score[1]})
                    
        return sorted(results, key=lambda x: x['score'] if searchType == 's' else x['relevance'], reverse=True)


if __name__ == "__main__":
    SoDatasetCreator.create_dataset("so")
    # SoDatasetCreator.create_index()
