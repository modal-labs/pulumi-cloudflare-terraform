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
    'GetHyperdriveConfigResult',
    'AwaitableGetHyperdriveConfigResult',
    'get_hyperdrive_config',
    'get_hyperdrive_config_output',
]

@pulumi.output_type
class GetHyperdriveConfigResult:
    """
    A collection of values returned by getHyperdriveConfig.
    """
    def __init__(__self__, account_id=None, caching=None, created_on=None, hyperdrive_id=None, id=None, modified_on=None, name=None, origin=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if caching and not isinstance(caching, dict):
            raise TypeError("Expected argument 'caching' to be a dict")
        pulumi.set(__self__, "caching", caching)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if hyperdrive_id and not isinstance(hyperdrive_id, str):
            raise TypeError("Expected argument 'hyperdrive_id' to be a str")
        pulumi.set(__self__, "hyperdrive_id", hyperdrive_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modified_on and not isinstance(modified_on, str):
            raise TypeError("Expected argument 'modified_on' to be a str")
        pulumi.set(__self__, "modified_on", modified_on)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin and not isinstance(origin, dict):
            raise TypeError("Expected argument 'origin' to be a dict")
        pulumi.set(__self__, "origin", origin)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def caching(self) -> 'outputs.GetHyperdriveConfigCachingResult':
        return pulumi.get(self, "caching")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter(name="hyperdriveId")
    def hyperdrive_id(self) -> str:
        return pulumi.get(self, "hyperdrive_id")

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
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origin(self) -> 'outputs.GetHyperdriveConfigOriginResult':
        return pulumi.get(self, "origin")


class AwaitableGetHyperdriveConfigResult(GetHyperdriveConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHyperdriveConfigResult(
            account_id=self.account_id,
            caching=self.caching,
            created_on=self.created_on,
            hyperdrive_id=self.hyperdrive_id,
            id=self.id,
            modified_on=self.modified_on,
            name=self.name,
            origin=self.origin)


def get_hyperdrive_config(account_id: Optional[str] = None,
                          hyperdrive_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHyperdriveConfigResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['hyperdriveId'] = hyperdrive_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getHyperdriveConfig:getHyperdriveConfig', __args__, opts=opts, typ=GetHyperdriveConfigResult, package_ref=_utilities.get_package()).value

    return AwaitableGetHyperdriveConfigResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        caching=pulumi.get(__ret__, 'caching'),
        created_on=pulumi.get(__ret__, 'created_on'),
        hyperdrive_id=pulumi.get(__ret__, 'hyperdrive_id'),
        id=pulumi.get(__ret__, 'id'),
        modified_on=pulumi.get(__ret__, 'modified_on'),
        name=pulumi.get(__ret__, 'name'),
        origin=pulumi.get(__ret__, 'origin'))
def get_hyperdrive_config_output(account_id: Optional[pulumi.Input[str]] = None,
                                 hyperdrive_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetHyperdriveConfigResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['hyperdriveId'] = hyperdrive_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getHyperdriveConfig:getHyperdriveConfig', __args__, opts=opts, typ=GetHyperdriveConfigResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetHyperdriveConfigResult(
        account_id=pulumi.get(__response__, 'account_id'),
        caching=pulumi.get(__response__, 'caching'),
        created_on=pulumi.get(__response__, 'created_on'),
        hyperdrive_id=pulumi.get(__response__, 'hyperdrive_id'),
        id=pulumi.get(__response__, 'id'),
        modified_on=pulumi.get(__response__, 'modified_on'),
        name=pulumi.get(__response__, 'name'),
        origin=pulumi.get(__response__, 'origin')))
