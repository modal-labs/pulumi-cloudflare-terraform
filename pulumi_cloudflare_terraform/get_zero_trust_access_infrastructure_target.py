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
from . import outputs
from ._inputs import *

__all__ = [
    'GetZeroTrustAccessInfrastructureTargetResult',
    'AwaitableGetZeroTrustAccessInfrastructureTargetResult',
    'get_zero_trust_access_infrastructure_target',
    'get_zero_trust_access_infrastructure_target_output',
]

@pulumi.output_type
class GetZeroTrustAccessInfrastructureTargetResult:
    """
    A collection of values returned by getZeroTrustAccessInfrastructureTarget.
    """
    def __init__(__self__, account_id=None, created_at=None, filter=None, hostname=None, id=None, ip=None, modified_at=None, target_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, dict):
            raise TypeError("Expected argument 'ip' to be a dict")
        pulumi.set(__self__, "ip", ip)
        if modified_at and not isinstance(modified_at, str):
            raise TypeError("Expected argument 'modified_at' to be a str")
        pulumi.set(__self__, "modified_at", modified_at)
        if target_id and not isinstance(target_id, str):
            raise TypeError("Expected argument 'target_id' to be a str")
        pulumi.set(__self__, "target_id", target_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetZeroTrustAccessInfrastructureTargetFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> 'outputs.GetZeroTrustAccessInfrastructureTargetIpResult':
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="modifiedAt")
    def modified_at(self) -> str:
        return pulumi.get(self, "modified_at")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[str]:
        return pulumi.get(self, "target_id")


class AwaitableGetZeroTrustAccessInfrastructureTargetResult(GetZeroTrustAccessInfrastructureTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZeroTrustAccessInfrastructureTargetResult(
            account_id=self.account_id,
            created_at=self.created_at,
            filter=self.filter,
            hostname=self.hostname,
            id=self.id,
            ip=self.ip,
            modified_at=self.modified_at,
            target_id=self.target_id)


def get_zero_trust_access_infrastructure_target(account_id: Optional[str] = None,
                                                filter: Optional[Union['GetZeroTrustAccessInfrastructureTargetFilterArgs', 'GetZeroTrustAccessInfrastructureTargetFilterArgsDict']] = None,
                                                target_id: Optional[str] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZeroTrustAccessInfrastructureTargetResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['targetId'] = target_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZeroTrustAccessInfrastructureTarget:getZeroTrustAccessInfrastructureTarget', __args__, opts=opts, typ=GetZeroTrustAccessInfrastructureTargetResult, package_ref=_utilities.get_package()).value

    return AwaitableGetZeroTrustAccessInfrastructureTargetResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        filter=pulumi.get(__ret__, 'filter'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        modified_at=pulumi.get(__ret__, 'modified_at'),
        target_id=pulumi.get(__ret__, 'target_id'))
def get_zero_trust_access_infrastructure_target_output(account_id: Optional[pulumi.Input[str]] = None,
                                                       filter: Optional[pulumi.Input[Optional[Union['GetZeroTrustAccessInfrastructureTargetFilterArgs', 'GetZeroTrustAccessInfrastructureTargetFilterArgsDict']]]] = None,
                                                       target_id: Optional[pulumi.Input[Optional[str]]] = None,
                                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZeroTrustAccessInfrastructureTargetResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['targetId'] = target_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getZeroTrustAccessInfrastructureTarget:getZeroTrustAccessInfrastructureTarget', __args__, opts=opts, typ=GetZeroTrustAccessInfrastructureTargetResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetZeroTrustAccessInfrastructureTargetResult(
        account_id=pulumi.get(__response__, 'account_id'),
        created_at=pulumi.get(__response__, 'created_at'),
        filter=pulumi.get(__response__, 'filter'),
        hostname=pulumi.get(__response__, 'hostname'),
        id=pulumi.get(__response__, 'id'),
        ip=pulumi.get(__response__, 'ip'),
        modified_at=pulumi.get(__response__, 'modified_at'),
        target_id=pulumi.get(__response__, 'target_id')))
