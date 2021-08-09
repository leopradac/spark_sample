import pytest
from pyspark.sql import SparkSession

from main import execute_challenge, get_dataframes, join_and_get_ids, overwrite_flag
from pyspark.sql.functions import when, lit, col


# def test_challenge():
#     df = execute_challenge()
#     assert df is not None

@pytest.fixture(scope="session")
def test_all(spark_test_session):
    print('RUNNING')
    # spark = SparkSession.builder.master("local").appName("challenge_2").getOrCreate()
    process_df, translation_df, client_rest_df, ccpa_df = get_dataframes(spark_test_session())
    client_rest_df = join_and_get_ids(client_rest_df, translation_df)
    ccpa_df = ccpa_df.withColumn('flag', lit(1))
    ccpa_df = join_and_get_ids(ccpa_df, translation_df)
    process_df = overwrite_flag(process_df, client_rest_df)
    process_df = overwrite_flag(process_df, ccpa_df)
    final_result = process_df.distinct().sort(process_df.id)
    assert final_result.count() == 10
