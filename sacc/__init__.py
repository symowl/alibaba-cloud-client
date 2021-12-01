"""Symowl Alibaba Cloud Client
SPDX-License-Identifier: Apache-2.0
"""

__version__ = "1.1.0"

from .private import Private
from .public import Public


def client(
    ak: str,
    secret: str,
    region_id: str = "cn-hangzhou",
    private: bool = False,
    endpoint: str = None,
    user_agent: str = None
):
    if private:
        if endpoint is None:
            raise Exception("私有云 endpoint 为必填项")
        if user_agent is None:
            raise Exception("私有云 user_agent 为必填项")
        return Private(ak, secret, region_id, endpoint, user_agent)
    else:
        return Public(ak, secret, region_id)
