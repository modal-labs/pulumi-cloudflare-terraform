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
    'GetLoadBalancerPoolResult',
    'AwaitableGetLoadBalancerPoolResult',
    'get_load_balancer_pool',
    'get_load_balancer_pool_output',
]

@pulumi.output_type
class GetLoadBalancerPoolResult:
    """
    A collection of values returned by getLoadBalancerPool.
    """
    def __init__(__self__, account_id=None, check_regions=None, created_on=None, description=None, disabled_at=None, enabled=None, filter=None, id=None, latitude=None, load_shedding=None, longitude=None, minimum_origins=None, modified_on=None, monitor=None, name=None, networks=None, notification_email=None, notification_filter=None, origin_steering=None, origins=None, pool_id=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if check_regions and not isinstance(check_regions, list):
            raise TypeError("Expected argument 'check_regions' to be a list")
        pulumi.set(__self__, "check_regions", check_regions)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disabled_at and not isinstance(disabled_at, str):
            raise TypeError("Expected argument 'disabled_at' to be a str")
        pulumi.set(__self__, "disabled_at", disabled_at)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if latitude and not isinstance(latitude, float):
            raise TypeError("Expected argument 'latitude' to be a float")
        pulumi.set(__self__, "latitude", latitude)
        if load_shedding and not isinstance(load_shedding, dict):
            raise TypeError("Expected argument 'load_shedding' to be a dict")
        pulumi.set(__self__, "load_shedding", load_shedding)
        if longitude and not isinstance(longitude, float):
            raise TypeError("Expected argument 'longitude' to be a float")
        pulumi.set(__self__, "longitude", longitude)
        if minimum_origins and not isinstance(minimum_origins, float):
            raise TypeError("Expected argument 'minimum_origins' to be a float")
        pulumi.set(__self__, "minimum_origins", minimum_origins)
        if modified_on and not isinstance(modified_on, str):
            raise TypeError("Expected argument 'modified_on' to be a str")
        pulumi.set(__self__, "modified_on", modified_on)
        if monitor and not isinstance(monitor, str):
            raise TypeError("Expected argument 'monitor' to be a str")
        pulumi.set(__self__, "monitor", monitor)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if networks and not isinstance(networks, list):
            raise TypeError("Expected argument 'networks' to be a list")
        pulumi.set(__self__, "networks", networks)
        if notification_email and not isinstance(notification_email, str):
            raise TypeError("Expected argument 'notification_email' to be a str")
        pulumi.set(__self__, "notification_email", notification_email)
        if notification_filter and not isinstance(notification_filter, dict):
            raise TypeError("Expected argument 'notification_filter' to be a dict")
        pulumi.set(__self__, "notification_filter", notification_filter)
        if origin_steering and not isinstance(origin_steering, dict):
            raise TypeError("Expected argument 'origin_steering' to be a dict")
        pulumi.set(__self__, "origin_steering", origin_steering)
        if origins and not isinstance(origins, list):
            raise TypeError("Expected argument 'origins' to be a list")
        pulumi.set(__self__, "origins", origins)
        if pool_id and not isinstance(pool_id, str):
            raise TypeError("Expected argument 'pool_id' to be a str")
        pulumi.set(__self__, "pool_id", pool_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="checkRegions")
    def check_regions(self) -> Sequence[str]:
        return pulumi.get(self, "check_regions")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disabledAt")
    def disabled_at(self) -> str:
        return pulumi.get(self, "disabled_at")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetLoadBalancerPoolFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def latitude(self) -> float:
        return pulumi.get(self, "latitude")

    @property
    @pulumi.getter(name="loadShedding")
    def load_shedding(self) -> 'outputs.GetLoadBalancerPoolLoadSheddingResult':
        return pulumi.get(self, "load_shedding")

    @property
    @pulumi.getter
    def longitude(self) -> float:
        return pulumi.get(self, "longitude")

    @property
    @pulumi.getter(name="minimumOrigins")
    def minimum_origins(self) -> float:
        return pulumi.get(self, "minimum_origins")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> str:
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def monitor(self) -> str:
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> Sequence[str]:
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> str:
        return pulumi.get(self, "notification_email")

    @property
    @pulumi.getter(name="notificationFilter")
    def notification_filter(self) -> 'outputs.GetLoadBalancerPoolNotificationFilterResult':
        return pulumi.get(self, "notification_filter")

    @property
    @pulumi.getter(name="originSteering")
    def origin_steering(self) -> 'outputs.GetLoadBalancerPoolOriginSteeringResult':
        return pulumi.get(self, "origin_steering")

    @property
    @pulumi.getter
    def origins(self) -> Sequence['outputs.GetLoadBalancerPoolOriginResult']:
        return pulumi.get(self, "origins")

    @property
    @pulumi.getter(name="poolId")
    def pool_id(self) -> Optional[str]:
        return pulumi.get(self, "pool_id")


class AwaitableGetLoadBalancerPoolResult(GetLoadBalancerPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLoadBalancerPoolResult(
            account_id=self.account_id,
            check_regions=self.check_regions,
            created_on=self.created_on,
            description=self.description,
            disabled_at=self.disabled_at,
            enabled=self.enabled,
            filter=self.filter,
            id=self.id,
            latitude=self.latitude,
            load_shedding=self.load_shedding,
            longitude=self.longitude,
            minimum_origins=self.minimum_origins,
            modified_on=self.modified_on,
            monitor=self.monitor,
            name=self.name,
            networks=self.networks,
            notification_email=self.notification_email,
            notification_filter=self.notification_filter,
            origin_steering=self.origin_steering,
            origins=self.origins,
            pool_id=self.pool_id)


def get_load_balancer_pool(account_id: Optional[str] = None,
                           filter: Optional[Union['GetLoadBalancerPoolFilterArgs', 'GetLoadBalancerPoolFilterArgsDict']] = None,
                           pool_id: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLoadBalancerPoolResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['poolId'] = pool_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getLoadBalancerPool:getLoadBalancerPool', __args__, opts=opts, typ=GetLoadBalancerPoolResult, package_ref=_utilities.get_package()).value

    return AwaitableGetLoadBalancerPoolResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        check_regions=pulumi.get(__ret__, 'check_regions'),
        created_on=pulumi.get(__ret__, 'created_on'),
        description=pulumi.get(__ret__, 'description'),
        disabled_at=pulumi.get(__ret__, 'disabled_at'),
        enabled=pulumi.get(__ret__, 'enabled'),
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        latitude=pulumi.get(__ret__, 'latitude'),
        load_shedding=pulumi.get(__ret__, 'load_shedding'),
        longitude=pulumi.get(__ret__, 'longitude'),
        minimum_origins=pulumi.get(__ret__, 'minimum_origins'),
        modified_on=pulumi.get(__ret__, 'modified_on'),
        monitor=pulumi.get(__ret__, 'monitor'),
        name=pulumi.get(__ret__, 'name'),
        networks=pulumi.get(__ret__, 'networks'),
        notification_email=pulumi.get(__ret__, 'notification_email'),
        notification_filter=pulumi.get(__ret__, 'notification_filter'),
        origin_steering=pulumi.get(__ret__, 'origin_steering'),
        origins=pulumi.get(__ret__, 'origins'),
        pool_id=pulumi.get(__ret__, 'pool_id'))
def get_load_balancer_pool_output(account_id: Optional[pulumi.Input[str]] = None,
                                  filter: Optional[pulumi.Input[Optional[Union['GetLoadBalancerPoolFilterArgs', 'GetLoadBalancerPoolFilterArgsDict']]]] = None,
                                  pool_id: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetLoadBalancerPoolResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['poolId'] = pool_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getLoadBalancerPool:getLoadBalancerPool', __args__, opts=opts, typ=GetLoadBalancerPoolResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetLoadBalancerPoolResult(
        account_id=pulumi.get(__response__, 'account_id'),
        check_regions=pulumi.get(__response__, 'check_regions'),
        created_on=pulumi.get(__response__, 'created_on'),
        description=pulumi.get(__response__, 'description'),
        disabled_at=pulumi.get(__response__, 'disabled_at'),
        enabled=pulumi.get(__response__, 'enabled'),
        filter=pulumi.get(__response__, 'filter'),
        id=pulumi.get(__response__, 'id'),
        latitude=pulumi.get(__response__, 'latitude'),
        load_shedding=pulumi.get(__response__, 'load_shedding'),
        longitude=pulumi.get(__response__, 'longitude'),
        minimum_origins=pulumi.get(__response__, 'minimum_origins'),
        modified_on=pulumi.get(__response__, 'modified_on'),
        monitor=pulumi.get(__response__, 'monitor'),
        name=pulumi.get(__response__, 'name'),
        networks=pulumi.get(__response__, 'networks'),
        notification_email=pulumi.get(__response__, 'notification_email'),
        notification_filter=pulumi.get(__response__, 'notification_filter'),
        origin_steering=pulumi.get(__response__, 'origin_steering'),
        origins=pulumi.get(__response__, 'origins'),
        pool_id=pulumi.get(__response__, 'pool_id')))
