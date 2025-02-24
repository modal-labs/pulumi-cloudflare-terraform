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

__all__ = ['ZoneHoldArgs', 'ZoneHold']

@pulumi.input_type
class ZoneHoldArgs:
    def __init__(__self__, *,
                 zone_id: pulumi.Input[str],
                 hold_after: Optional[pulumi.Input[str]] = None,
                 include_subdomains: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ZoneHold resource.
        :param pulumi.Input[str] zone_id: Identifier
        :param pulumi.Input[str] hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
               the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
               effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        :param pulumi.Input[bool] include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
               example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
               'staging.example.com', 'api.staging.example.com', etc.
        """
        pulumi.set(__self__, "zone_id", zone_id)
        if hold_after is not None:
            pulumi.set(__self__, "hold_after", hold_after)
        if include_subdomains is not None:
            pulumi.set(__self__, "include_subdomains", include_subdomains)

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

    @property
    @pulumi.getter(name="holdAfter")
    def hold_after(self) -> Optional[pulumi.Input[str]]:
        """
        If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
        the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
        effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        """
        return pulumi.get(self, "hold_after")

    @hold_after.setter
    def hold_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hold_after", value)

    @property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> Optional[pulumi.Input[bool]]:
        """
        If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
        example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
        'staging.example.com', 'api.staging.example.com', etc.
        """
        return pulumi.get(self, "include_subdomains")

    @include_subdomains.setter
    def include_subdomains(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_subdomains", value)


@pulumi.input_type
class _ZoneHoldState:
    def __init__(__self__, *,
                 hold: Optional[pulumi.Input[bool]] = None,
                 hold_after: Optional[pulumi.Input[str]] = None,
                 include_subdomains: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZoneHold resources.
        :param pulumi.Input[str] hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
               the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
               effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        :param pulumi.Input[bool] include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
               example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
               'staging.example.com', 'api.staging.example.com', etc.
        :param pulumi.Input[str] zone_id: Identifier
        """
        if hold is not None:
            pulumi.set(__self__, "hold", hold)
        if hold_after is not None:
            pulumi.set(__self__, "hold_after", hold_after)
        if include_subdomains is not None:
            pulumi.set(__self__, "include_subdomains", include_subdomains)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def hold(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "hold")

    @hold.setter
    def hold(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hold", value)

    @property
    @pulumi.getter(name="holdAfter")
    def hold_after(self) -> Optional[pulumi.Input[str]]:
        """
        If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
        the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
        effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        """
        return pulumi.get(self, "hold_after")

    @hold_after.setter
    def hold_after(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hold_after", value)

    @property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> Optional[pulumi.Input[bool]]:
        """
        If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
        example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
        'staging.example.com', 'api.staging.example.com', etc.
        """
        return pulumi.get(self, "include_subdomains")

    @include_subdomains.setter
    def include_subdomains(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_subdomains", value)

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


class ZoneHold(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hold_after: Optional[pulumi.Input[str]] = None,
                 include_subdomains: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZoneHold resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
               the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
               effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        :param pulumi.Input[bool] include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
               example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
               'staging.example.com', 'api.staging.example.com', etc.
        :param pulumi.Input[str] zone_id: Identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZoneHoldArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZoneHold resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZoneHoldArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneHoldArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hold_after: Optional[pulumi.Input[str]] = None,
                 include_subdomains: Optional[pulumi.Input[bool]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneHoldArgs.__new__(ZoneHoldArgs)

            __props__.__dict__["hold_after"] = hold_after
            __props__.__dict__["include_subdomains"] = include_subdomains
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["hold"] = None
        super(ZoneHold, __self__).__init__(
            'cloudflare:index/zoneHold:ZoneHold',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            hold: Optional[pulumi.Input[bool]] = None,
            hold_after: Optional[pulumi.Input[str]] = None,
            include_subdomains: Optional[pulumi.Input[bool]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ZoneHold':
        """
        Get an existing ZoneHold resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hold_after: If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
               the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
               effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        :param pulumi.Input[bool] include_subdomains: If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
               example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
               'staging.example.com', 'api.staging.example.com', etc.
        :param pulumi.Input[str] zone_id: Identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneHoldState.__new__(_ZoneHoldState)

        __props__.__dict__["hold"] = hold
        __props__.__dict__["hold_after"] = hold_after
        __props__.__dict__["include_subdomains"] = include_subdomains
        __props__.__dict__["zone_id"] = zone_id
        return ZoneHold(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def hold(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "hold")

    @property
    @pulumi.getter(name="holdAfter")
    def hold_after(self) -> pulumi.Output[str]:
        """
        If `hold_after` is provided and future-dated, the hold will be temporarily disabled, then automatically re-enabled by
        the system at the time specified in this RFC3339-formatted timestamp. A past-dated `hold_after` value will have no
        effect on an existing, enabled hold. Providing an empty string will set its value to the current time.
        """
        return pulumi.get(self, "hold_after")

    @property
    @pulumi.getter(name="includeSubdomains")
    def include_subdomains(self) -> pulumi.Output[bool]:
        """
        If `true`, the zone hold will extend to block any subdomain of the given zone, as well as SSL4SaaS Custom Hostnames. For
        example, a zone hold on a zone with the hostname 'example.com' and include_subdomains=true will block 'example.com',
        'staging.example.com', 'api.staging.example.com', etc.
        """
        return pulumi.get(self, "include_subdomains")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

