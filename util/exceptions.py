# coding=utf-8

class NewdexAPIException(Exception):
    '''Exception class to handle general API Exceptions'''
    def __init__(self, response):
        self.code = ''
        self.message = 'Unknown Error'
        try:
            json_res = response
        except ValueError:
            print("Can't parse error response: {}".format(response.text))
            self.message = response.text
        else:
            if 'msg' in json_res:
                self.message = json_res['msg']
                self.code = json_res['code']

    def __str__(self):
        return 'NewdexAPIException {}: {}'.format(self.code, self.message)