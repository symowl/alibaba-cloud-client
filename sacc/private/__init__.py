# SPDX-License-Identifier: Apache-2.0

from .ecs import ECS
from .rds import RDS


class Private(ECS, RDS):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str,
        endpoint: str,
        user_agent: str
    ):
        ECS.__init__(self, ak, secret, region_id, endpoint, user_agent)
        RDS.__init__(self, ak, secret, region_id, endpoint, user_agent)
