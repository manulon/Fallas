run:
	docker build  -f Dockerfile . --rm  -t movie-selector
	docker run --publish 5025:5025 -e PORT=5025 --rm -it movie-selector
