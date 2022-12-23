#!/bin/bash

alias testoj="oj t -c 'python main.py'"
function testpy(){
  python main.py < test/sample-$1.in
  return 0
}
function newprob(){
  acc new $1 && cd $1
  return 0
}
