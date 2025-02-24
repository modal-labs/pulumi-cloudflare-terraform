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
    'GetEmailRoutingAddressesResult',
    'AwaitableGetEmailRoutingAddressesResult',
    'get_email_routing_addresses',
    'get_email_routing_addresses_output',
]

@pulumi.output_type
class GetEmailRoutingAddressesResult:
    """
    A collection of values returned by getEmailRoutingAddresses.
    """
    def __init__(__self__, account_id=None, direction=None, id=None, max_items=None, results=None, verified=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if direction and not isinstance(direction, str):
            raise TypeError("Expected argument 'direction' to be a str")
        pulumi.set(__self__, "direction", direction)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if verified and not isinstance(verified, bool):
            raise TypeError("Expected argument 'verified' to be a bool")
        pulumi.set(__self__, "verified", verified)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def direction(self) -> str:
        return pulumi.get(self, "direction")

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
    def results(self) -> Sequence['outputs.GetEmailRoutingAddressesResultResult']:
        return pulumi.get(self, "results")

    @property
    @pulumi.getter
    def verified(self) -> bool:
        return pulumi.get(self, "verified")


class AwaitableGetEmailRoutingAddressesResult(GetEmailRoutingAddressesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEmailRoutingAddressesResult(
            account_id=self.account_id,
            direction=self.direction,
            id=self.id,
            max_items=self.max_items,
            results=self.results,
            verified=self.verified)


def get_email_routing_addresses(account_id: Optional[str] = None,
                                direction: Optional[str] = None,
                                max_items: Optional[float] = None,
                                verified: Optional[bool] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEmailRoutingAddressesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['direction'] = direction
    __args__['maxItems'] = max_items
    __args__['verified'] = verified
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getEmailRoutingAddresses:getEmailRoutingAddresses', __args__, opts=opts, typ=GetEmailRoutingAddressesResult, package_ref=_utilities.get_package()).value

    return AwaitableGetEmailRoutingAddressesResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        direction=pulumi.get(__ret__, 'direction'),
        id=pulumi.get(__ret__, 'id'),
        max_items=pulumi.get(__ret__, 'max_items'),
        results=pulumi.get(__ret__, 'results'),
        verified=pulumi.get(__ret__, 'verified'))
def get_email_routing_addresses_output(account_id: Optional[pulumi.Input[str]] = None,
                                       direction: Optional[pulumi.Input[Optional[str]]] = None,
                                       max_items: Optional[pulumi.Input[Optional[float]]] = None,
                                       verified: Optional[pulumi.Input[Optional[bool]]] = None,
                                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetEmailRoutingAddressesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['direction'] = direction
    __args__['maxItems'] = max_items
    __args__['verified'] = verified
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getEmailRoutingAddresses:getEmailRoutingAddresses', __args__, opts=opts, typ=GetEmailRoutingAddressesResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetEmailRoutingAddressesResult(
        account_id=pulumi.get(__response__, 'account_id'),
        direction=pulumi.get(__response__, 'direction'),
        id=pulumi.get(__response__, 'id'),
        max_items=pulumi.get(__response__, 'max_items'),
        results=pulumi.get(__response__, 'results'),
        verified=pulumi.get(__response__, 'verified')))
