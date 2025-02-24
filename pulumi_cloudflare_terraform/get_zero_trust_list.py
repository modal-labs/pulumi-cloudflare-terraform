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
    'GetZeroTrustListResult',
    'AwaitableGetZeroTrustListResult',
    'get_zero_trust_list',
    'get_zero_trust_list_output',
]

@pulumi.output_type
class GetZeroTrustListResult:
    """
    A collection of values returned by getZeroTrustList.
    """
    def __init__(__self__, account_id=None, created_at=None, description=None, filter=None, id=None, list_count=None, list_id=None, name=None, type=None, updated_at=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if list_count and not isinstance(list_count, float):
            raise TypeError("Expected argument 'list_count' to be a float")
        pulumi.set(__self__, "list_count", list_count)
        if list_id and not isinstance(list_id, str):
            raise TypeError("Expected argument 'list_id' to be a str")
        pulumi.set(__self__, "list_id", list_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetZeroTrustListFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listCount")
    def list_count(self) -> float:
        return pulumi.get(self, "list_count")

    @property
    @pulumi.getter(name="listId")
    def list_id(self) -> Optional[str]:
        return pulumi.get(self, "list_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")


class AwaitableGetZeroTrustListResult(GetZeroTrustListResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZeroTrustListResult(
            account_id=self.account_id,
            created_at=self.created_at,
            description=self.description,
            filter=self.filter,
            id=self.id,
            list_count=self.list_count,
            list_id=self.list_id,
            name=self.name,
            type=self.type,
            updated_at=self.updated_at)


def get_zero_trust_list(account_id: Optional[str] = None,
                        filter: Optional[Union['GetZeroTrustListFilterArgs', 'GetZeroTrustListFilterArgsDict']] = None,
                        list_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZeroTrustListResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['listId'] = list_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZeroTrustList:getZeroTrustList', __args__, opts=opts, typ=GetZeroTrustListResult, package_ref=_utilities.get_package()).value

    return AwaitableGetZeroTrustListResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created_at=pulumi.get(__ret__, 'created_at'),
        description=pulumi.get(__ret__, 'description'),
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        list_count=pulumi.get(__ret__, 'list_count'),
        list_id=pulumi.get(__ret__, 'list_id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'),
        updated_at=pulumi.get(__ret__, 'updated_at'))
def get_zero_trust_list_output(account_id: Optional[pulumi.Input[str]] = None,
                               filter: Optional[pulumi.Input[Optional[Union['GetZeroTrustListFilterArgs', 'GetZeroTrustListFilterArgsDict']]]] = None,
                               list_id: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZeroTrustListResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    __args__['listId'] = list_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getZeroTrustList:getZeroTrustList', __args__, opts=opts, typ=GetZeroTrustListResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetZeroTrustListResult(
        account_id=pulumi.get(__response__, 'account_id'),
        created_at=pulumi.get(__response__, 'created_at'),
        description=pulumi.get(__response__, 'description'),
        filter=pulumi.get(__response__, 'filter'),
        id=pulumi.get(__response__, 'id'),
        list_count=pulumi.get(__response__, 'list_count'),
        list_id=pulumi.get(__response__, 'list_id'),
        name=pulumi.get(__response__, 'name'),
        type=pulumi.get(__response__, 'type'),
        updated_at=pulumi.get(__response__, 'updated_at')))
