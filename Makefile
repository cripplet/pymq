all: clean
	@python2 -m unittest discover
	@python3 -m unittest discover
	@make clean

clean:
	@rm -rf pymq/*pyc
	@rm -rf pymq/*/*pyc
	@rm -rf pymq/__pycache__
	@rm -rf pymq/*/__pycache__

purge: clean
