Year=$1
Month=$2
Day=$3
input1=/user/vpa/wangtingting/project/vpa/VpaAllSceneUpgradeRetDetailPre/$Year$Month$Day/p*
output=VpaOutput_guobk/allScene_new/Tab3/wtt/$Year$Month$Day
mapper=mapper_wtt.py
reducer=reducer0.py
sh join0.sh $input1 $output $mapper $reducer >> log/allScene_new-day-wtt-$Year$Month$Day.log 2>&1 &