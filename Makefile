
.DEFAULT_GOAL=compile

compile:
	python -m compileall -q poller_directory.py

test:
	nosetests --exe tests/

# needs python-stdeb
package_deb:
	python setup.py --command-packages=stdeb.command bdist_deb

clean:
	rm -rf deb_dist/
	rm -rf debian/
	rm -rf dist/
	rm -f poller_directory-*.tar.gz
