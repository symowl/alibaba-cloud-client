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

import json

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

    def get_rds_instances(self) -> list[dict[str, str]]:
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

    def get_rds_instance_ip_arrays(self, dbinstance_id: str):
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
