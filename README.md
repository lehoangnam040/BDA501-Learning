# Môi trường chạy hadoop sử dụng docker

- Cần cài đặt docker trên máy 
- File \*.tar.gz là docker file đã được đóng gói và dump lại
- Load docker dùng câu lệnh docker load -i \*.tar.gz
- Run image: docker run -tid <image-id>
- Vào trong máy ảo: docker exec -it <container-id> bash
- Chạy /etc/init.d/ssh start để mở openssh-server
- su hduser\_ để switch sang user "hduser\_" có sẵn
- chmod 750 ~/hdfs
- $HADOOP_HOME/bin/hdfs namenode -format
- $HADOOP_HOME/sbin/start-dfs.sh
- $HADOOP_HOME/sbin/start-yarn.sh
- Chạy hadoop version và jps để kiểm tra việc cài đặt

- Enjoy your time!!!
