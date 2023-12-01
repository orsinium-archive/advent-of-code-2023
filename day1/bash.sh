#!/usr/bin/env bash

sed -n 's/[^0-9]//gp' | # filter out everything but digits
awk '{print substr($0, 0, 1),substr($0, length($0), 1)}' | # leave only the first and the last character
sed -n 's/ //gp' |      # remove the space between the digits
paste -sd+ |            # replace newlines with a "+" sign
bc                      # evaluate the math expression
