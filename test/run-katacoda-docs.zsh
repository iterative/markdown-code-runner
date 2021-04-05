#!/bin/zsh

# This script runs a set of Katacoda Markdown files in associated containers.
# Basically it's a bunch of commands that runs Katacoda files in associated
# containers after cloning the katacoda-scenarios repository. 


REPO=https://github.com/iesahin/katacoda-scenarios

CLONE_PATH="/tmp/katacoda-scenarios-${RANDOM}"

DIR="${CLONE_PATH}/get-started-dockerized"
export PYTHONPATH=${PYTHONPATH}:$(dirname $0)/../
RUNNER="$(dirname $0)/../bin/run-in-container.py"

git clone $REPO $CLONE_PATH

$RUNNER -c emresult/katacoda-base -k execute ${DIR}/01-initialize/*.md 

$RUNNER -c emresult/katacoda-gs-versioning -k execute ${DIR}/02-versioning/*.md

$RUNNER -c emresult/katacoda-gs-accessing -k execute ${DIR}/03-accessing/*.md

$RUNNER -c emresult/katacoda-gs-stages -k execute ${DIR}/04-stages/*.md

$RUNNER -c emresult/katacoda-gs-params -k execute ${DIR}/05-params-metrics-plots/*.md

$RUNNER -c emresult/katacoda-gs-experiments -k execute ${DIR}/06-experiments/*.md

