build:
	docker build . -t personal-website

clean:
	docker-compose down

dev:
	docker-compose up --watch --build

stop:
	docker-compose stop