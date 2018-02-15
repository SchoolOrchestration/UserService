#!/usr/bin/env bash
sleep 10 # Wait for DB to startup
echo "==================================================================="
echo "STARTING TESTS"
echo "==================================================================="
coverage run manage.py test && # Put && so if tests fail it will exit with 1
coverage xml &&
echo "PUSHING COVERAGE TO CODACY" &&
echo "===================================================================" &&
python-codacy-coverage -r coverage.xml
