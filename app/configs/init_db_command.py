from flask import Flask
from flask.cli import click
from app.controllers.init_db import init_db, init_test_load

def init_app(app: Flask):
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_test_data_command)

@click.command('init-db')
def init_db_command():
    init_db()

@click.command('load-test-db')
def load_test_data_command():
    init_test_load()
    