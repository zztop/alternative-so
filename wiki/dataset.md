# Create dataset
Corpus dataset can be created either directly from Google BigQuery dataset or the embedded SQLITE database so.db included in the repository.  

### Dataset from Google BigQuery
For creating dataset one need to request [here](mailto:zaryab.ahmad@gmail.com) access to the spherical-voice-182903:so.so_qa table or one can export the table into a custom BigQuery namespace using the following query

```sql
        SELECT
        pq.id,
        pq.title,
        pq.body,
        pq.score AS question_score,
        po.id AS answer_id,
        po.body AS answer_body
        FROM
        `bigquery-public-data.stackoverflow.posts_questions` AS pq
        INNER JOIN
        `bigquery-public-data.stackoverflow.posts_answers` AS po
        ON
        po.parent_id = pq.id
        and pq.accepted_answer_id = po.id 
        WHERE
        DATE(pq.creation_date) > DATE('2012-12-30')
        AND DATE(pq.creation_date) < DATE('2013-03-01')
        AND pq.score > 0
        AND UPPER(pq.tags) LIKE '%JAVA%'
        AND UPPER(pq.tags) NOT LIKE '%JAVASCRIPT%'
        and po.score > 0
        GROUP BY
        pq.id,
        pq.title,
        pq.body,
        question_score,
        answer_id,
        answer_body
        ORDER BY
        pq.id ASC
```

User can then invoke ```SoDatasetCreator.create_dataset``` method to create Corpus dataset. 
> In order to connect to Google Big Query one needs to set correct authentication token. Follow instructions [here](https://cloud.google.com/docs/authentication/getting-started) to do so
> This method creates a folder with corpus dataset files. Once done add ```line.toml``` file in the dataset folder with following content
```toml
type = "line-corpus"
metadata = [{name = "index", type="int"},{name="score",type ="int"}]
```
> This process also creates a SQLITE file ```so.db```. This database contains so_qa table , which is an extract of the Big Query table


