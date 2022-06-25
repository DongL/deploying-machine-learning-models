#!/bin/sh -l

if [ true ]
then
    echo 'Error: this experiment failed!'
    exit 1
fi

echo "::debug ::Debug Message"
echo "::warning ::Warning Message"
echo "::error ::Error Message"


echo "Hello $1"
echo "::add-mask::$1"
echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"

echo "::group::Some expandable logs"
echo 'some stuff'
echo 'some stuff'
echo 'some stuff'
echo '::endgroup::'

# echo '::set-env name=HELLO::hello'