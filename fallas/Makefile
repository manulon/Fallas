run:
	docker build  -f Dockerfile . --rm  -t movie-selector
	docker run --publish 6002:6002 -e PORT=6002 --rm -it movie-selector
