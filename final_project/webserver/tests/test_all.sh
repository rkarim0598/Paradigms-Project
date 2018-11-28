#!/bin/bash

printf "testing /shows/ and /shows/:show_id\n"
python test_shows.py

printf "\ntesting /ratings/:show_id\n"
python test_ratings.py

printf "\ntesting /recommendations/:user_id\n"
python test_rec.py

printf "\ntesting /users/ and /users/:user_id\n"
python test_users.py

printf "\ntesting /reset/ and /reset/:show_id\n"
python test_reset.py
