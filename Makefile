SHELL				=	/bin/sh

PROJNAME			=	bcc-fe-exchange-model

RM					=	rm
ECHO				=	echo
COPY				=	cp
FIND				=	find

CONDA				=	conda
CONDA_ENV_FILE		=	environment.yml

PYTHON				=	/usr/bin/env python
PYTHON_SETUP		=	setup.py

ALL_FILES			=

CLEAN_FILES			=	*_cache

define cleanup
	-$(RM) -rf $(CLEAN_FILES)
endef

define pycache_cleanup
	$(FIND) -name "__pycache__" -type d -exec $(RM) -rf {} +
endef

define setup_conda_env
	bash -lc "$(CONDA) env update --file $(CONDA_ENV_FILE)"
endef

.SILENT		:
.PHONY		:	all clean dev

all			:	$(ALL_FILES)

docs		:
	$(call make_docs)

clean		:
	$(call cleanup)
	$(call pycache_cleanup)

dev			:
	$(ECHO) Setting up dev environment
	$(call setup_conda_env)
