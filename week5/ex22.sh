if test ! -f nums
then
  echo 0 > nums
fi

for i in `seq 1 50`;
do
  n=`tail -1 nums`
  expr $n + 1 >> nums
  done
