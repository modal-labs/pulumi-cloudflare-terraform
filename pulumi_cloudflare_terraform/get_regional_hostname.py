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
    'GetRegionalHostnameResult',
    'AwaitableGetRegionalHostnameResult',
    'get_regional_hostname',
    'get_regional_hostname_output',
]

@pulumi.output_type
class GetRegionalHostnameResult:
    """
    A collection of values returned by getRegionalHostname.
    """
    def __init__(__self__, created_on=None, hostname=None, id=None, region_key=None, zone_id=None):
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region_key and not isinstance(region_key, str):
            raise TypeError("Expected argument 'region_key' to be a str")
        pulumi.set(__self__, "region_key", region_key)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="regionKey")
    def region_key(self) -> str:
        return pulumi.get(self, "region_key")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetRegionalHostnameResult(GetRegionalHostnameResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegionalHostnameResult(
            created_on=self.created_on,
            hostname=self.hostname,
            id=self.id,
            region_key=self.region_key,
            zone_id=self.zone_id)


def get_regional_hostname(hostname: Optional[str] = None,
                          zone_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegionalHostnameResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['hostname'] = hostname
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getRegionalHostname:getRegionalHostname', __args__, opts=opts, typ=GetRegionalHostnameResult, package_ref=_utilities.get_package()).value

    return AwaitableGetRegionalHostnameResult(
        created_on=pulumi.get(__ret__, 'created_on'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        region_key=pulumi.get(__ret__, 'region_key'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_regional_hostname_output(hostname: Optional[pulumi.Input[Optional[str]]] = None,
                                 zone_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetRegionalHostnameResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['hostname'] = hostname
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getRegionalHostname:getRegionalHostname', __args__, opts=opts, typ=GetRegionalHostnameResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetRegionalHostnameResult(
        created_on=pulumi.get(__response__, 'created_on'),
        hostname=pulumi.get(__response__, 'hostname'),
        id=pulumi.get(__response__, 'id'),
        region_key=pulumi.get(__response__, 'region_key'),
        zone_id=pulumi.get(__response__, 'zone_id')))
