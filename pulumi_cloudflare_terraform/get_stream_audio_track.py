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
    'GetStreamAudioTrackResult',
    'AwaitableGetStreamAudioTrackResult',
    'get_stream_audio_track',
    'get_stream_audio_track_output',
]

@pulumi.output_type
class GetStreamAudioTrackResult:
    """
    A collection of values returned by getStreamAudioTrack.
    """
    def __init__(__self__, account_id=None, default=None, id=None, identifier=None, label=None, status=None, uid=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if default and not isinstance(default, bool):
            raise TypeError("Expected argument 'default' to be a bool")
        pulumi.set(__self__, "default", default)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifier and not isinstance(identifier, str):
            raise TypeError("Expected argument 'identifier' to be a str")
        pulumi.set(__self__, "identifier", identifier)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def default(self) -> bool:
        return pulumi.get(self, "default")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identifier(self) -> str:
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def uid(self) -> str:
        return pulumi.get(self, "uid")


class AwaitableGetStreamAudioTrackResult(GetStreamAudioTrackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamAudioTrackResult(
            account_id=self.account_id,
            default=self.default,
            id=self.id,
            identifier=self.identifier,
            label=self.label,
            status=self.status,
            uid=self.uid)


def get_stream_audio_track(account_id: Optional[str] = None,
                           identifier: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamAudioTrackResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['identifier'] = identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getStreamAudioTrack:getStreamAudioTrack', __args__, opts=opts, typ=GetStreamAudioTrackResult, package_ref=_utilities.get_package()).value

    return AwaitableGetStreamAudioTrackResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        default=pulumi.get(__ret__, 'default'),
        id=pulumi.get(__ret__, 'id'),
        identifier=pulumi.get(__ret__, 'identifier'),
        label=pulumi.get(__ret__, 'label'),
        status=pulumi.get(__ret__, 'status'),
        uid=pulumi.get(__ret__, 'uid'))
def get_stream_audio_track_output(account_id: Optional[pulumi.Input[str]] = None,
                                  identifier: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetStreamAudioTrackResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['identifier'] = identifier
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getStreamAudioTrack:getStreamAudioTrack', __args__, opts=opts, typ=GetStreamAudioTrackResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetStreamAudioTrackResult(
        account_id=pulumi.get(__response__, 'account_id'),
        default=pulumi.get(__response__, 'default'),
        id=pulumi.get(__response__, 'id'),
        identifier=pulumi.get(__response__, 'identifier'),
        label=pulumi.get(__response__, 'label'),
        status=pulumi.get(__response__, 'status'),
        uid=pulumi.get(__response__, 'uid')))
