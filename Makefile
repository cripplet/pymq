all:
	@python2 bin/run_tests.py
	@python3 bin/run_tests.py

clean:
	@rm -rf pymq/*pyc
	@rm -rf pymq/*/*pyc
	@rm -rf pymq/__pycache__
	@rm -rf pymq/*/__pycache__
