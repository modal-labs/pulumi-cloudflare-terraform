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
    'GetApiShieldDiscoveryOperationsResult',
    'AwaitableGetApiShieldDiscoveryOperationsResult',
    'get_api_shield_discovery_operations',
    'get_api_shield_discovery_operations_output',
]

@pulumi.output_type
class GetApiShieldDiscoveryOperationsResult:
    """
    A collection of values returned by getApiShieldDiscoveryOperations.
    """
    def __init__(__self__, diff=None, direction=None, endpoint=None, hosts=None, id=None, max_items=None, methods=None, order=None, origin=None, results=None, state=None, zone_id=None):
        if diff and not isinstance(diff, bool):
            raise TypeError("Expected argument 'diff' to be a bool")
        pulumi.set(__self__, "diff", diff)
        if direction and not isinstance(direction, str):
            raise TypeError("Expected argument 'direction' to be a str")
        pulumi.set(__self__, "direction", direction)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if hosts and not isinstance(hosts, list):
            raise TypeError("Expected argument 'hosts' to be a list")
        pulumi.set(__self__, "hosts", hosts)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if methods and not isinstance(methods, list):
            raise TypeError("Expected argument 'methods' to be a list")
        pulumi.set(__self__, "methods", methods)
        if order and not isinstance(order, str):
            raise TypeError("Expected argument 'order' to be a str")
        pulumi.set(__self__, "order", order)
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        pulumi.set(__self__, "origin", origin)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def diff(self) -> Optional[bool]:
        return pulumi.get(self, "diff")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[str]:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def hosts(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "hosts")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[float]:
        return pulumi.get(self, "max_items")

    @property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "methods")

    @property
    @pulumi.getter
    def order(self) -> Optional[str]:
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def origin(self) -> Optional[str]:
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetApiShieldDiscoveryOperationsResultResult']:
        return pulumi.get(self, "results")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetApiShieldDiscoveryOperationsResult(GetApiShieldDiscoveryOperationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiShieldDiscoveryOperationsResult(
            diff=self.diff,
            direction=self.direction,
            endpoint=self.endpoint,
            hosts=self.hosts,
            id=self.id,
            max_items=self.max_items,
            methods=self.methods,
            order=self.order,
            origin=self.origin,
            results=self.results,
            state=self.state,
            zone_id=self.zone_id)


def get_api_shield_discovery_operations(diff: Optional[bool] = None,
                                        direction: Optional[str] = None,
                                        endpoint: Optional[str] = None,
                                        hosts: Optional[Sequence[str]] = None,
                                        max_items: Optional[float] = None,
                                        methods: Optional[Sequence[str]] = None,
                                        order: Optional[str] = None,
                                        origin: Optional[str] = None,
                                        state: Optional[str] = None,
                                        zone_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiShieldDiscoveryOperationsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['diff'] = diff
    __args__['direction'] = direction
    __args__['endpoint'] = endpoint
    __args__['hosts'] = hosts
    __args__['maxItems'] = max_items
    __args__['methods'] = methods
    __args__['order'] = order
    __args__['origin'] = origin
    __args__['state'] = state
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getApiShieldDiscoveryOperations:getApiShieldDiscoveryOperations', __args__, opts=opts, typ=GetApiShieldDiscoveryOperationsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetApiShieldDiscoveryOperationsResult(
        diff=pulumi.get(__ret__, 'diff'),
        direction=pulumi.get(__ret__, 'direction'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        hosts=pulumi.get(__ret__, 'hosts'),
        id=pulumi.get(__ret__, 'id'),
        max_items=pulumi.get(__ret__, 'max_items'),
        methods=pulumi.get(__ret__, 'methods'),
        order=pulumi.get(__ret__, 'order'),
        origin=pulumi.get(__ret__, 'origin'),
        results=pulumi.get(__ret__, 'results'),
        state=pulumi.get(__ret__, 'state'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_api_shield_discovery_operations_output(diff: Optional[pulumi.Input[Optional[bool]]] = None,
                                               direction: Optional[pulumi.Input[Optional[str]]] = None,
                                               endpoint: Optional[pulumi.Input[Optional[str]]] = None,
                                               hosts: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               max_items: Optional[pulumi.Input[Optional[float]]] = None,
                                               methods: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                               order: Optional[pulumi.Input[Optional[str]]] = None,
                                               origin: Optional[pulumi.Input[Optional[str]]] = None,
                                               state: Optional[pulumi.Input[Optional[str]]] = None,
                                               zone_id: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetApiShieldDiscoveryOperationsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['diff'] = diff
    __args__['direction'] = direction
    __args__['endpoint'] = endpoint
    __args__['hosts'] = hosts
    __args__['maxItems'] = max_items
    __args__['methods'] = methods
    __args__['order'] = order
    __args__['origin'] = origin
    __args__['state'] = state
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getApiShieldDiscoveryOperations:getApiShieldDiscoveryOperations', __args__, opts=opts, typ=GetApiShieldDiscoveryOperationsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetApiShieldDiscoveryOperationsResult(
        diff=pulumi.get(__response__, 'diff'),
        direction=pulumi.get(__response__, 'direction'),
        endpoint=pulumi.get(__response__, 'endpoint'),
        hosts=pulumi.get(__response__, 'hosts'),
        id=pulumi.get(__response__, 'id'),
        max_items=pulumi.get(__response__, 'max_items'),
        methods=pulumi.get(__response__, 'methods'),
        order=pulumi.get(__response__, 'order'),
        origin=pulumi.get(__response__, 'origin'),
        results=pulumi.get(__response__, 'results'),
        state=pulumi.get(__response__, 'state'),
        zone_id=pulumi.get(__response__, 'zone_id')))
