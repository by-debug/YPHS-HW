# -*- coding: utf-8 -*-
class YPHSError(ValueError):
    pass


class LogInError(YPHSError):
    pass


class HwIndexError(YPHSError):
    pass


class PasswordError(YPHSError):
    pass

class InputSyntaxError(YPHSError):
    pass