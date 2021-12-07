# Copyright 2021 Symowl
# SPDX-License-Identifier: Apache-2.0

from .ecs import ECS, models
from .rds import RDS
from .waf import WAF


class Public(ECS, RDS, WAF):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str = "cn-hangzhou"
    ) -> None:
        ECS.__init__(self, ak, secret, region_id)
        RDS.__init__(self, ak, secret, region_id)
        WAF.__init__(self, ak, secret, region_id)

    def get_regions(self) -> list[dict[str, str]]:
        req = models.DescribeRegionsRequest()

        resp = self.ecs.describe_regions(req)
        resp = resp.body.to_map()
        resp = resp["Regions"]["Region"]

        return resp

    def set_region_id(self, region_id: str) -> None:
        self.ecs._region_id = region_id
        self.rds._region_id = region_id
        self.waf._region_id = region_id
        self.region_id = region_id
