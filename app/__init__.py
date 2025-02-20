from flask import Flask


def create_app():
    return Flask(__name__, instance_relative_config=True)
