#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

import responses

from slacker import (
    API_BASE_URL,
    Channels,
)


class TestChannels(unittest.TestCase):
    @responses.activate
    def test_valid_ids_return_channel_id(self):
        response = {
            'ok': 'true',
            'channels': [
                {'name': 'general', 'id': 'C111'},
                {'name': 'random', 'id': 'C222'}
            ]
        }
        responses.add(
            responses.GET,
            API_BASE_URL.format(api='channels.list'),
            json=response,
            status=200
        )
        channels = Channels(token='aaa')
        self.assertEqual(channels.get_channel_id('general'), 'C111')

    @responses.activate
    def test_invalid_channel_ids_return_none(self):
        response = {
            'ok': 'true',
            'channels': [
                {'name': 'general', 'id': 'C111'},
                {'name': 'random', 'id': 'C222'}
            ]
        }
        responses.add(
            responses.GET,
            API_BASE_URL.format(api='channels.list'),
            json=response,
            status=200
        )
        channels = Channels(token='aaa')
        self.assertEqual(channels.get_channel_id('fake_group'), None)
