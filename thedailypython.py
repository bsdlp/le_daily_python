#!/usr/bin/env python3

import os
import json
import configparser
import requests

url = 'http://tdp.me/v1'

def search_tdp_config(**kwargs):
    """
    Look for configuration and parse it.
    """
    api_key = None

    if 'TDP_CONFIG' in os.environ:
        paths = [os.environ['TDP_CONFIG']]
    else:
        paths = ['/etc/tdp.cfg', '~/.tdp']

    paths = [os.path.expandvars(p) for p in paths]
    paths = [os.path.expanduser(p) for p in paths]

    cfg = configparser.RawConfigParser()
    cfg.read(paths)

    if cfg.has_section('Credentials'):
        api_key = cfg.get('Credentials', 'api_key')

headers = {'X-Access-Token': api_key}
