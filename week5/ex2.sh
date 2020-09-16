if test ! -f numbers
then
  echo 0 > numbers
fi

if ln numbers numbers.lock
  then
  for i in `seq 1 50`;
  do
  n=`tail  -1 numbers`
  expr $n + 1 >> numbers
  done

  rm numbers.lock
fi
