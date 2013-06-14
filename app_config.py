#!/usr/bin/env python

"""
Project-wide application configuration.
"""

import os

"""
DEPLOYMENT
"""
PRODUCTION_S3_BUCKETS = ['apps.npr.org']

STAGING_S3_BUCKETS = ['stage-apps.npr.org']

SITEMAP_GOOGLE_DOC_KEY = '0AlXMOHKxzQVRdGQ5eDBzYUhQQWI3VjNtQ29iWTdGS0E'

# These variables will be set at runtime. See configure_targets() below
S3_BUCKETS = []
DEBUG = True

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKETS
    global DEBUG

    if deployment_target == 'production':
        S3_BUCKETS = PRODUCTION_S3_BUCKETS
        DEBUG = False
    else:
        S3_BUCKETS = STAGING_S3_BUCKETS
        DEBUG = True

"""
Run automated configuration
"""
DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)

