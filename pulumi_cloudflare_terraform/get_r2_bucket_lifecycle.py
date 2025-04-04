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
    'GetR2BucketLifecycleResult',
    'AwaitableGetR2BucketLifecycleResult',
    'get_r2_bucket_lifecycle',
    'get_r2_bucket_lifecycle_output',
]

@pulumi.output_type
class GetR2BucketLifecycleResult:
    """
    A collection of values returned by getR2BucketLifecycle.
    """
    def __init__(__self__, account_id=None, bucket_name=None, id=None, rules=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.GetR2BucketLifecycleRuleResult']:
        return pulumi.get(self, "rules")


class AwaitableGetR2BucketLifecycleResult(GetR2BucketLifecycleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetR2BucketLifecycleResult(
            account_id=self.account_id,
            bucket_name=self.bucket_name,
            id=self.id,
            rules=self.rules)


def get_r2_bucket_lifecycle(account_id: Optional[str] = None,
                            bucket_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetR2BucketLifecycleResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['bucketName'] = bucket_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getR2BucketLifecycle:getR2BucketLifecycle', __args__, opts=opts, typ=GetR2BucketLifecycleResult, package_ref=_utilities.get_package()).value

    return AwaitableGetR2BucketLifecycleResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        bucket_name=pulumi.get(__ret__, 'bucket_name'),
        id=pulumi.get(__ret__, 'id'),
        rules=pulumi.get(__ret__, 'rules'))
def get_r2_bucket_lifecycle_output(account_id: Optional[pulumi.Input[str]] = None,
                                   bucket_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetR2BucketLifecycleResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['bucketName'] = bucket_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getR2BucketLifecycle:getR2BucketLifecycle', __args__, opts=opts, typ=GetR2BucketLifecycleResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetR2BucketLifecycleResult(
        account_id=pulumi.get(__response__, 'account_id'),
        bucket_name=pulumi.get(__response__, 'bucket_name'),
        id=pulumi.get(__response__, 'id'),
        rules=pulumi.get(__response__, 'rules')))
