PID=$(shell cat run.pid)

debug:
	python app.py --debug

run:
	gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app

start:
	/usr/local/bin/gunicorn -k eventlet -w 1 --bind 0.0.0.0:80 app:app > log.txt 2>&1 & echo $$! > run.pid

stop:
	kill -2 ${PID}
