import app
import pytest 
from flask import Flask, request, jsonify


def test_instructions():
    assert isinstance(app.instructions(), str) == True
