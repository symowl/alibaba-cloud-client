# SPDX-License-Identifier: Apache-2.0

from aliyunsdkasapi.AsapiRequest import AsapiRequest
from aliyunsdkasapi.client import AcsClient


class Client:
    request = AsapiRequest

    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str,
        endpoint: str,
        user_agent: str
    ):
        self.client = AcsClient(ak, secret, region_id)
        self.endpoint = endpoint
        self.user_agent = user_agent
