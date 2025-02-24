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

__all__ = ['RegionalHostnameArgs', 'RegionalHostname']

@pulumi.input_type
class RegionalHostnameArgs:
    def __init__(__self__, *,
                 hostname: pulumi.Input[str],
                 region_key: pulumi.Input[str],
                 zone_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a RegionalHostname resource.
        :param pulumi.Input[str] hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
               `*.example.com`
        :param pulumi.Input[str] region_key: Identifying key for the region
        :param pulumi.Input[str] zone_id: Identifier
        """
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "region_key", region_key)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Input[str]:
        """
        DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
        `*.example.com`
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: pulumi.Input[str]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="regionKey")
    def region_key(self) -> pulumi.Input[str]:
        """
        Identifying key for the region
        """
        return pulumi.get(self, "region_key")

    @region_key.setter
    def region_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "region_key", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _RegionalHostnameState:
    def __init__(__self__, *,
                 created_on: Optional[pulumi.Input[str]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 region_key: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RegionalHostname resources.
        :param pulumi.Input[str] created_on: When the regional hostname was created
        :param pulumi.Input[str] hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
               `*.example.com`
        :param pulumi.Input[str] region_key: Identifying key for the region
        :param pulumi.Input[str] zone_id: Identifier
        """
        if created_on is not None:
            pulumi.set(__self__, "created_on", created_on)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if region_key is not None:
            pulumi.set(__self__, "region_key", region_key)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[str]]:
        """
        When the regional hostname was created
        """
        return pulumi.get(self, "created_on")

    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_on", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
        `*.example.com`
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="regionKey")
    def region_key(self) -> Optional[pulumi.Input[str]]:
        """
        Identifying key for the region
        """
        return pulumi.get(self, "region_key")

    @region_key.setter
    def region_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region_key", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class RegionalHostname(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 region_key: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a RegionalHostname resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
               `*.example.com`
        :param pulumi.Input[str] region_key: Identifying key for the region
        :param pulumi.Input[str] zone_id: Identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegionalHostnameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a RegionalHostname resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param RegionalHostnameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegionalHostnameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 region_key: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegionalHostnameArgs.__new__(RegionalHostnameArgs)

            if hostname is None and not opts.urn:
                raise TypeError("Missing required property 'hostname'")
            __props__.__dict__["hostname"] = hostname
            if region_key is None and not opts.urn:
                raise TypeError("Missing required property 'region_key'")
            __props__.__dict__["region_key"] = region_key
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["created_on"] = None
        super(RegionalHostname, __self__).__init__(
            'cloudflare:index/regionalHostname:RegionalHostname',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_on: Optional[pulumi.Input[str]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            region_key: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'RegionalHostname':
        """
        Get an existing RegionalHostname resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_on: When the regional hostname was created
        :param pulumi.Input[str] hostname: DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
               `*.example.com`
        :param pulumi.Input[str] region_key: Identifying key for the region
        :param pulumi.Input[str] zone_id: Identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegionalHostnameState.__new__(_RegionalHostnameState)

        __props__.__dict__["created_on"] = created_on
        __props__.__dict__["hostname"] = hostname
        __props__.__dict__["region_key"] = region_key
        __props__.__dict__["zone_id"] = zone_id
        return RegionalHostname(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        When the regional hostname was created
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        """
        DNS hostname to be regionalized, must be a subdomain of the zone. Wildcards are supported for one level, e.g
        `*.example.com`
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="regionKey")
    def region_key(self) -> pulumi.Output[str]:
        """
        Identifying key for the region
        """
        return pulumi.get(self, "region_key")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

