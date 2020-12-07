Guideline to run project:<br/>
# Requirement
- docker
- python
- pyspark

# 1. Kafka
- cd kafka && docker-compose up -d

# 2. Spark Streaming
- cd spark 
- spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 --master yarn spark_app.py 

# 3. ELK
- cd ELK
- docker-compose up -d

# 4. Ecommerce website
- cd frontend-backend
- python3 server.py
- Open index.html on browser
