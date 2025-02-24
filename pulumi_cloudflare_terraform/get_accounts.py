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
    'GetAccountsResult',
    'AwaitableGetAccountsResult',
    'get_accounts',
    'get_accounts_output',
]

@pulumi.output_type
class GetAccountsResult:
    """
    A collection of values returned by getAccounts.
    """
    def __init__(__self__, direction=None, id=None, max_items=None, name=None, results=None):
        if direction and not isinstance(direction, str):
            raise TypeError("Expected argument 'direction' to be a str")
        pulumi.set(__self__, "direction", direction)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
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
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetAccountsResultResult']:
        return pulumi.get(self, "results")


class AwaitableGetAccountsResult(GetAccountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountsResult(
            direction=self.direction,
            id=self.id,
            max_items=self.max_items,
            name=self.name,
            results=self.results)


def get_accounts(direction: Optional[str] = None,
                 max_items: Optional[float] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['direction'] = direction
    __args__['maxItems'] = max_items
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAccounts:getAccounts', __args__, opts=opts, typ=GetAccountsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetAccountsResult(
        direction=pulumi.get(__ret__, 'direction'),
        id=pulumi.get(__ret__, 'id'),
        max_items=pulumi.get(__ret__, 'max_items'),
        name=pulumi.get(__ret__, 'name'),
        results=pulumi.get(__ret__, 'results'))
def get_accounts_output(direction: Optional[pulumi.Input[Optional[str]]] = None,
                        max_items: Optional[pulumi.Input[Optional[float]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccountsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['direction'] = direction
    __args__['maxItems'] = max_items
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getAccounts:getAccounts', __args__, opts=opts, typ=GetAccountsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetAccountsResult(
        direction=pulumi.get(__response__, 'direction'),
        id=pulumi.get(__response__, 'id'),
        max_items=pulumi.get(__response__, 'max_items'),
        name=pulumi.get(__response__, 'name'),
        results=pulumi.get(__response__, 'results')))
