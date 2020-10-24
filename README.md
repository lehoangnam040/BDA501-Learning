# Note lại việc học môn BDA501, môi trường cài cắm sử dụng docker 
## Dùng cho việc tự học big data hiệu quả hơn, khi không cần cài máy ảo chạy nặng và tốn tài nguyên mà dựa vào docker
## docker chỉ chạy tốt trên Linux, không khuyến khích chạy trên window và mac.
## docker phiên bản ubuntu 20.04 LTS

- Cần cài đặt docker trên máy
- File \*.tar.gz là docker file đã được đóng gói và dump lại, các file này có dung lượng lớn nên phải tải git lfs để support việc pull về
- Load docker dùng câu lệnh ```docker load -i *.tar.gz```
- Run image: ```docker run -tid "image-id"```
- Vào trong máy ảo: ```docker exec -it "container-id" bash```
- Chạy ```/etc/init.d/ssh start``` để mở openssh-server
- Kiểm tra ssh bằng cách ```/etc/init.d/ssh status```
- ```su hduser_``` để switch sang user "hduser\_" có sẵn
- ```$HADOOP_HOME/bin/hdfs namenode -format```
- ```$HADOOP_HOME/sbin/start-dfs.sh```
- ```$HADOOP_HOME/sbin/start-yarn.sh```

## Kiểm tra việc cài đặt
- ```java -version```
```
openjdk version "1.8.0_265"
OpenJDK Runtime Environment (build 1.8.0_265-8u265-b01-0ubuntu2~20.04-b01)
OpenJDK 64-Bit Server VM (build 25.265-b01, mixed mode)
```

- ```javac -version```
```
javac 1.8.0_265
```

- ```hadoop version```
```
Hadoop 3.2.1
Source code repository https://gitbox.apache.org/repos/asf/hadoop.git -r b3cbbb467e22ea829b3808f4b7b01d07e0bf3842
Compiled by rohithsharmaks on 2019-09-10T15:56Z
Compiled with protoc 2.5.0
From source with checksum 776eaf9eee9c0ffc370bcbc1888737
This command was run using /home/hduser_/hadoop/share/hadoop/common/hadoop-common-3.2.1.jar
```
- ```jps```
```
pid NodeManager
pid NameNode
pid DataNode
pid ResourceManager
pid Jps
```

- ```pig --version```
```
Apache Pig version 0.17.0 (r1797386) 
compiled Jun 02 2017, 15:41:58
```

- ```scala --version```
```
Scala code runner version 2.12.10 -- Copyright 2002-2019, LAMP/EPFL and Lightbend, Inc.
```

- ```spark-shell --version```
```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.1
      /_/
                        
Using Scala version 2.12.10, OpenJDK 64-Bit Server VM, 1.8.0_265
Branch HEAD
Compiled by user ubuntu on 2020-08-28T08:58:35Z
Revision 2b147c4cd50da32fe2b4167f97c8142102a0510d
Url https://gitbox.apache.org/repos/asf/spark.git
Type --help for more information.
```

- ```pyspark --version```
```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.1
      /_/
                        
Using Scala version 2.12.10, OpenJDK 64-Bit Server VM, 1.8.0_265
Branch HEAD
Compiled by user ubuntu on 2020-08-28T08:58:35Z
Revision 2b147c4cd50da32fe2b4167f97c8142102a0510d
Url https://gitbox.apache.org/repos/asf/spark.git
Type --help for more information.
```

## Enjoy your time!!!
