
TODAY := $(shell date '+%Y-%m-%d')

.DEFAULT_GOAL := all

AWS_PROFILE := default

all: check_venv
	pytest

awsci: check_venv
	pytest aws/ --aws-profiles $(AWS_PROFILE) --json=results-$(AWS_PROFILE)-$(TODAY).json

aws-sg: check_venv
	pytest \
		aws/ec2/test_ec2_security_group_in_use.py \
		aws/ec2/test_ec2_security_group_opens_all_ports.py \
		aws/ec2/test_ec2_security_group_opens_all_ports_to_all.py \
		aws/ec2/test_ec2_security_group_opens_all_ports_to_self.py \
		aws/rds/test_rds_db_security_group_does_not_grant_public_access.py \
		aws/rds/test_rds_db_instance_not_publicly_accessible_by_vpc_sg.py \
		--aws-profiles $(AWS_PROFILE) --json=results-sg-$(AWS_PROFILE)-$(TODAY).json

check_venv:
ifeq ($(VIRTUAL_ENV),)
	$(error "Run pytest-services from a virtualenv (try 'make install && source venv/bin/activate')")
endif

clean: clean-cache
	rm -rf venv

clean-cache: check_venv
	pytest --cache-clear --aws-profiles $(AWS_PROFILE)

doctest: check_venv
	for f in $(shell find . -name '*.py' | egrep -v '(venv|test|resources|init)'); do python -m doctest $$f; done

flake8: check_venv
	flake8 --max-line-length 120 $(shell find . -name '*.py' -not -path "./venv/*")

install: venv
	( . venv/bin/activate && pip install -r requirements.txt )

venv:
	python3 -m venv venv

.PHONY:
	all \
	check_venv \
	clean \
	clean-cache \
	flake8 \
	install \
	venv
