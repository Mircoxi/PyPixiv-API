class PixivBaseError(Exception):
    def __init__(self, reason: str):
        super(Exception, self).__init__(self, reason)
        self.reason = str(reason)

    def __str__(self):
        return self.reason


class PixivUnauthenticatedError(PixivBaseError):
   pass

