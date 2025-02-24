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

__all__ = ['DnsZoneTransfersPeerArgs', 'DnsZoneTransfersPeer']

@pulumi.input_type
class DnsZoneTransfersPeerArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 ip: Optional[pulumi.Input[str]] = None,
                 ixfr_enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 tsig_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DnsZoneTransfersPeer resource.
        :param pulumi.Input[str] ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
               this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
               defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        :param pulumi.Input[bool] ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        :param pulumi.Input[str] name: The name of the peer.
        :param pulumi.Input[float] port: DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        :param pulumi.Input[str] tsig_id: TSIG authentication will be used for zone transfer if configured.
        """
        pulumi.set(__self__, "account_id", account_id)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if ixfr_enable is not None:
            pulumi.set(__self__, "ixfr_enable", ixfr_enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if tsig_id is not None:
            pulumi.set(__self__, "tsig_id", tsig_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
        this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
        defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="ixfrEnable")
    def ixfr_enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        """
        return pulumi.get(self, "ixfr_enable")

    @ixfr_enable.setter
    def ixfr_enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ixfr_enable", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peer.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[float]]:
        """
        DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="tsigId")
    def tsig_id(self) -> Optional[pulumi.Input[str]]:
        """
        TSIG authentication will be used for zone transfer if configured.
        """
        return pulumi.get(self, "tsig_id")

    @tsig_id.setter
    def tsig_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tsig_id", value)


@pulumi.input_type
class _DnsZoneTransfersPeerState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 ixfr_enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 tsig_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DnsZoneTransfersPeer resources.
        :param pulumi.Input[str] ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
               this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
               defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        :param pulumi.Input[bool] ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        :param pulumi.Input[str] name: The name of the peer.
        :param pulumi.Input[float] port: DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        :param pulumi.Input[str] tsig_id: TSIG authentication will be used for zone transfer if configured.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if ixfr_enable is not None:
            pulumi.set(__self__, "ixfr_enable", ixfr_enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if tsig_id is not None:
            pulumi.set(__self__, "tsig_id", tsig_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
        this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
        defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="ixfrEnable")
    def ixfr_enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        """
        return pulumi.get(self, "ixfr_enable")

    @ixfr_enable.setter
    def ixfr_enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ixfr_enable", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peer.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[float]]:
        """
        DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="tsigId")
    def tsig_id(self) -> Optional[pulumi.Input[str]]:
        """
        TSIG authentication will be used for zone transfer if configured.
        """
        return pulumi.get(self, "tsig_id")

    @tsig_id.setter
    def tsig_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tsig_id", value)


class DnsZoneTransfersPeer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 ixfr_enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 tsig_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DnsZoneTransfersPeer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
               this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
               defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        :param pulumi.Input[bool] ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        :param pulumi.Input[str] name: The name of the peer.
        :param pulumi.Input[float] port: DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        :param pulumi.Input[str] tsig_id: TSIG authentication will be used for zone transfer if configured.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DnsZoneTransfersPeerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DnsZoneTransfersPeer resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DnsZoneTransfersPeerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DnsZoneTransfersPeerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 ixfr_enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[float]] = None,
                 tsig_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DnsZoneTransfersPeerArgs.__new__(DnsZoneTransfersPeerArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["ip"] = ip
            __props__.__dict__["ixfr_enable"] = ixfr_enable
            __props__.__dict__["name"] = name
            __props__.__dict__["port"] = port
            __props__.__dict__["tsig_id"] = tsig_id
        super(DnsZoneTransfersPeer, __self__).__init__(
            'cloudflare:index/dnsZoneTransfersPeer:DnsZoneTransfersPeer',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            ip: Optional[pulumi.Input[str]] = None,
            ixfr_enable: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[float]] = None,
            tsig_id: Optional[pulumi.Input[str]] = None) -> 'DnsZoneTransfersPeer':
        """
        Get an existing DnsZoneTransfersPeer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip: IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
               this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
               defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        :param pulumi.Input[bool] ixfr_enable: Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        :param pulumi.Input[str] name: The name of the peer.
        :param pulumi.Input[float] port: DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        :param pulumi.Input[str] tsig_id: TSIG authentication will be used for zone transfer if configured.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DnsZoneTransfersPeerState.__new__(_DnsZoneTransfersPeerState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["ip"] = ip
        __props__.__dict__["ixfr_enable"] = ixfr_enable
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["tsig_id"] = tsig_id
        return DnsZoneTransfersPeer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[Optional[str]]:
        """
        IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones
        this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP
        defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="ixfrEnable")
    def ixfr_enable(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
        """
        return pulumi.get(self, "ixfr_enable")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the peer.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[float]]:
        """
        DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="tsigId")
    def tsig_id(self) -> pulumi.Output[Optional[str]]:
        """
        TSIG authentication will be used for zone transfer if configured.
        """
        return pulumi.get(self, "tsig_id")

