
## Test chạy MapReduce cho bài code nhân ma trận
```./matmul_mapper.py < input.txt | sort -t 1 | ./matmul_reducer.py```

```hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.1.jar -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator -D mapreduce.partition.keycomparator.options='-k1,1 -k2nr' -D stream.num.map.output.key.fields=2 -files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input /input.txt -output /output```

## Test chạy Pig cho bài nhân ma trận
```pig -x local matmul.pig```
