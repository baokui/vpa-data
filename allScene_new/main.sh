#Year=$1
#Month=$2
#Day=$3
#for((Hour=0;Hour<9;Hour++))
#do
#Hour=0$Hour
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1 &
#done
#Hour=09
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1
#
#for((Hour=10;Hour<18;Hour++))
#do
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1 &
#done
#Hour=18
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1
#
#for((Hour=19;Hour<23;Hour++))
#do
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1 &
#done
#Hour=23
#input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*$Year$Month$Day$Hour*.lzo
#input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/vpare_log.vpa-*.$Year-$Month-${Day}_$Hour-*.lzo
#output=VpaOutput_guobk/allScene_new/Tab3/hour/$Year$Month$Day$Hour
#sh join.sh $input1 $input2 $output >> log/allScene_new-$Year$Month$Day$Hour.log 2>&1

Year=$1
Month=$2
Day=$3
input1=/cloud/dt/pingback/ping/djt-pb-log/vpapb_android_shouji/$Year$Month/$Year$Month$Day/*.lzo
input2=/storage/sogou/desktop/imeservice/vpare/$Year$Month/$Year$Month$Day/*.lzo
output=VpaOutput_guobk/allScene_new/Tab3/day/$Year$Month$Day
sh join.sh $input1 $input2 $output >> log/allScene_new-day-$Year$Month$Day.log 2>&1 &