# BQ table empty creation and schema defintions for GA tables
from google.cloud import bigquery
client = bigquery.Client()
dataset_ref = client.dataset('sumo')


def create_twitter_word_frequencies():
  schema = [
    bigquery.SchemaField('tweet_dt', 'DATE', mode='NULLABLE'),
    bigquery.SchemaField('tweet_word', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('tweet_freq', 'INTEGER', mode='NULLABLE')
  ]
  table_ref = dataset_ref.table('twitter_word_frequencies')
  table = bigquery.Table(table_ref, schema=schema)
  table = client.create_table(table)  # API request

  assert table.table_id == 'twitter_word_frequencies'


def create_twitter_antivirus_frequencies():
  schema = [
    bigquery.SchemaField('tweet_dt', 'DATE', mode='NULLABLE'),
    bigquery.SchemaField('tweet_word', 'STRING', mode='NULLABLE'),
    bigquery.SchemaField('tweet_freq', 'INTEGER', mode='NULLABLE')
  ]
  table_ref = dataset_ref.table('twitter_antivirus_frequencies')
  table = bigquery.Table(table_ref, schema=schema)
  table = client.create_table(table)  # API request

  assert table.table_id == 'twitter_antivirus_frequencies'

def create_twitter_sentiment():
  schema = [
      bigquery.SchemaField('id_str', 'INTEGER', mode='NULLABLE'),
      bigquery.SchemaField('score', 'FLOAT', mode='NULLABLE',
                           description='Sentiment score from the google language api'),
      bigquery.SchemaField('magnitude', 'FLOAT', mode='NULLABLE',
                           description='Sentiment magnitude from the google language api'),
      bigquery.SchemaField('discrete_sentiment', 'STRING', mode='NULLABLE', 
                           description='''Contains a simple to understand aggregate score 
                                       of the sentiment such as positive or negative, based 
                                      on the score and magnitude'''),
  ]
  table_ref = dataset_ref.table('twitter_sentiment')
  table = bigquery.Table(table_ref, schema=schema)
  table = client.create_table(table)

def create_twitter_driving_sentiment():
  schema = [
      bigquery.SchemaField('id_str', 'INTEGER', mode='NULLABLE'),
      bigquery.SchemaField('empty_filler', 'STRING', mode='NULLABLE', description='ignore this'),
  ]
  table_ref = dataset_ref.table('twitter_driving_sentiment')
  table = bigquery.Table(table_ref, schema=schema)
  table = client.create_table(table) 


def main():

  #create_twitter_word_frequencies()
  #create_twitter_antivirus_frequencies()
  create_twitter_sentiment()
  create_twitter_driving_sentiment()  


if __name__ == '__main__':
  main()
