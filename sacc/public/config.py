# SPDX-License-Identifier: Apache-2.0

from alibabacloud_tea_openapi import models


class Config:
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str
    ):
        self.config = models.Config(ak, secret, region_id=region_id)
        self.region_id = region_id
