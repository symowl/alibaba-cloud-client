# SPDX-License-Identifier: Apache-2.0

import json

from .client import Client


class ECS(Client):
    __PRODUCT = "Ecs"
    __VERSION = "2014-05-26"

    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str,
        endpoint: str,
        user_agent: str
    ):
        super().__init__(ak, secret, region_id, endpoint, user_agent)

    def get_ecs_instance_status(self, instance_ids: list[str] = None) -> list[dict[str, str]]:
        req = self.request(
            self.__PRODUCT,
            self.__VERSION,
            "DescribeInstanceStatus",
            self.endpoint
        )
        req.add_header("User-Agent", self.user_agent)
        page_number = 1
        req.add_query_param("PageNumber", page_number)
        if instance_ids is not None:
            req.add_query_param("InstanceIds", str(instance_ids))

        status = []
        while True:
            try:
                resp = json.loads(self.client.do_request(req))
            except Exception as e:
                print(e)
                return []
            resp = resp["InstanceStatuses"]["InstanceStatus"]

            if len(resp) == 0:
                break
            status.extend(resp)
            page_number += 1
            req.add_query_param("PageNumber", page_number)

        return status

    def get_ecs_instances(self, instance_ids: list[str] = None) -> list[dict[str, str]]:
        req = self.request(
            self.__PRODUCT,
            self.__VERSION,
            "DescribeInstances",
            self.endpoint
        )
        req.add_header("User-Agent", self.user_agent)
        page_number = 1
        req.add_query_param("PageNumber", page_number)
        if instance_ids is not None:
            req.add_query_param("InstanceIds", str(instance_ids))

        instances = []
        while True:
            try:
                resp = json.loads(self.client.do_request(req))
            except Exception as e:
                print(e)
                return []
            resp = resp["Instances"]["Instance"]

            if len(resp) == 0:
                break
            instances.extend(resp)
            page_number += 1
            req.add_query_param("PageNumber", page_number)

        return instances
