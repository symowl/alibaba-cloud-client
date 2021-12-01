"""Copyright 2021 Symowl

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

from .ecs import ECS, models
from .rds import RDS
from .waf import WAF


class Public(ECS, RDS, WAF):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str = "cn-hangzhou"
    ):
        ECS.__init__(self, ak, secret, region_id)
        RDS.__init__(self, ak, secret, region_id)
        WAF.__init__(self, ak, secret, region_id)

    def get_regions(self) -> list[dict[str, str]]:
        req = models.DescribeRegionsRequest()

        resp = self.ecs.describe_regions(req)
        resp = resp.body.to_map()
        resp = resp["Regions"]["Region"]

        return resp

    def set_region_id(self, region_id: str):
        self.ecs._region_id = region_id
        self.rds._region_id = region_id
        self.waf._region_id = region_id
        self.region_id = region_id
