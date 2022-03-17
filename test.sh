#!/bin/bash

echo "Run test ...."

echo "Run first test suite test_app"
python3 -m unittest test_tic_tac_toe/test_app.py
#
echo "Run second test suite test_random_moves"
python3 -m unittest test_tic_tac_toe/test_human_vahuman_e2e.py