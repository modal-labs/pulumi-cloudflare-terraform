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
    'GetEmailRoutingSettingsResult',
    'AwaitableGetEmailRoutingSettingsResult',
    'get_email_routing_settings',
    'get_email_routing_settings_output',
]

@pulumi.output_type
class GetEmailRoutingSettingsResult:
    """
    A collection of values returned by getEmailRoutingSettings.
    """
    def __init__(__self__, created=None, enabled=None, id=None, modified=None, name=None, skip_wizard=None, status=None, tag=None, zone_id=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modified and not isinstance(modified, str):
            raise TypeError("Expected argument 'modified' to be a str")
        pulumi.set(__self__, "modified", modified)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if skip_wizard and not isinstance(skip_wizard, bool):
            raise TypeError("Expected argument 'skip_wizard' to be a bool")
        pulumi.set(__self__, "skip_wizard", skip_wizard)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tag and not isinstance(tag, str):
            raise TypeError("Expected argument 'tag' to be a str")
        pulumi.set(__self__, "tag", tag)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def created(self) -> str:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def modified(self) -> str:
        return pulumi.get(self, "modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="skipWizard")
    def skip_wizard(self) -> bool:
        return pulumi.get(self, "skip_wizard")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tag(self) -> str:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetEmailRoutingSettingsResult(GetEmailRoutingSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEmailRoutingSettingsResult(
            created=self.created,
            enabled=self.enabled,
            id=self.id,
            modified=self.modified,
            name=self.name,
            skip_wizard=self.skip_wizard,
            status=self.status,
            tag=self.tag,
            zone_id=self.zone_id)


def get_email_routing_settings(zone_id: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEmailRoutingSettingsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getEmailRoutingSettings:getEmailRoutingSettings', __args__, opts=opts, typ=GetEmailRoutingSettingsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetEmailRoutingSettingsResult(
        created=pulumi.get(__ret__, 'created'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        modified=pulumi.get(__ret__, 'modified'),
        name=pulumi.get(__ret__, 'name'),
        skip_wizard=pulumi.get(__ret__, 'skip_wizard'),
        status=pulumi.get(__ret__, 'status'),
        tag=pulumi.get(__ret__, 'tag'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_email_routing_settings_output(zone_id: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetEmailRoutingSettingsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getEmailRoutingSettings:getEmailRoutingSettings', __args__, opts=opts, typ=GetEmailRoutingSettingsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetEmailRoutingSettingsResult(
        created=pulumi.get(__response__, 'created'),
        enabled=pulumi.get(__response__, 'enabled'),
        id=pulumi.get(__response__, 'id'),
        modified=pulumi.get(__response__, 'modified'),
        name=pulumi.get(__response__, 'name'),
        skip_wizard=pulumi.get(__response__, 'skip_wizard'),
        status=pulumi.get(__response__, 'status'),
        tag=pulumi.get(__response__, 'tag'),
        zone_id=pulumi.get(__response__, 'zone_id')))
