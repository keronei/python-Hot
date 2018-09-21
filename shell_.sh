#!/bin/sh

#  Shell_counterpart.sh
#  perfoms same operation with the python-Hot counterpart.
#
#  Created by Keronei on 9/20/18.
#


read -p 'Provide first number: ' first_num

read -p 'Then the number to add: ' second_num

total=`expr $first_num + $second_num`

echo "Your total for $first_num & $second_num is : $total and running this script as $1"
