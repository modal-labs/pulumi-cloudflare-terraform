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
    'GetR2BucketResult',
    'AwaitableGetR2BucketResult',
    'get_r2_bucket',
    'get_r2_bucket_output',
]

@pulumi.output_type
class GetR2BucketResult:
    """
    A collection of values returned by getR2Bucket.
    """
    def __init__(__self__, account_id=None, bucket_name=None, creation_date=None, id=None, location=None, name=None, storage_class=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if bucket_name and not isinstance(bucket_name, str):
            raise TypeError("Expected argument 'bucket_name' to be a str")
        pulumi.set(__self__, "bucket_name", bucket_name)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_class and not isinstance(storage_class, str):
            raise TypeError("Expected argument 'storage_class' to be a str")
        pulumi.set(__self__, "storage_class", storage_class)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> str:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        return pulumi.get(self, "storage_class")


class AwaitableGetR2BucketResult(GetR2BucketResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetR2BucketResult(
            account_id=self.account_id,
            bucket_name=self.bucket_name,
            creation_date=self.creation_date,
            id=self.id,
            location=self.location,
            name=self.name,
            storage_class=self.storage_class)


def get_r2_bucket(account_id: Optional[str] = None,
                  bucket_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetR2BucketResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['bucketName'] = bucket_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getR2Bucket:getR2Bucket', __args__, opts=opts, typ=GetR2BucketResult, package_ref=_utilities.get_package()).value

    return AwaitableGetR2BucketResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        bucket_name=pulumi.get(__ret__, 'bucket_name'),
        creation_date=pulumi.get(__ret__, 'creation_date'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        storage_class=pulumi.get(__ret__, 'storage_class'))
def get_r2_bucket_output(account_id: Optional[pulumi.Input[str]] = None,
                         bucket_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetR2BucketResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['bucketName'] = bucket_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getR2Bucket:getR2Bucket', __args__, opts=opts, typ=GetR2BucketResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetR2BucketResult(
        account_id=pulumi.get(__response__, 'account_id'),
        bucket_name=pulumi.get(__response__, 'bucket_name'),
        creation_date=pulumi.get(__response__, 'creation_date'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        storage_class=pulumi.get(__response__, 'storage_class')))
