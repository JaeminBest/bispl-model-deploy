SHELL = bash
ifneq ("$(wildcard .env)","")
	include .env
endif

.PHONY: help pre-commit

help:
	@echo -e "\033[1mUSAGE:\033[0m"
	@echo "  make [target]"
	@echo "  this is for dev environment"
	@echo ""
	@echo -e "\033[1mTARGETS:\033[0m"
	@echo "  pre-commit           - run pre-commit hooks on all files"

.ONESHELL:
pre-commit:
	# pre-commit
	git ls-files | xargs poetry run pre-commit run -c .conf/.pre-commit-config.yaml --verbose --files
