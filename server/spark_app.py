#from __future__ import print_function
#
#import sys
#
#from pyspark import SparkContext
#from pyspark.streaming import StreamingContext
#
#if __name__ == "__main__":
#    if len(sys.argv) != 3:
#        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
#        exit(-1)
#    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
#    sc.setLogLevel("ERROR")
#    ssc = StreamingContext(sc, 10)
#
#    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
#    counts = lines.flatMap(lambda line: line.split(" "))\
#                  .map(lambda word: (word, 1))\
#                  .reduceByKey(lambda a, b: a+b)
#    counts.pprint()
#
#    ssc.start()
#    ssc.awaitTermination()

from pyspark.sql.session import SparkSession
from pyspark.sql.functions import explode, split, col, from_json,struct,to_json
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == '__main__':
    spark = SparkSession.builder.appName("wordCount").getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("WARN")
    # Read the data from kafka
    df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "192.168.1.24:9093").option("subscribe", "wordcount").load()

    string_df = df.selectExpr("CAST(key AS STRING)","CAST(value AS STRING)")

    schema = StructType([StructField("text", StringType())])

    json_df = string_df.withColumn("jsonData", from_json(col("value"), schema)).select("jsondata.*")

    words = json_df.select(
        explode(
            split(json_df.text, " ")
        ).alias("word")
    )

    wordCounts = words.groupBy("word").count()

    query = wordCounts.writeStream.outputMode("complete").format("console").start()

    query.awaitTermination()

