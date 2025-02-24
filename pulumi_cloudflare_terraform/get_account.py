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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

@pulumi.output_type
class GetAccountResult:
    """
    A collection of values returned by getAccount.
    """
    def __init__(__self__, account_id=None, created_on=None, filter=None, id=None, name=None, settings=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if settings and not isinstance(settings, dict):
            raise TypeError("Expected argument 'settings' to be a dict")
        pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetAccountFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def settings(self) -> 'outputs.GetAccountSettingsResult':
        return pulumi.get(self, "settings")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_id=self.account_id,
            created_on=self.created_on,
            filter=self.filter,
            id=self.id,
            name=self.name,
            settings=self.settings)


def get_account(account_id: Optional[str] = None,
                filter: Optional[Union['GetAccountFilterArgs', 'GetAccountFilterArgsDict']] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult, package_ref=_utilities.get_package()).value

    return AwaitableGetAccountResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created_on=pulumi.get(__ret__, 'created_on'),
        filter=pulumi.get(__ret__, 'filter'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        settings=pulumi.get(__ret__, 'settings'))
def get_account_output(account_id: Optional[pulumi.Input[Optional[str]]] = None,
                       filter: Optional[pulumi.Input[Optional[Union['GetAccountFilterArgs', 'GetAccountFilterArgsDict']]]] = None,
                       opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAccountResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['filter'] = filter
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getAccount:getAccount', __args__, opts=opts, typ=GetAccountResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetAccountResult(
        account_id=pulumi.get(__response__, 'account_id'),
        created_on=pulumi.get(__response__, 'created_on'),
        filter=pulumi.get(__response__, 'filter'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        settings=pulumi.get(__response__, 'settings')))
