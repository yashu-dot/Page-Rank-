																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																													#!/bin/sh
CONVERGE=1
rm A2F/v* log*																												

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave																																																																																																																																																												
bin/hdfs dfs -rm -r /user/output* 
bin/hdfs dfs -rm -r /user/A2_out/adj1* 																																																																																																																																																																																																																																																																																																																																																											
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
-mapper "/home/navyadhara/hadoop/A2F/BD_0087_0196_0230_0252_mapper_t1.py" \
-reducer "/home/navyadhara/hadoop/A2F/BD_0087_0196_0230_0252_reducer_t1.py '/home/navyadhara/hadoop/A2F/v'"  \
-input /user/web \
-output /user/A2_out/adj10 #has adjacency list


while [ "$CONVERGE" -ne 0 ]
do
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.2.0.jar \
	-mapper "'/home/navyadhara/hadoop/A2F/BD_0087_0196_0230_0252_mapper_t2.py' '/home/navyadhara/hadoop/A2F/v'" \
	-reducer '/home/navyadhara/hadoop/A2F/BD_0087_0196_0230_0252_reducer_t2.py' \
	-input /user/A2_out/adj10/part-00000 \
	-output /user/outputkn14
	touch v1
	bin/hadoop fs -cat /user/outputkn14/part-00000 > '/home/navyadhara/hadoop/A2F/v1'
	CONVERGE=$(python3 '/home/navyadhara/hadoop/A2/check_conv.py' >&1)
	bin/hdfs dfs -rm -r /user/outputkn14
	echo $CONVERGE

done
