input1=$1
hpoutput=$2
mapper=$3
reducer=$4
hadoop fs -rmr $hpoutput
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D stream.non.zero.exit.is.failure=false \
    -D mapred.reduce.tasks=5 \
    -D mapred.map.tasks=5 \
    -D mapred.task.timeout=86400000 \
    -D mapreduce.map.memory.mb=2048 \
    -D mapreduce.reduce.memory.mb=4096 \
    -files $mapper,$reducer \
    -input $input1 \
    -output $hpoutput \
    -mapper "python $mapper" \
    -reducer "python $reducer"