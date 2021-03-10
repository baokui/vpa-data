input1=$1
input2=$2
hpoutput=$3
hadoop fs -rmr $hpoutput
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D stream.non.zero.exit.is.failure=false \
    -D mapred.reduce.tasks=5 \
    -D mapred.map.tasks=5 \
    -D mapred.task.timeout=86400000 \
    -D mapreduce.map.memory.mb=2048 \
    -D mapreduce.reduce.memory.mb=4096 \
    -files mapper.py,reducer.py \
    -input $input1 \
    -input $input2 \
    -output $hpoutput \
    -mapper "python mapper.py" \
    -reducer "python reducer.py"