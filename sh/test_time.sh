       
SEARCH_TIME="2022-07-06 10:00:00"
input_timestamp=`date -d "$SEARCH_TIME" +%s`
     
end_time=`expr $input_timestamp - 32401`
END_TIME=`date -d @$end_time +%Y-%m-%d\ %H:%M:00`


start_time=`expr $input_timestamp - 25200`
START_TIME=`date -d @$start_time +%Y-%m-%d\ %H:%M:00`





echo $START_TIME
echo $END_TIME