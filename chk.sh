#!/bin/bash

if [ ! -f "$(which ccrypt)" ]; then
	sudo apt-get install ccrypt || sudo yum install ccrypt
fi
