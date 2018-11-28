#!/bin/bash

printf "testing /shows/ and /shows/:show_id\n"
if [ -e test_shows.py ]; then
	python test_shows.py
else
	python tests/test_shows.py
fi

printf "\ntesting /ratings/:show_id\n"
if [ -e test_ratings.py ]; then
	python test_ratings.py
else
	python tests/test_ratings.py
fi

printf "\ntesting /recommendations/:user_id\n"
if [ -e test_rec.py ]; then
	python test_rec.py
else
	python tests/test_rec.py
fi

printf "\ntesting /users/ and /users/:user_id\n"
if [ -e test_users.py ]; then
	python test_users.py
else
	python tests/test_users.py
fi

printf "\ntesting /reset/ and /reset/:show_id\n"
if [ -e test_reset.py ]; then
	python test_reset.py
else
	python tests/test_reset.py
fi
