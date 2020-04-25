# -*- coding: utf-8 -*-

import requests
import json
import time
import hashlib
import hmac
from util.logger import setup_logger
from util.exceptions import NewdexAPIException

class NewdexV1():
    def __init__(self, access_key, secret_key,
                    symbol = 'theonlykarma-karma-wax', max_retries = 3):
        self.key = access_key
        self.secret = secret_key
        self.host = 'https://api.newdex.io/v1'
        self.symbol = symbol
        self._retries = 0
        self.max_retries = max_retries

        self.logger = setup_logger('NewdexV1')
        self.logger.info('NewdexV1 initialized. Endpoint: %s, Symbol: %s, Max retries: %s.' % 
                                                (self.host, self.symbol, self.max_retries))

    def open_orders(self):
        '''Get all open orders from symbol pair.'''
        return self._curl_newdex('/order/orders?', state= 'pending')

    def filled_orders(self):
        '''Get all open orders from symbol pair.'''
        return self._curl_newdex('/order/orders?', state= 'filled')

    def canceled_orders(self):
        '''Get all open orders from symbol pair.'''
        return self._curl_newdex('/order/orders?', state= 'canceled')

    def order_history(self):
        '''Get all open orders from symbol pair.'''
        return self._curl_newdex('/order/orders?', state= 'history')

    def cancel_order(self, trx_id):
        '''Cancel order based on trx_id.'''
        return self._curl_newdex('/order/cancel?', cancel= trx_id)

    def get_pairs(self):
        '''Get the list of all exchange pairs.'''
        return self._curl_newdex('/common/symbols')

    def get_tickers(self):
        '''Get the market of all exchange pairs.'''
        return self._curl_newdex('/tickers')

    def get_ticker(self):
        '''Get the market of a particular exchange pair.'''
        return self._curl_newdex('/ticker?symbol=')

    def get_price(self):
        '''Get the price of an exchange pair.'''
        return self._curl_newdex('/price?symbol=')

    def get_depth(self):
        '''Get order book (quoted depth).'''
        return self._curl_newdex('/depth?symbol=')

    def get_trades(self):
        '''Get deals record of exchange pair.'''
        return self._curl_newdex('/trades?symbol=')

    def get_candles(self):
        '''Get K-Line data of exchange pair.'''
        return self._curl_newdex('/candles?symbol=')

    def _curl_newdex(self, path, state = False, cancel = False):
        '''Build Newdex request url and auto retry on failure.'''
        if state:
            message = 'api_key=' + self.key + '&size=50&state=' + state + '&symbol=' + self.symbol + '&timestamp=' + str(int(time.time()))
            url = self.host + path + message + "&sign=" + self._sign(message)
        elif cancel:
            message = 'api_key=' + self.key + '&trx_id=' + cancel + '&timestamp=' + str(int(time.time()))
            url = self.host + path + message + "&sign=" + self._sign(message)
        else:
            url = self.host + path + self.symbol if '?' in path else self.host + path

        self.logger.info('Sending request to %s' % url)
        response = requests.get(url).json()

        if response["code"] != 200:
            self._retries += 1
            if self._retries >= self.max_retries:
                self.logger.error('Max retries with error code %s, exiting.' % response['code'])
                raise NewdexAPIException(response)
            else:
                self.logger.warning('Request returned with error code %s, retrying...' % response['code'])
                self._curl_newdex(path, state, cancel)
        self._retries = 0
        return response["data"]

    def _sign(self, message):
        '''Generate HmacSHA256 signature according to message.'''
        return hmac.new(key=bytes(self.secret, 'UTF-8'), msg=bytes(message, 'UTF-8'), 
        digestmod=hashlib.sha256).hexdigest()