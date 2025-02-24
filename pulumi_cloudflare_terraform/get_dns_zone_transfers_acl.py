# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetDnsZoneTransfersAclResult',
    'AwaitableGetDnsZoneTransfersAclResult',
    'get_dns_zone_transfers_acl',
    'get_dns_zone_transfers_acl_output',
]

@pulumi.output_type
class GetDnsZoneTransfersAclResult:
    """
    A collection of values returned by getDnsZoneTransfersAcl.
    """
    def __init__(__self__, account_id=None, acl_id=None, id=None, ip_range=None, name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if acl_id and not isinstance(acl_id, str):
            raise TypeError("Expected argument 'acl_id' to be a str")
        pulumi.set(__self__, "acl_id", acl_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_range and not isinstance(ip_range, str):
            raise TypeError("Expected argument 'ip_range' to be a str")
        pulumi.set(__self__, "ip_range", ip_range)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> Optional[str]:
        return pulumi.get(self, "acl_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> str:
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


class AwaitableGetDnsZoneTransfersAclResult(GetDnsZoneTransfersAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsZoneTransfersAclResult(
            account_id=self.account_id,
            acl_id=self.acl_id,
            id=self.id,
            ip_range=self.ip_range,
            name=self.name)


def get_dns_zone_transfers_acl(account_id: Optional[str] = None,
                               acl_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsZoneTransfersAclResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['aclId'] = acl_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getDnsZoneTransfersAcl:getDnsZoneTransfersAcl', __args__, opts=opts, typ=GetDnsZoneTransfersAclResult, package_ref=_utilities.get_package()).value

    return AwaitableGetDnsZoneTransfersAclResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        acl_id=pulumi.get(__ret__, 'acl_id'),
        id=pulumi.get(__ret__, 'id'),
        ip_range=pulumi.get(__ret__, 'ip_range'),
        name=pulumi.get(__ret__, 'name'))
def get_dns_zone_transfers_acl_output(account_id: Optional[pulumi.Input[str]] = None,
                                      acl_id: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsZoneTransfersAclResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['aclId'] = acl_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getDnsZoneTransfersAcl:getDnsZoneTransfersAcl', __args__, opts=opts, typ=GetDnsZoneTransfersAclResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetDnsZoneTransfersAclResult(
        account_id=pulumi.get(__response__, 'account_id'),
        acl_id=pulumi.get(__response__, 'acl_id'),
        id=pulumi.get(__response__, 'id'),
        ip_range=pulumi.get(__response__, 'ip_range'),
        name=pulumi.get(__response__, 'name')))
