#!/usr/bin/env sh
#   sh run_dev.sh

export FLASK_APP=app/routes.py
export FLASK_DEBUG=True

flask run --host=127.0.0.1 --port=5000