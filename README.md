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
- ```chmod 750 ~/hdfs```
- ```$HADOOP_HOME/bin/hdfs namenode -format```
- ```$HADOOP_HOME/sbin/start-dfs.sh```
- ```$HADOOP_HOME/sbin/start-yarn.sh```
- Chạy ```hadoop version``` và ```jps``` để kiểm tra việc cài đặt

- Enjoy your time!!!
