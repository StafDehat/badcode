#!/bin/bash

if ! grep -qP '^\d+' <<<"$1"; then
  echo "Takes 1 argument, numbers only."
  echo "ie: $0 12"
  exit 1
fi


STR="lst=[\n"
for x in $(seq 1 $1); do 
  if [[ $x -ge $1 ]]; then
    STR+="  $((10#$RANDOM$RANDOM))\n"
  else
    STR+="  $((10#$RANDOM$RANDOM)),\n"
  fi
done
STR+="]"
echo -e "$STR"
