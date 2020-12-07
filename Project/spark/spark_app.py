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
from pyspark.sql.functions import explode, split, col, from_json,struct,to_json, count
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == '__main__':
    spark = SparkSession.builder.appName("productCount").getOrCreate()
    sc = spark.sparkContext
    sc.setLogLevel("WARN")
    # Read the data from kafka
    df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "172.17.0.1:9093").option("subscribe", "productView").load()

    string_df = df.selectExpr("CAST(key AS STRING)","CAST(value AS STRING)")

    schema = StructType([StructField("product", StringType())])

    json_df = string_df.withColumn("jsonData", from_json(col("value"), schema)).select("jsondata.*")

    products = json_df.select(json_df.product).alias("product")

    productCount = products.groupBy("product").agg(count('product').alias("view"))

    # Debug: print to console
    #query = productCount.writeStream.outputMode("complete").format("console").start()
    #query.awaitTermination()

    # Publish to Kafka
    productCount.selectExpr("to_json(struct(*)) AS value").writeStream.outputMode("complete")\
            .format("kafka").option("kafka.bootstrap.servers", "172.17.0.1:9093")\
            .option("checkpointLocation", "file:///home/hduser_/checkpoint")\
            .option("topic", "productViewCount").start().awaitTermination()

