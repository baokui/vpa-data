Year=2021
Month=02
for((Day=24;Day<29;Day++))
do
sh main0.sh $Year $Month $Day >> log/main0-$Year$Month$Day.log 2>&1 &
done

Year=2021
Month=03
for((Day=1;Day<10;Day++))
do
sh main0.sh $Year $Month 0$Day >> log/main0-$Year$Month0$Day.log 2>&1 &
done