# Copyright (c) 2021 Symowl
# SPDX-License-Identifier: MIT

import json
from typing import Dict, List

from .client import Client


class RDS(Client):
    __PRODUCT = "Rds"
    __VERSION = "2014-08-15"

    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str,
        endpoint: str,
        user_agent: str
    ):
        super().__init__(ak, secret, region_id, endpoint, user_agent)

    def get_rds_instances(self) -> List[Dict[str, str]]:
        req = self.request(
            self.__PRODUCT,
            self.__VERSION,
            "DescribeDBInstances",
            self.endpoint
        )
        req.add_header("User-Agent", self.user_agent)
        page_number = 1
        req.add_query_param("PageNumber", page_number)

        db_instances = []
        while True:
            try:
                resp = json.loads(self.client.do_request(req))
            except Exception as e:
                print(e)
                return []
            resp = resp["Items"]["DBInstance"]

            if len(resp) == 0:
                break
            db_instances.extend(resp)
            page_number += 1
            req.add_query_param("PageNumber", page_number)

        return db_instances

    def get_rds_instance_ip_arrays(self, dbinstance_id: str) -> List[Dict[str, str]]:
        req = self.request(
            self.__PRODUCT,
            self.__VERSION,
            "DescribeDBInstanceIPArrayList",
            self.endpoint
        )
        req.add_header("User-Agent", self.user_agent)
        req.add_query_param("DBInstanceId", dbinstance_id)

        resp = json.loads(self.client.do_request(req))

        return resp["Items"]["DBInstanceIPArray"]
