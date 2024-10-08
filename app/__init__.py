from flask import Flask, g
from .app_factory import create_app

app = create_app()
app.secret_key = 'y'

from . import routes
