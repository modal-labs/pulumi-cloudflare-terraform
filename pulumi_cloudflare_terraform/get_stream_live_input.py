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
    'GetStreamLiveInputResult',
    'AwaitableGetStreamLiveInputResult',
    'get_stream_live_input',
    'get_stream_live_input_output',
]

@pulumi.output_type
class GetStreamLiveInputResult:
    """
    A collection of values returned by getStreamLiveInput.
    """
    def __init__(__self__, account_id=None, created=None, delete_recording_after_days=None, id=None, live_input_identifier=None, meta=None, modified=None, recording=None, rtmps=None, rtmps_playback=None, srt=None, srt_playback=None, status=None, uid=None, web_rtc=None, web_rtc_playback=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if delete_recording_after_days and not isinstance(delete_recording_after_days, float):
            raise TypeError("Expected argument 'delete_recording_after_days' to be a float")
        pulumi.set(__self__, "delete_recording_after_days", delete_recording_after_days)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if live_input_identifier and not isinstance(live_input_identifier, str):
            raise TypeError("Expected argument 'live_input_identifier' to be a str")
        pulumi.set(__self__, "live_input_identifier", live_input_identifier)
        if meta and not isinstance(meta, str):
            raise TypeError("Expected argument 'meta' to be a str")
        pulumi.set(__self__, "meta", meta)
        if modified and not isinstance(modified, str):
            raise TypeError("Expected argument 'modified' to be a str")
        pulumi.set(__self__, "modified", modified)
        if recording and not isinstance(recording, dict):
            raise TypeError("Expected argument 'recording' to be a dict")
        pulumi.set(__self__, "recording", recording)
        if rtmps and not isinstance(rtmps, dict):
            raise TypeError("Expected argument 'rtmps' to be a dict")
        pulumi.set(__self__, "rtmps", rtmps)
        if rtmps_playback and not isinstance(rtmps_playback, dict):
            raise TypeError("Expected argument 'rtmps_playback' to be a dict")
        pulumi.set(__self__, "rtmps_playback", rtmps_playback)
        if srt and not isinstance(srt, dict):
            raise TypeError("Expected argument 'srt' to be a dict")
        pulumi.set(__self__, "srt", srt)
        if srt_playback and not isinstance(srt_playback, dict):
            raise TypeError("Expected argument 'srt_playback' to be a dict")
        pulumi.set(__self__, "srt_playback", srt_playback)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if uid and not isinstance(uid, str):
            raise TypeError("Expected argument 'uid' to be a str")
        pulumi.set(__self__, "uid", uid)
        if web_rtc and not isinstance(web_rtc, dict):
            raise TypeError("Expected argument 'web_rtc' to be a dict")
        pulumi.set(__self__, "web_rtc", web_rtc)
        if web_rtc_playback and not isinstance(web_rtc_playback, dict):
            raise TypeError("Expected argument 'web_rtc_playback' to be a dict")
        pulumi.set(__self__, "web_rtc_playback", web_rtc_playback)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def created(self) -> str:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="deleteRecordingAfterDays")
    def delete_recording_after_days(self) -> float:
        return pulumi.get(self, "delete_recording_after_days")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="liveInputIdentifier")
    def live_input_identifier(self) -> str:
        return pulumi.get(self, "live_input_identifier")

    @property
    @pulumi.getter
    def meta(self) -> str:
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter
    def modified(self) -> str:
        return pulumi.get(self, "modified")

    @property
    @pulumi.getter
    def recording(self) -> 'outputs.GetStreamLiveInputRecordingResult':
        return pulumi.get(self, "recording")

    @property
    @pulumi.getter
    def rtmps(self) -> 'outputs.GetStreamLiveInputRtmpsResult':
        return pulumi.get(self, "rtmps")

    @property
    @pulumi.getter(name="rtmpsPlayback")
    def rtmps_playback(self) -> 'outputs.GetStreamLiveInputRtmpsPlaybackResult':
        return pulumi.get(self, "rtmps_playback")

    @property
    @pulumi.getter
    def srt(self) -> 'outputs.GetStreamLiveInputSrtResult':
        return pulumi.get(self, "srt")

    @property
    @pulumi.getter(name="srtPlayback")
    def srt_playback(self) -> 'outputs.GetStreamLiveInputSrtPlaybackResult':
        return pulumi.get(self, "srt_playback")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def uid(self) -> str:
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="webRtc")
    def web_rtc(self) -> 'outputs.GetStreamLiveInputWebRtcResult':
        return pulumi.get(self, "web_rtc")

    @property
    @pulumi.getter(name="webRtcPlayback")
    def web_rtc_playback(self) -> 'outputs.GetStreamLiveInputWebRtcPlaybackResult':
        return pulumi.get(self, "web_rtc_playback")


