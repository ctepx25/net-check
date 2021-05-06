#!/bin/bash
service nginx start
[[ ! -z $1 ]] && nc -lvk $1 || (nc -lvk 3044 & nc -lvk 4044)
