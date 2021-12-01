# SPDX-License-Identifier: Apache-2.0

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
