#!/bin/bash

while read p; do
  echo "$p"
  whatis "$p"
done <test11
