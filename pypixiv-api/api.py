import hashlib
from requests.structures import CaseInsensitiveDict
import json
import os
from datetime import datetime
from .exceptions import PixivUnauthenticatedError

class PixivAPI:
    """
    Base class for the Pixiv API interaction, based on the Android app. Extensions - e.g. dummy APIs for testing -
    can inherit from this one.


    """

    _client_id: str = "MOBrBDS8blbauoSck0ZfDbtuzpyT"
    _client_secret: str = "lsACyCD94FhDUtGTXi3QzcFE2uU1hqtDaKeqrdwj"
    _hash_secret: str = "28c1fdd170a5204386cb1313c7077b34f83e4aaf4aa829ce78c231e05b0bae2c"
    _host = "https://app-api.pixiv.net"
    def __init__(self, **kwargs):
        self.user_id: int | None = None
        self.access_token: str | None = None
        self.refresh_token: str | None = None
        self.user_name: str | None = None
        self._extra_headers: CaseInsensitiveDict = CaseInsensitiveDict()

        # Process kwargs, if provided.
        self._cooldown_multiplier = kwargs.get('cooldown_multiplier', 1)
        self._accept_language = kwargs.get('accept_language', 'en-us')
        self._extra_headers['Accept-Language'] = self._accept_language

    def require_auth(self, func):
        """
        Decorator method to wrap functions that need auth.
        :return:
        """
        def check_auth_status():
            if self.access_token is None:
                raise PixivUnauthenticatedError('Not yet authenticated! Call auth(refresh_token) first.')
            func()

        return check_auth_status

