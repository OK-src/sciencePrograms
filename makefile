COMPILER = gcc
COMPILED_FILE_NAME = reactionBalancer
LANG = ITA
ROOT = sudo

all:
	${COMPILER} reactionBalancer_${LANG}.c -o ${COMPILED_FILE_NAME}

install:
	${ROOT} cp ${COMPILED_FILE_NAME} /bin/
