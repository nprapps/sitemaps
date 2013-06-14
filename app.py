#!/usr/bin/env python

import csv

from flask import Flask, render_template

import app_config
from render_utils import make_context

app = Flask('sitemaps')

@app.route('/sitemap.xml')
def sitemap():
    """
    Renders a sitemap.
    """
    context = make_context()
    context['slugs'] = []

    with open('data/index.csv') as f:
        reader = csv.reader(f)
        reader.next()

        for row in reader:
            context['slugs'].append(row[0])

    sitemap = render_template('sitemap.xml', **context)

    return (sitemap, 200, { 'content-type': 'application/xml' })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app_config.DEBUG)
