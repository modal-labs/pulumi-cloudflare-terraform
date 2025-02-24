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
    'GetDcvDelegationResult',
    'AwaitableGetDcvDelegationResult',
    'get_dcv_delegation',
    'get_dcv_delegation_output',
]

@pulumi.output_type
class GetDcvDelegationResult:
    """
    A collection of values returned by getDcvDelegation.
    """
    def __init__(__self__, id=None, uuid=None, zone_id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetDcvDelegationResult(GetDcvDelegationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDcvDelegationResult(
            id=self.id,
            uuid=self.uuid,
            zone_id=self.zone_id)


def get_dcv_delegation(zone_id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDcvDelegationResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getDcvDelegation:getDcvDelegation', __args__, opts=opts, typ=GetDcvDelegationResult, package_ref=_utilities.get_package()).value

    return AwaitableGetDcvDelegationResult(
        id=pulumi.get(__ret__, 'id'),
        uuid=pulumi.get(__ret__, 'uuid'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_dcv_delegation_output(zone_id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDcvDelegationResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getDcvDelegation:getDcvDelegation', __args__, opts=opts, typ=GetDcvDelegationResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetDcvDelegationResult(
        id=pulumi.get(__response__, 'id'),
        uuid=pulumi.get(__response__, 'uuid'),
        zone_id=pulumi.get(__response__, 'zone_id')))
