
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

if __name__=="__main__":
    sc = SparkContext(appName="testing_python_spark")
    ssc = StreamingContext(sc, 1)
    kafkaStream = KafkaUtils.createStream(ssc,topics =['logs_stream'],kafkaParams = {"metadata.broker.list":'localhost:9092'})
    lines = kafkaStream.map(lambda x: x[1])
    lines.pprint()
    ssc.start()
    ssc.awaitTermination()