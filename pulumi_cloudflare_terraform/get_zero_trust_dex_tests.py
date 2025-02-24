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
    'GetZeroTrustDexTestsResult',
    'AwaitableGetZeroTrustDexTestsResult',
    'get_zero_trust_dex_tests',
    'get_zero_trust_dex_tests_output',
]

@pulumi.output_type
class GetZeroTrustDexTestsResult:
    """
    A collection of values returned by getZeroTrustDexTests.
    """
    def __init__(__self__, account_id=None, id=None, max_items=None, results=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_items and not isinstance(max_items, float):
            raise TypeError("Expected argument 'max_items' to be a float")
        pulumi.set(__self__, "max_items", max_items)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

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
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[float]:
        return pulumi.get(self, "max_items")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetZeroTrustDexTestsResultResult']:
        return pulumi.get(self, "results")


class AwaitableGetZeroTrustDexTestsResult(GetZeroTrustDexTestsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetZeroTrustDexTestsResult(
            account_id=self.account_id,
            id=self.id,
            max_items=self.max_items,
            results=self.results)


def get_zero_trust_dex_tests(account_id: Optional[str] = None,
                             max_items: Optional[float] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetZeroTrustDexTestsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['maxItems'] = max_items
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getZeroTrustDexTests:getZeroTrustDexTests', __args__, opts=opts, typ=GetZeroTrustDexTestsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetZeroTrustDexTestsResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        id=pulumi.get(__ret__, 'id'),
        max_items=pulumi.get(__ret__, 'max_items'),
        results=pulumi.get(__ret__, 'results'))
def get_zero_trust_dex_tests_output(account_id: Optional[pulumi.Input[str]] = None,
                                    max_items: Optional[pulumi.Input[Optional[float]]] = None,
                                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetZeroTrustDexTestsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['maxItems'] = max_items
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getZeroTrustDexTests:getZeroTrustDexTests', __args__, opts=opts, typ=GetZeroTrustDexTestsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetZeroTrustDexTestsResult(
        account_id=pulumi.get(__response__, 'account_id'),
        id=pulumi.get(__response__, 'id'),
        max_items=pulumi.get(__response__, 'max_items'),
        results=pulumi.get(__response__, 'results')))
