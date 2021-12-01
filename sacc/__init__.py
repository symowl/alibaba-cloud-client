"""Symowl Alibaba Cloud Client

Copyright 2021 Symowl

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
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
