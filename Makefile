.PHONY: package
package:
	make clean
	python setup.py sdist
.PHONY: pypi
pypi:
	make clean
	python setup.py sdist bdist_wheel; python setup.py register; python setup.py bdist_wheel sdist upload
.PHONY: devpkgs
devpkgs:
	pip install --upgrade pip
	pip install --upgrade arrow
	pip install --upgrade pytest==2.6.4
.PHONY: clean
clean:
	find ./* -name '*.pyc' -exec rm {} \;
	find ./* -name '*.so' -exec rm {} \;
	find ./* -name '*.coverage' -exec rm {} \;
	@# A minus sign prefixing the line means it ignores the return value
	-find ./* -path '*__pycache__' -exec rm -rf {} \;
	@# remove all the MockSSH keys
	-find ./* -name '*.key' -exec rm {} \;
	-rm -rf .eggs/
	-rm -rf build/ dist/ shellsnmp.egg-info/ setuptools*
.PHONY: help
help:
	@# An @ sign prevents outputting the command itself to stdout
	@echo "help                 : You figured that out ;-)"
	@echo "pypi                 : Build the project and push to pypi"
	@echo "devpkgs              : Get all dependencies for the dev environment"
	@echo "devtest              : Run tests - Specific to Mike Pennington's build env"
	@echo "clean                : Housecleaning"
	@echo ""
