from pyspark.sql import SparkSession
from pyspark.sql.functions import when, lit, col

from schemas import process_schema, translation_schema, client_restrictions_schema, ccpa_schema


def get_dataframes(spk):
    process_df = spk.read.options(header=True).csv('files/1_process.csv', schema=process_schema)
    translation_df = spk.read.options(header=True).csv('files/2_translation.csv', schema=translation_schema)
    client_rest_df = spk.read.options(header=True).csv('files/3_client_restrictions.csv',
                                                       schema=client_restrictions_schema)
    ccpa_df = spk.read.options(header=True).csv('files/4_ccpa.csv', schema=ccpa_schema)
    return process_df, translation_df, client_rest_df, ccpa_df


def join_and_get_ids(main_df, df_to_join_with):
    return (
        main_df
        .join(df_to_join_with, main_df.pii == df_to_join_with.pii, 'left')
        .select('id', main_df.pii, main_df.type, main_df.flag)
        .filter("id is not null")
    )


def overwrite_flag(final_df, source_df):
    return (
        final_df
        .join(source_df, final_df.id == source_df.id, 'left')
        .withColumn('new_flag', when(source_df.flag == 1, 1).otherwise(final_df.flag))
        .select(
            final_df.id,
            final_df.content,
            col('new_flag').alias('flag')
        )
    )


def execute_challenge():
    print('RUNNING')
    spark = SparkSession.builder.master("local").appName("challenge_2").getOrCreate()
    process_df, translation_df, client_rest_df, ccpa_df = get_dataframes(spark)
    client_rest_df = join_and_get_ids(client_rest_df, translation_df)
    ccpa_df = ccpa_df.withColumn('flag', lit(1))
    ccpa_df = join_and_get_ids(ccpa_df, translation_df)
    process_df = overwrite_flag(process_df, client_rest_df)
    process_df = overwrite_flag(process_df, ccpa_df)
    final_result = process_df.distinct().sort(process_df.id)
    final_result.show()
    return final_result


if __name__ == '__main__':
    execute_challenge()
