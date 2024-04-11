#!/bin/bash

CLUSTER_NAME=simon.ejilogo # please put your name here. It will be used for the name of kind cluster (format: fistname.lastname, only [a-z\.] characters allowed)
APP_LANGUAGE=python #please put the language you chose to use here (possible options: python, golang)

CLUSTER_VERSION=$(cat .tool-versions | grep kubectl | cut -d" " -f2)

[ -z "$APP_LANGUAGE" ] && echo "Programming language for the app not defined, please fill it in settings.sh" && exit 1

[ -z "$CLUSTER_NAME" ] && echo "Cluster name is not defined, please fill it in settings.sh" && exit 1
