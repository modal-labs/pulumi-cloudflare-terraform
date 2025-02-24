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
    'GetDnsZoneTransfersTsigResult',
    'AwaitableGetDnsZoneTransfersTsigResult',
    'get_dns_zone_transfers_tsig',
    'get_dns_zone_transfers_tsig_output',
]

@pulumi.output_type
class GetDnsZoneTransfersTsigResult:
    """
    A collection of values returned by getDnsZoneTransfersTsig.
    """
    def __init__(__self__, account_id=None, algo=None, id=None, name=None, secret=None, tsig_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if algo and not isinstance(algo, str):
            raise TypeError("Expected argument 'algo' to be a str")
        pulumi.set(__self__, "algo", algo)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if secret and not isinstance(secret, str):
            raise TypeError("Expected argument 'secret' to be a str")
        pulumi.set(__self__, "secret", secret)
        if tsig_id and not isinstance(tsig_id, str):
            raise TypeError("Expected argument 'tsig_id' to be a str")
        pulumi.set(__self__, "tsig_id", tsig_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def algo(self) -> str:
        return pulumi.get(self, "algo")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> str:
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="tsigId")
    def tsig_id(self) -> Optional[str]:
        return pulumi.get(self, "tsig_id")


class AwaitableGetDnsZoneTransfersTsigResult(GetDnsZoneTransfersTsigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsZoneTransfersTsigResult(
            account_id=self.account_id,
            algo=self.algo,
            id=self.id,
            name=self.name,
            secret=self.secret,
            tsig_id=self.tsig_id)


def get_dns_zone_transfers_tsig(account_id: Optional[str] = None,
                                tsig_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsZoneTransfersTsigResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['tsigId'] = tsig_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getDnsZoneTransfersTsig:getDnsZoneTransfersTsig', __args__, opts=opts, typ=GetDnsZoneTransfersTsigResult, package_ref=_utilities.get_package()).value

    return AwaitableGetDnsZoneTransfersTsigResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        algo=pulumi.get(__ret__, 'algo'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        secret=pulumi.get(__ret__, 'secret'),
        tsig_id=pulumi.get(__ret__, 'tsig_id'))
def get_dns_zone_transfers_tsig_output(account_id: Optional[pulumi.Input[str]] = None,
                                       tsig_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsZoneTransfersTsigResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['tsigId'] = tsig_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getDnsZoneTransfersTsig:getDnsZoneTransfersTsig', __args__, opts=opts, typ=GetDnsZoneTransfersTsigResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetDnsZoneTransfersTsigResult(
        account_id=pulumi.get(__response__, 'account_id'),
        algo=pulumi.get(__response__, 'algo'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        secret=pulumi.get(__response__, 'secret'),
        tsig_id=pulumi.get(__response__, 'tsig_id')))
