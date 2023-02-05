#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Executing the startup script for the docs container...'
cd docs
echo 'Sleeping for 2 minutes'
sleep 2m
make livehtml
