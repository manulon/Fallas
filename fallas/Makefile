run:
	docker build  -f Dockerfile . --rm  -t movie-selector
	docker run --publish 5022:5022 -e PORT=5022 --rm -it movie-selector
