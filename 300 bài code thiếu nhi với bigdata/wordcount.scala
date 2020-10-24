import org.apache.spark._
import org.apache.spark.SparkContext._
object WordCount {
    def main(args: Array[String]) {
      val conf = new SparkConf().setAppName("wordCount")
      // Create a Scala Spark Context.
      val sc = new SparkContext(conf)
      val textFile = sc.textFile("file:///home/hduser_/hadoop/LICENSE.txt")
      val counts = textFile.flatMap(line => line.split(" "))
                 .map(word => (word, 1))
                 .reduceByKey(_ + _)
      counts.saveAsTextFile("file:///home/hduser_/output")
    }
}

