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
    'GetWorkersCronTriggerResult',
    'AwaitableGetWorkersCronTriggerResult',
    'get_workers_cron_trigger',
    'get_workers_cron_trigger_output',
]

@pulumi.output_type
class GetWorkersCronTriggerResult:
    """
    A collection of values returned by getWorkersCronTrigger.
    """
    def __init__(__self__, account_id=None, id=None, schedules=None, script_name=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if schedules and not isinstance(schedules, list):
            raise TypeError("Expected argument 'schedules' to be a list")
        pulumi.set(__self__, "schedules", schedules)
        if script_name and not isinstance(script_name, str):
            raise TypeError("Expected argument 'script_name' to be a str")
        pulumi.set(__self__, "script_name", script_name)

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
    @pulumi.getter
    def schedules(self) -> Sequence['outputs.GetWorkersCronTriggerScheduleResult']:
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter(name="scriptName")
    def script_name(self) -> str:
        return pulumi.get(self, "script_name")


class AwaitableGetWorkersCronTriggerResult(GetWorkersCronTriggerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkersCronTriggerResult(
            account_id=self.account_id,
            id=self.id,
            schedules=self.schedules,
            script_name=self.script_name)


def get_workers_cron_trigger(account_id: Optional[str] = None,
                             script_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkersCronTriggerResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getWorkersCronTrigger:getWorkersCronTrigger', __args__, opts=opts, typ=GetWorkersCronTriggerResult, package_ref=_utilities.get_package()).value

    return AwaitableGetWorkersCronTriggerResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        id=pulumi.get(__ret__, 'id'),
        schedules=pulumi.get(__ret__, 'schedules'),
        script_name=pulumi.get(__ret__, 'script_name'))
def get_workers_cron_trigger_output(account_id: Optional[pulumi.Input[str]] = None,
                                    script_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetWorkersCronTriggerResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['accountId'] = account_id
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getWorkersCronTrigger:getWorkersCronTrigger', __args__, opts=opts, typ=GetWorkersCronTriggerResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetWorkersCronTriggerResult(
        account_id=pulumi.get(__response__, 'account_id'),
        id=pulumi.get(__response__, 'id'),
        schedules=pulumi.get(__response__, 'schedules'),
        script_name=pulumi.get(__response__, 'script_name')))
