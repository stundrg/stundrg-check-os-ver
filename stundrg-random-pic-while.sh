#!/bin/bash

# 인자가 없으면 ppabam-random-match, 있으면 전달된 인자 실행
if [ -z "$1" ]; then
    COMMAND="ppabam-random-match"
else
    COMMAND="$1"
fi

# 1초 간격으로 ppabam-random-match 명령어 실행
while true; do
    pdm update
    clear
    $COMMAND
    sleep 1  # 1초 대기
done
