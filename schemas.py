from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, ArrayType

process_schema = (
    StructType()
    .add("id", IntegerType(), False)
    .add("content", StringType(), False)
    .add("flag", IntegerType(), False)
)

translation_schema = (
    StructType()
    .add("id", IntegerType(), False)
    .add("pii", StringType(), False)
    .add("type", StringType(), False))

client_restrictions_schema = (
    StructType()
    .add("pii", StringType(), False)
    .add("type", StringType(), False)
    .add("flag", IntegerType(), False)
)

ccpa_schema = (
    StructType()
    .add("pii", StringType(), False)
    .add("type", StringType(), False)
)
