#!/usr/bin/env python3

import os
import json
import configparser
import requests

url = 'http://tdp.me/v1'

class Config_Opts(object):
    """
    Config stuff go here?
    """

    def __init__(self, api_key=None):
        self.api_key = api_key


def get_tdp_api_key():
    """
    Look for configuration and parse it for the API key. Return True and store
    the key in class Config_Opts if the key is found, or return False.
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

    if 'TDP_API_KEY' in os.environ:
        api_key = os.environ['TDP_API_KEY']
    elif cfg.has_section('Credentials'):
        api_key = cfg.get('Credentials', 'api_key')

    if api_key:
        Config_Opts(api_key)
        return True
    else:
        return False

headers = {'X-Access-Token': api_key}
