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
    'GetDnsZoneTransfersPeerResult',
    'AwaitableGetDnsZoneTransfersPeerResult',
    'get_dns_zone_transfers_peer',
    'get_dns_zone_transfers_peer_output',
]

@pulumi.output_type
class GetDnsZoneTransfersPeerResult:
    """
    A collection of values returned by getDnsZoneTransfersPeer.
    """
    def __init__(__self__, account_id=None, id=None, ip=None, ixfr_enable=None, name=None, peer_id=None, port=None, tsig_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if ixfr_enable and not isinstance(ixfr_enable, bool):
            raise TypeError("Expected argument 'ixfr_enable' to be a bool")
        pulumi.set(__self__, "ixfr_enable", ixfr_enable)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peer_id and not isinstance(peer_id, str):
            raise TypeError("Expected argument 'peer_id' to be a str")
        pulumi.set(__self__, "peer_id", peer_id)
        if port and not isinstance(port, float):
            raise TypeError("Expected argument 'port' to be a float")
        pulumi.set(__self__, "port", port)
        if tsig_id and not isinstance(tsig_id, str):
            raise TypeError("Expected argument 'tsig_id' to be a str")
        pulumi.set(__self__, "tsig_id", tsig_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="ixfrEnable")
    def ixfr_enable(self) -> bool:
        return pulumi.get(self, "ixfr_enable")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerId")
    def peer_id(self) -> Optional[str]:
        return pulumi.get(self, "peer_id")

    @property
    @pulumi.getter
    def port(self) -> float:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="tsigId")
    def tsig_id(self) -> str:
        return pulumi.get(self, "tsig_id")


class AwaitableGetDnsZoneTransfersPeerResult(GetDnsZoneTransfersPeerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsZoneTransfersPeerResult(
            account_id=self.account_id,
            id=self.id,
            ip=self.ip,
            ixfr_enable=self.ixfr_enable,
            name=self.name,
            peer_id=self.peer_id,
            port=self.port,
            tsig_id=self.tsig_id)


def get_dns_zone_transfers_peer(account_id: Optional[str] = None,
                                peer_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsZoneTransfersPeerResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['peerId'] = peer_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getDnsZoneTransfersPeer:getDnsZoneTransfersPeer', __args__, opts=opts, typ=GetDnsZoneTransfersPeerResult, package_ref=_utilities.get_package()).value

    return AwaitableGetDnsZoneTransfersPeerResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        ixfr_enable=pulumi.get(__ret__, 'ixfr_enable'),
        name=pulumi.get(__ret__, 'name'),
        peer_id=pulumi.get(__ret__, 'peer_id'),
        port=pulumi.get(__ret__, 'port'),
        tsig_id=pulumi.get(__ret__, 'tsig_id'))
def get_dns_zone_transfers_peer_output(account_id: Optional[pulumi.Input[str]] = None,
                                       peer_id: Optional[pulumi.Input[Optional[str]]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsZoneTransfersPeerResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['peerId'] = peer_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getDnsZoneTransfersPeer:getDnsZoneTransfersPeer', __args__, opts=opts, typ=GetDnsZoneTransfersPeerResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetDnsZoneTransfersPeerResult(
        account_id=pulumi.get(__response__, 'account_id'),
        id=pulumi.get(__response__, 'id'),
        ip=pulumi.get(__response__, 'ip'),
        ixfr_enable=pulumi.get(__response__, 'ixfr_enable'),
        name=pulumi.get(__response__, 'name'),
        peer_id=pulumi.get(__response__, 'peer_id'),
        port=pulumi.get(__response__, 'port'),
        tsig_id=pulumi.get(__response__, 'tsig_id')))
