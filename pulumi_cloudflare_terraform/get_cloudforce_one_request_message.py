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
    'GetCloudforceOneRequestMessageResult',
    'AwaitableGetCloudforceOneRequestMessageResult',
    'get_cloudforce_one_request_message',
    'get_cloudforce_one_request_message_output',
]

@pulumi.output_type
class GetCloudforceOneRequestMessageResult:
    """
    A collection of values returned by getCloudforceOneRequestMessage.
    """
    def __init__(__self__, account_identifier=None, author=None, content=None, created=None, id=None, is_follow_on_request=None, request_identifier=None, updated=None):
        if account_identifier and not isinstance(account_identifier, str):
            raise TypeError("Expected argument 'account_identifier' to be a str")
        pulumi.set(__self__, "account_identifier", account_identifier)
        if author and not isinstance(author, str):
            raise TypeError("Expected argument 'author' to be a str")
        pulumi.set(__self__, "author", author)
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        pulumi.set(__self__, "id", id)
        if is_follow_on_request and not isinstance(is_follow_on_request, bool):
            raise TypeError("Expected argument 'is_follow_on_request' to be a bool")
        pulumi.set(__self__, "is_follow_on_request", is_follow_on_request)
        if request_identifier and not isinstance(request_identifier, str):
            raise TypeError("Expected argument 'request_identifier' to be a str")
        pulumi.set(__self__, "request_identifier", request_identifier)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter(name="accountIdentifier")
    def account_identifier(self) -> str:
        return pulumi.get(self, "account_identifier")

    @property
    @pulumi.getter
    def author(self) -> str:
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def content(self) -> str:
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def created(self) -> str:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def id(self) -> float:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isFollowOnRequest")
    def is_follow_on_request(self) -> bool:
        return pulumi.get(self, "is_follow_on_request")

    @property
    @pulumi.getter(name="requestIdentifier")
    def request_identifier(self) -> str:
        return pulumi.get(self, "request_identifier")

    @property
    @pulumi.getter
    def updated(self) -> str:
        return pulumi.get(self, "updated")


class AwaitableGetCloudforceOneRequestMessageResult(GetCloudforceOneRequestMessageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudforceOneRequestMessageResult(
            account_identifier=self.account_identifier,
            author=self.author,
            content=self.content,
            created=self.created,
            id=self.id,
            is_follow_on_request=self.is_follow_on_request,
            request_identifier=self.request_identifier,
            updated=self.updated)


def get_cloudforce_one_request_message(account_identifier: Optional[str] = None,
                                       request_identifier: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudforceOneRequestMessageResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountIdentifier'] = account_identifier
    __args__['requestIdentifier'] = request_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getCloudforceOneRequestMessage:getCloudforceOneRequestMessage', __args__, opts=opts, typ=GetCloudforceOneRequestMessageResult, package_ref=_utilities.get_package()).value

    return AwaitableGetCloudforceOneRequestMessageResult(
        account_identifier=pulumi.get(__ret__, 'account_identifier'),
        author=pulumi.get(__ret__, 'author'),
        content=pulumi.get(__ret__, 'content'),
        created=pulumi.get(__ret__, 'created'),
        id=pulumi.get(__ret__, 'id'),
        is_follow_on_request=pulumi.get(__ret__, 'is_follow_on_request'),
        request_identifier=pulumi.get(__ret__, 'request_identifier'),
        updated=pulumi.get(__ret__, 'updated'))
def get_cloudforce_one_request_message_output(account_identifier: Optional[pulumi.Input[str]] = None,
                                              request_identifier: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetCloudforceOneRequestMessageResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountIdentifier'] = account_identifier
    __args__['requestIdentifier'] = request_identifier
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getCloudforceOneRequestMessage:getCloudforceOneRequestMessage', __args__, opts=opts, typ=GetCloudforceOneRequestMessageResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetCloudforceOneRequestMessageResult(
        account_identifier=pulumi.get(__response__, 'account_identifier'),
        author=pulumi.get(__response__, 'author'),
        content=pulumi.get(__response__, 'content'),
        created=pulumi.get(__response__, 'created'),
        id=pulumi.get(__response__, 'id'),
        is_follow_on_request=pulumi.get(__response__, 'is_follow_on_request'),
        request_identifier=pulumi.get(__response__, 'request_identifier'),
        updated=pulumi.get(__response__, 'updated')))
