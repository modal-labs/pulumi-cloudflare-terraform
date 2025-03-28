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
    'GetListItemsResult',
    'AwaitableGetListItemsResult',
    'get_list_items',
    'get_list_items_output',
]

@pulumi.output_type
class GetListItemsResult:
    """
    A collection of values returned by getListItems.
    """
    def __init__(__self__, account_id=None, id=None, list_id=None, max_items=None, results=None, search=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if list_id and not isinstance(list_id, str):
            raise TypeError("Expected argument 'list_id' to be a str")
        pulumi.set(__self__, "list_id", list_id)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)
        if search and not isinstance(search, str):
            raise TypeError("Expected argument 'search' to be a str")
        pulumi.set(__self__, "search", search)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listId")
    def list_id(self) -> str:
        return pulumi.get(self, "list_id")

    @property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[float]:
        return pulumi.get(self, "max_items")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetListItemsResultResult']:
        return pulumi.get(self, "results")

    @property
    @pulumi.getter
    def search(self) -> Optional[str]:
        return pulumi.get(self, "search")


class AwaitableGetListItemsResult(GetListItemsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListItemsResult(
            account_id=self.account_id,
            id=self.id,
            list_id=self.list_id,
            max_items=self.max_items,
            results=self.results,
            search=self.search)


def get_list_items(account_id: Optional[str] = None,
                   list_id: Optional[str] = None,
                   max_items: Optional[float] = None,
                   search: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListItemsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['listId'] = list_id
    __args__['maxItems'] = max_items
    __args__['search'] = search
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getListItems:getListItems', __args__, opts=opts, typ=GetListItemsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetListItemsResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        id=pulumi.get(__ret__, 'id'),
        list_id=pulumi.get(__ret__, 'list_id'),
        max_items=pulumi.get(__ret__, 'max_items'),
        results=pulumi.get(__ret__, 'results'),
        search=pulumi.get(__ret__, 'search'))
def get_list_items_output(account_id: Optional[pulumi.Input[str]] = None,
                          list_id: Optional[pulumi.Input[str]] = None,
                          max_items: Optional[pulumi.Input[Optional[float]]] = None,
                          search: Optional[pulumi.Input[Optional[str]]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetListItemsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['listId'] = list_id
    __args__['maxItems'] = max_items
    __args__['search'] = search
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getListItems:getListItems', __args__, opts=opts, typ=GetListItemsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetListItemsResult(
        account_id=pulumi.get(__response__, 'account_id'),
        id=pulumi.get(__response__, 'id'),
        list_id=pulumi.get(__response__, 'list_id'),
        max_items=pulumi.get(__response__, 'max_items'),
        results=pulumi.get(__response__, 'results'),
        search=pulumi.get(__response__, 'search')))
