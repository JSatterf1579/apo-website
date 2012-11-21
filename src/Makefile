test:
	nosetests tests/
start_webserver:
	dev_appserver.py . -p 8080
run_tests:
	python tests/test_accounts/test_accounts.py
	python tests/test_accounts/test_forms.py 
	python tests/test_accounts/test_views.py 
	python tests/test_accounts/test_models.py 
generate_coverage:
	coverage run tests/test_accounts/test_accounts.py
	mv .coverage .coverage.1
	coverage run tests/test_accounts/test_views.py
	mv .coverage .coverage.2
	coverage run tests/test_accounts/test_forms.py
	mv .coverage .coverage.3
	coverage run tests/test_accounts/test_models.py
	mv .coverage .coverage.4
	coverage combine
	coverage html --include=application/*
run_tests_highlighting:
	(python tests/test_accounts/test_accounts.py 2>&1 1>&3 | grep --color=AUTO 'Ran [0-9]* tests in [0-9]\.[0-9]*s' 1>&2) 3>&1