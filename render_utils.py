#!/usr/bin/env python

import app_config

def flatten_app_config():
    """
    Returns a copy of app_config containing only
    configuration variables.
    """
    config = {}

    # Only all-caps [constant] vars get included
    for k, v in app_config.__dict__.items():
        if k.upper() == k:
            config[k] = v

    return config

def make_context():
    """
    Create a base-context for rendering views.
    Includes app_config and JS/CSS includers.
    """
    context = flatten_app_config()

    return context

