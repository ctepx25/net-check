#!/bin/bash
service nginx start
case $1 in
  3044)
    nc -lvk 3044
    ;;
  4044)
    nc -lvk 4044
    ;;
  *)
    nc -lvk 3044 & nc -lvk 4044
    ;;
esac