class AwaitableGetStreamLiveInputResult(GetStreamLiveInputResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStreamLiveInputResult(
            account_id=self.account_id,
            created=self.created,
            delete_recording_after_days=self.delete_recording_after_days,
            id=self.id,
            live_input_identifier=self.live_input_identifier,
            meta=self.meta,
            modified=self.modified,
            recording=self.recording,
            rtmps=self.rtmps,
            rtmps_playback=self.rtmps_playback,
            srt=self.srt,
            srt_playback=self.srt_playback,
            status=self.status,
            uid=self.uid,
            web_rtc=self.web_rtc,
            web_rtc_playback=self.web_rtc_playback)


def get_stream_live_input(account_id: Optional[str] = None,
                          live_input_identifier: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStreamLiveInputResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['liveInputIdentifier'] = live_input_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getStreamLiveInput:getStreamLiveInput', __args__, opts=opts, typ=GetStreamLiveInputResult, package_ref=_utilities.get_package()).value

    return AwaitableGetStreamLiveInputResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        created=pulumi.get(__ret__, 'created'),
        delete_recording_after_days=pulumi.get(__ret__, 'delete_recording_after_days'),
        id=pulumi.get(__ret__, 'id'),
        live_input_identifier=pulumi.get(__ret__, 'live_input_identifier'),
        meta=pulumi.get(__ret__, 'meta'),
        modified=pulumi.get(__ret__, 'modified'),
        recording=pulumi.get(__ret__, 'recording'),
        rtmps=pulumi.get(__ret__, 'rtmps'),
        rtmps_playback=pulumi.get(__ret__, 'rtmps_playback'),
        srt=pulumi.get(__ret__, 'srt'),
        srt_playback=pulumi.get(__ret__, 'srt_playback'),
        status=pulumi.get(__ret__, 'status'),
        uid=pulumi.get(__ret__, 'uid'),
        web_rtc=pulumi.get(__ret__, 'web_rtc'),
        web_rtc_playback=pulumi.get(__ret__, 'web_rtc_playback'))
def get_stream_live_input_output(account_id: Optional[pulumi.Input[str]] = None,
                                 live_input_identifier: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetStreamLiveInputResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['liveInputIdentifier'] = live_input_identifier
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getStreamLiveInput:getStreamLiveInput', __args__, opts=opts, typ=GetStreamLiveInputResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetStreamLiveInputResult(
        account_id=pulumi.get(__response__, 'account_id'),
        created=pulumi.get(__response__, 'created'),
        delete_recording_after_days=pulumi.get(__response__, 'delete_recording_after_days'),
        id=pulumi.get(__response__, 'id'),
        live_input_identifier=pulumi.get(__response__, 'live_input_identifier'),
        meta=pulumi.get(__response__, 'meta'),
        modified=pulumi.get(__response__, 'modified'),
        recording=pulumi.get(__response__, 'recording'),
        rtmps=pulumi.get(__response__, 'rtmps'),
        rtmps_playback=pulumi.get(__response__, 'rtmps_playback'),
        srt=pulumi.get(__response__, 'srt'),
        srt_playback=pulumi.get(__response__, 'srt_playback'),
        status=pulumi.get(__response__, 'status'),
        uid=pulumi.get(__response__, 'uid'),
        web_rtc=pulumi.get(__response__, 'web_rtc'),
        web_rtc_playback=pulumi.get(__response__, 'web_rtc_playback')))
