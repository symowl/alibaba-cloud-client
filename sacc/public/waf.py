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

from alibabacloud_waf_openapi20190910 import client, models

from .config import Config


class WAF(Config):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str
    ):
        super().__init__(ak, secret, region_id)
        self.__client = client.Client(self.config)
        self.waf = self.__client

    def get_waf_domain_names(self, instance_id: str):
        req = models.DescribeDomainNamesRequest(
            instance_id=instance_id
        )

        resp = self.__client.describe_domain_names(req)
        resp = resp.body.to_map()

        return resp["DomainNames"]

    def get_waf_instance_infos(self):
        req = models.DescribeInstanceInfosRequest()

        resp = self.__client.describe_instance_infos(req)
        resp = resp.body.to_map()

        return resp["InstanceInfos"]

    def get_waf_protection_module_rules_ac_blacklist(self, instance_id: str, domain: str):
        req = models.DescribeProtectionModuleRulesRequest(
            domain=domain,
            defense_type="ac_blacklist",
            instance_id=instance_id
        )

        resp = self.__client.describe_protection_module_rules(req)
        resp = resp.body.to_map()
        resp = resp["Rules"][0]
        if resp["Content"].get("remoteAddr") is None:
            resp["Content"]["remoteAddr"] = []

        return resp

    def set_waf_protection_module_rule_ac_blacklist(self, instance_id: str, domain: str, remote_addr: list[str], rule_id: int):
        req = models.ModifyProtectionModuleRuleRequest(
            domain,
            "ac_blacklist",
            json.dumps({"remoteAddr": remote_addr}),
            rule_id,
            0,
            instance_id
        )

        self.__client.modify_protection_module_rule(req)
