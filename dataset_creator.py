import os
import sqlite3
from google.cloud import bigquery


class SoDatasetCreator:
    """Create dataset for SO"""

    def __init__(self, dataset_name):
        self.dataset_name = dataset_name
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
                        metadata_file.write(str(row.id) + '\n')

                    for row in cursor.execute('select * from so_qa'):
                        print(row)


if __name__ == "__main__":
    so = SoDatasetCreator("test")
