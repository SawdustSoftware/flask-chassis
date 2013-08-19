SHELL=/bin/bash
SHELLOPTS=errexit:pipefail

ENVDIR=env
ACTIVATE:=$(ENVDIR)/bin/activate

.PHONY:	clean

count=10

requirements = requirements.txt requirements-dev.txt
virtualenv: $(ACTIVATE)
$(ACTIVATE): $(requirements)
	test -d $(ENVDIR) || virtualenv --no-site-packages $(ENVDIR)
	for f in $?; do \
		. $(ACTIVATE); pip install -r $$f; \
	done
	touch $(ACTIVATE)

dev: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" python src/runserver.py

test: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" nosetests --config=nose.ini src/tests.py

shell: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" python src/manage.py shell

dummy: virtualenv
	. $(ACTIVATE); FLASK_CONFIG="../../conf/dev.py" python src/manage.py dummy -n $(count)

docs: virtualenv
	git submodule update --init
	. $(ACTIVATE); make -C doc/ html
	open doc/_build/html/index.html

clean:
	rm -rf $(ENVDIR)
	rm -rf doc/_build/
