APP=docker-compose run --rm app

update:
	docker-compose build
	docker-compose stop
	docker-compose rm -f
	docker-compose build

test:
	$(APP) tox
