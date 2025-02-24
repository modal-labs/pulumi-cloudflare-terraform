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
    'GetZoneCacheReserveResult',
    'AwaitableGetZoneCacheReserveResult',
    'get_zone_cache_reserve',
    'get_zone_cache_reserve_output',
]

@pulumi.output_type
class GetZoneCacheReserveResult:
    """
    A collection of values returned by getZoneCacheReserve.
    """
    def __init__(__self__, editable=None, id=None, modified_on=None, value=None, zone_id=None):
        if editable and not isinstance(editable, bool):
            raise TypeError("Expected argument 'editable' to be a bool")
        pulumi.set(__self__, "editable", editable)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modified_on and not isinstance(modified_on, str):
            raise TypeError("Expected argument 'modified_on' to be a str")
        pulumi.set(__self__, "modified_on", modified_on)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def editable(self) -> bool:
        return pulumi.get(self, "editable")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> str:
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetZoneCacheReserveResult(GetZoneCacheReserveResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZoneCacheReserveResult(
            editable=self.editable,
            id=self.id,
            modified_on=self.modified_on,
            value=self.value,
            zone_id=self.zone_id)


def get_zone_cache_reserve(zone_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZoneCacheReserveResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZoneCacheReserve:getZoneCacheReserve', __args__, opts=opts, typ=GetZoneCacheReserveResult, package_ref=_utilities.get_package()).value

    return AwaitableGetZoneCacheReserveResult(
        editable=pulumi.get(__ret__, 'editable'),
        id=pulumi.get(__ret__, 'id'),
        modified_on=pulumi.get(__ret__, 'modified_on'),
        value=pulumi.get(__ret__, 'value'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_zone_cache_reserve_output(zone_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZoneCacheReserveResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getZoneCacheReserve:getZoneCacheReserve', __args__, opts=opts, typ=GetZoneCacheReserveResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetZoneCacheReserveResult(
        editable=pulumi.get(__response__, 'editable'),
        id=pulumi.get(__response__, 'id'),
        modified_on=pulumi.get(__response__, 'modified_on'),
        value=pulumi.get(__response__, 'value'),
        zone_id=pulumi.get(__response__, 'zone_id')))
