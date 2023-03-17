APP=docker-compose run --rm app
TOX=tox

update:
	docker-compose build
	docker-compose stop
	docker-compose rm -f
	docker-compose build

test:
	$(APP) $(TOX)

test-circle:	# run automated tests like circle-ci would
	docker-compose run --rm test-circle $(TOX)
