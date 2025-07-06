# app/__init__.py
# This file can be left empty, or you can expose important objects for easier access.

from fastapi import FastAPI

__all__ = ["get_app"]


def get_app() -> FastAPI:
    """Return the FastAPI application lazily."""
    from app.main import app

    return app
