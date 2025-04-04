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
    'GetArgoSmartRoutingResult',
    'AwaitableGetArgoSmartRoutingResult',
    'get_argo_smart_routing',
    'get_argo_smart_routing_output',
]

@pulumi.output_type
class GetArgoSmartRoutingResult:
    """
    A collection of values returned by getArgoSmartRouting.
    """
    def __init__(__self__, id=None, zone_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetArgoSmartRoutingResult(GetArgoSmartRoutingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArgoSmartRoutingResult(
            id=self.id,
            zone_id=self.zone_id)


def get_argo_smart_routing(zone_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArgoSmartRoutingResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getArgoSmartRouting:getArgoSmartRouting', __args__, opts=opts, typ=GetArgoSmartRoutingResult, package_ref=_utilities.get_package()).value

    return AwaitableGetArgoSmartRoutingResult(
        id=pulumi.get(__ret__, 'id'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_argo_smart_routing_output(zone_id: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetArgoSmartRoutingResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getArgoSmartRouting:getArgoSmartRouting', __args__, opts=opts, typ=GetArgoSmartRoutingResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetArgoSmartRoutingResult(
        id=pulumi.get(__response__, 'id'),
        zone_id=pulumi.get(__response__, 'zone_id')))
