from pyspark import SparkContext

def main():
    sc = SparkContext(appName='SparkWordCount')
    input_file = sc.textFile('file:///home/hduser_/hadoop/NOTICE.txt')
    counts = input_file.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile('file:///home/hduser_/output')
    sc.stop()

if __name__ == '__main__':
    main()
