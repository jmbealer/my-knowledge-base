#!/usr/bin/env bash

awk '{
print "** "$1,$2
print ":PROPERTIES:"
print ":ANKI_NOTE_TYPE: spelling Vocabuary Basic"
print ":END:"

print "*** Front"
print $1
print "*** Extra"
print $2

} ' awkTest.txt > awkTest.org
