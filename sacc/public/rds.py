from alibabacloud_rds20140815 import client, models

from .config import Config


class RDS(Config):
    def __init__(
        self,
        ak: str,
        secret: str,
        region_id: str
    ):
        super().__init__(ak, secret, region_id)
        self.__client = client.Client(self.config)
        self.rds = self.__client

    def get_rds_error_logs(self, dbinstance_id: str, start_time: str, end_time: str):
        req = models.DescribeErrorLogsRequest(
            dbinstance_id=dbinstance_id,
            start_time=start_time,
            end_time=end_time,
        )
        req.page_number = 1

        error_logs = []
        while True:
            try:
                resp = self.__client.describe_error_logs(req)
            except Exception as e:
                print(e)
                return []
            resp = resp.body.to_map()
            resp = resp["Items"]["ErrorLog"]

            if len(resp) == 0:
                break
            error_logs.extend(resp)
            req.page_number += 1

        return error_logs

    def get_rds_instances(self, region_id: str = None) -> list[dict[str, str]]:
        req = models.DescribeDBInstancesRequest(
            region_id=self.region_id if region_id is None else region_id,
        )
        req.page_number = 1

        db_instances = []
        while True:
            try:
                resp = self.__client.describe_dbinstances(req)
            except Exception as e:
                print(e)
                return []
            resp = resp.body.to_map()
            resp = resp["Items"]["DBInstance"]

            if len(resp) == 0:
                break
            db_instances.extend(resp)
            req.page_number += 1

        return db_instances

    def get_rds_instance_ip_arrays(self, dbinstance_id: str):
        req = models.DescribeDBInstanceIPArrayListRequest(
            dbinstance_id=dbinstance_id
        )

        resp = self.__client.describe_dbinstance_iparray_list(req)
        resp = resp.body.to_map()

        return resp["Items"]["DBInstanceIPArray"]

    def set_rds_modify_security_ips(
        self,
        dbinstance_id: str,
        dbinstance_iparray_name: str,
        security_ips: list[str]
    ):
        req = models.ModifySecurityIpsRequest(
            dbinstance_id=dbinstance_id,
            security_ips=",".join(security_ips),
            dbinstance_iparray_name=dbinstance_iparray_name,
            modify_mode="Append"
        )

        resp = self.__client.modify_security_ips(req)

        return resp.body.to_map()
