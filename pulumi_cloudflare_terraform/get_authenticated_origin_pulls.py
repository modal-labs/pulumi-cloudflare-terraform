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
    'GetAuthenticatedOriginPullsResult',
    'AwaitableGetAuthenticatedOriginPullsResult',
    'get_authenticated_origin_pulls',
    'get_authenticated_origin_pulls_output',
]

@pulumi.output_type
class GetAuthenticatedOriginPullsResult:
    """
    A collection of values returned by getAuthenticatedOriginPulls.
    """
    def __init__(__self__, cert_id=None, cert_status=None, cert_updated_at=None, cert_uploaded_on=None, certificate=None, created_at=None, enabled=None, expires_on=None, hostname=None, id=None, issuer=None, serial_number=None, signature=None, status=None, updated_at=None, zone_id=None):
        if cert_id and not isinstance(cert_id, str):
            raise TypeError("Expected argument 'cert_id' to be a str")
        pulumi.set(__self__, "cert_id", cert_id)
        if cert_status and not isinstance(cert_status, str):
            raise TypeError("Expected argument 'cert_status' to be a str")
        pulumi.set(__self__, "cert_status", cert_status)
        if cert_updated_at and not isinstance(cert_updated_at, str):
            raise TypeError("Expected argument 'cert_updated_at' to be a str")
        pulumi.set(__self__, "cert_updated_at", cert_updated_at)
        if cert_uploaded_on and not isinstance(cert_uploaded_on, str):
            raise TypeError("Expected argument 'cert_uploaded_on' to be a str")
        pulumi.set(__self__, "cert_uploaded_on", cert_uploaded_on)
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if expires_on and not isinstance(expires_on, str):
            raise TypeError("Expected argument 'expires_on' to be a str")
        pulumi.set(__self__, "expires_on", expires_on)
        if hostname and not isinstance(hostname, str):
            raise TypeError("Expected argument 'hostname' to be a str")
        pulumi.set(__self__, "hostname", hostname)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issuer and not isinstance(issuer, str):
            raise TypeError("Expected argument 'issuer' to be a str")
        pulumi.set(__self__, "issuer", issuer)
        if serial_number and not isinstance(serial_number, str):
            raise TypeError("Expected argument 'serial_number' to be a str")
        pulumi.set(__self__, "serial_number", serial_number)
        if signature and not isinstance(signature, str):
            raise TypeError("Expected argument 'signature' to be a str")
        pulumi.set(__self__, "signature", signature)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="certId")
    def cert_id(self) -> str:
        return pulumi.get(self, "cert_id")

    @property
    @pulumi.getter(name="certStatus")
    def cert_status(self) -> str:
        return pulumi.get(self, "cert_status")

    @property
    @pulumi.getter(name="certUpdatedAt")
    def cert_updated_at(self) -> str:
        return pulumi.get(self, "cert_updated_at")

    @property
    @pulumi.getter(name="certUploadedOn")
    def cert_uploaded_on(self) -> str:
        return pulumi.get(self, "cert_uploaded_on")

    @property
    @pulumi.getter
    def certificate(self) -> str:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> str:
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> str:
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter
    def signature(self) -> str:
        return pulumi.get(self, "signature")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetAuthenticatedOriginPullsResult(GetAuthenticatedOriginPullsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthenticatedOriginPullsResult(
            cert_id=self.cert_id,
            cert_status=self.cert_status,
            cert_updated_at=self.cert_updated_at,
            cert_uploaded_on=self.cert_uploaded_on,
            certificate=self.certificate,
            created_at=self.created_at,
            enabled=self.enabled,
            expires_on=self.expires_on,
            hostname=self.hostname,
            id=self.id,
            issuer=self.issuer,
            serial_number=self.serial_number,
            signature=self.signature,
            status=self.status,
            updated_at=self.updated_at,
            zone_id=self.zone_id)


def get_authenticated_origin_pulls(zone_id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthenticatedOriginPullsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getAuthenticatedOriginPulls:getAuthenticatedOriginPulls', __args__, opts=opts, typ=GetAuthenticatedOriginPullsResult, package_ref=_utilities.get_package()).value

    return AwaitableGetAuthenticatedOriginPullsResult(
        cert_id=pulumi.get(__ret__, 'cert_id'),
        cert_status=pulumi.get(__ret__, 'cert_status'),
        cert_updated_at=pulumi.get(__ret__, 'cert_updated_at'),
        cert_uploaded_on=pulumi.get(__ret__, 'cert_uploaded_on'),
        certificate=pulumi.get(__ret__, 'certificate'),
        created_at=pulumi.get(__ret__, 'created_at'),
        enabled=pulumi.get(__ret__, 'enabled'),
        expires_on=pulumi.get(__ret__, 'expires_on'),
        hostname=pulumi.get(__ret__, 'hostname'),
        id=pulumi.get(__ret__, 'id'),
        issuer=pulumi.get(__ret__, 'issuer'),
        serial_number=pulumi.get(__ret__, 'serial_number'),
        signature=pulumi.get(__ret__, 'signature'),
        status=pulumi.get(__ret__, 'status'),
        updated_at=pulumi.get(__ret__, 'updated_at'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_authenticated_origin_pulls_output(zone_id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetAuthenticatedOriginPullsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('cloudflare:index/getAuthenticatedOriginPulls:getAuthenticatedOriginPulls', __args__, opts=opts, typ=GetAuthenticatedOriginPullsResult, package_ref=_utilities.get_package())
    return __ret__.apply(lambda __response__: GetAuthenticatedOriginPullsResult(
        cert_id=pulumi.get(__response__, 'cert_id'),
        cert_status=pulumi.get(__response__, 'cert_status'),
        cert_updated_at=pulumi.get(__response__, 'cert_updated_at'),
        cert_uploaded_on=pulumi.get(__response__, 'cert_uploaded_on'),
        certificate=pulumi.get(__response__, 'certificate'),
        created_at=pulumi.get(__response__, 'created_at'),
        enabled=pulumi.get(__response__, 'enabled'),
        expires_on=pulumi.get(__response__, 'expires_on'),
        hostname=pulumi.get(__response__, 'hostname'),
        id=pulumi.get(__response__, 'id'),
        issuer=pulumi.get(__response__, 'issuer'),
        serial_number=pulumi.get(__response__, 'serial_number'),
        signature=pulumi.get(__response__, 'signature'),
        status=pulumi.get(__response__, 'status'),
        updated_at=pulumi.get(__response__, 'updated_at'),
        zone_id=pulumi.get(__response__, 'zone_id')))
