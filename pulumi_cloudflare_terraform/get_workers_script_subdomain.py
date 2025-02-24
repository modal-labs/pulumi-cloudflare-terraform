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
    'GetWorkersScriptSubdomainResult',
    'AwaitableGetWorkersScriptSubdomainResult',
    'get_workers_script_subdomain',
    'get_workers_script_subdomain_output',
]

@pulumi.output_type
class GetWorkersScriptSubdomainResult:
    """
    A collection of values returned by getWorkersScriptSubdomain.
    """
    def __init__(__self__, account_id=None, enabled=None, id=None, previews_enabled=None, script_name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if previews_enabled and not isinstance(previews_enabled, bool):
            raise TypeError("Expected argument 'previews_enabled' to be a bool")
        pulumi.set(__self__, "previews_enabled", previews_enabled)
        if script_name and not isinstance(script_name, str):
            raise TypeError("Expected argument 'script_name' to be a str")
        pulumi.set(__self__, "script_name", script_name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="previewsEnabled")
    def previews_enabled(self) -> bool:
        return pulumi.get(self, "previews_enabled")

    @property
    @pulumi.getter(name="scriptName")
    def script_name(self) -> str:
        return pulumi.get(self, "script_name")


class AwaitableGetWorkersScriptSubdomainResult(GetWorkersScriptSubdomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkersScriptSubdomainResult(
            account_id=self.account_id,
            enabled=self.enabled,
            id=self.id,
            previews_enabled=self.previews_enabled,
            script_name=self.script_name)


def get_workers_script_subdomain(account_id: Optional[str] = None,
                                 script_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkersScriptSubdomainResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getWorkersScriptSubdomain:getWorkersScriptSubdomain', __args__, opts=opts, typ=GetWorkersScriptSubdomainResult, package_ref=_utilities.get_package()).value

    return AwaitableGetWorkersScriptSubdomainResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        previews_enabled=pulumi.get(__ret__, 'previews_enabled'),
        script_name=pulumi.get(__ret__, 'script_name'))
def get_workers_script_subdomain_output(account_id: Optional[pulumi.Input[str]] = None,
                                        script_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWorkersScriptSubdomainResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getWorkersScriptSubdomain:getWorkersScriptSubdomain', __args__, opts=opts, typ=GetWorkersScriptSubdomainResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetWorkersScriptSubdomainResult(
        account_id=pulumi.get(__response__, 'account_id'),
        enabled=pulumi.get(__response__, 'enabled'),
        id=pulumi.get(__response__, 'id'),
        previews_enabled=pulumi.get(__response__, 'previews_enabled'),
        script_name=pulumi.get(__response__, 'script_name')))
