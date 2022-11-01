ARG APP_IMAGE=python:3.10.7-alpine
FROM $APP_IMAGE

# permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Pre-populate db tables and default admin user
RUN flask init-db

# define the port number the container should expose
EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:app"]
