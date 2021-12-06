# Copyright (c) 2021 Symowl
# SPDX-License-Identifier: MIT

from alibabacloud_ecs20140526 import client, models

from .config import Config


class ECS(Config):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str
    ):
        super().__init__(ak, secret, region_id)
        self.__client = client.Client(self.config)
        self.ecs = self.__client

    def get_ecs_instance_status(
        self,
        region_id: str = None,
        instance_ids: list[str] = None
    ) -> list[dict[str, str]]:
        req = models.DescribeInstanceStatusRequest(
            region_id=self.region_id if region_id is None else region_id,
            instance_id=instance_ids
        )
        req.page_number = 1

        status = []
        while True:
            try:
                resp = self.__client.describe_instance_status(req)
            except Exception as e:
                print(e)
                return []
            resp = resp.body.to_map()
            resp = resp["InstanceStatuses"]["InstanceStatus"]

            if len(resp) == 0:
                break
            status.extend(resp)
            req.page_number += 1

        return status

    def get_ecs_instances(
        self,
        region_id: str = None,
        instance_ids: list[str] = None
    ) -> list[dict[str, str]]:
        req = models.DescribeInstancesRequest(
            region_id=self.region_id if region_id is None else region_id,
            instance_ids=None if instance_ids is None else str(instance_ids)
        )
        req.page_number = 1

        instances = []
        while True:
            try:
                resp = self.__client.describe_instances(req)
            except Exception as e:
                print(e)
                return []
            resp = resp.body.to_map()
            resp = resp["Instances"]["Instance"]

            if len(resp) == 0:
                break
            instances.extend(resp)
            req.page_number += 1

        return instances
