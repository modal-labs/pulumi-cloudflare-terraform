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

__all__ = [
    'GetCustomSslsResult',
    'AwaitableGetCustomSslsResult',
    'get_custom_ssls',
    'get_custom_ssls_output',
]

@pulumi.output_type
class GetCustomSslsResult:
    """
    A collection of values returned by getCustomSsls.
    """
    def __init__(__self__, id=None, match=None, max_items=None, results=None, status=None, zone_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if match and not isinstance(match, str):
            raise TypeError("Expected argument 'match' to be a str")
        pulumi.set(__self__, "match", match)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
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
    @pulumi.getter
    def match(self) -> str:
        return pulumi.get(self, "match")

    @property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[float]:
        return pulumi.get(self, "max_items")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetCustomSslsResultResult']:
        return pulumi.get(self, "results")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetCustomSslsResult(GetCustomSslsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomSslsResult(
            id=self.id,
            match=self.match,
            max_items=self.max_items,
            results=self.results,
            status=self.status,
            zone_id=self.zone_id)


def get_custom_ssls(match: Optional[str] = None,
                    max_items: Optional[float] = None,
                    status: Optional[str] = None,
                    zone_id: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomSslsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['match'] = match
    __args__['maxItems'] = max_items
    __args__['status'] = status
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getCustomSsls:getCustomSsls', __args__, opts=opts, typ=GetCustomSslsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetCustomSslsResult(
        id=pulumi.get(__ret__, 'id'),
        match=pulumi.get(__ret__, 'match'),
        max_items=pulumi.get(__ret__, 'max_items'),
        results=pulumi.get(__ret__, 'results'),
        status=pulumi.get(__ret__, 'status'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_custom_ssls_output(match: Optional[pulumi.Input[Optional[str]]] = None,
                           max_items: Optional[pulumi.Input[Optional[float]]] = None,
                           status: Optional[pulumi.Input[Optional[str]]] = None,
                           zone_id: Optional[pulumi.Input[str]] = None,
                           opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCustomSslsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['match'] = match
    __args__['maxItems'] = max_items
    __args__['status'] = status
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getCustomSsls:getCustomSsls', __args__, opts=opts, typ=GetCustomSslsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetCustomSslsResult(
        id=pulumi.get(__response__, 'id'),
        match=pulumi.get(__response__, 'match'),
        max_items=pulumi.get(__response__, 'max_items'),
        results=pulumi.get(__response__, 'results'),
        status=pulumi.get(__response__, 'status'),
        zone_id=pulumi.get(__response__, 'zone_id')))
