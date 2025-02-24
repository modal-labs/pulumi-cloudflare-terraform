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
from ._inputs import *

__all__ = ['ZeroTrustTunnelCloudflaredConfigArgs', 'ZeroTrustTunnelCloudflaredConfig']

@pulumi.input_type
class ZeroTrustTunnelCloudflaredConfigArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 tunnel_id: pulumi.Input[str],
                 config: Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZeroTrustTunnelCloudflaredConfig resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[str] tunnel_id: UUID of the tunnel.
        :param pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs'] config: The tunnel configuration and ingress rules.
        :param pulumi.Input[str] source: Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
               origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "tunnel_id", tunnel_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Identifier
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> pulumi.Input[str]:
        """
        UUID of the tunnel.
        """
        return pulumi.get(self, "tunnel_id")

    @tunnel_id.setter
    def tunnel_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tunnel_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']]:
        """
        The tunnel configuration and ingress rules.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
        origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


@pulumi.input_type
class _ZeroTrustTunnelCloudflaredConfigState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[float]] = None):
        """
        Input properties used for looking up and filtering ZeroTrustTunnelCloudflaredConfig resources.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs'] config: The tunnel configuration and ingress rules.
        :param pulumi.Input[str] source: Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
               origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        :param pulumi.Input[str] tunnel_id: UUID of the tunnel.
        :param pulumi.Input[float] version: The version of the Tunnel Configuration.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tunnel_id is not None:
            pulumi.set(__self__, "tunnel_id", tunnel_id)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']]:
        """
        The tunnel configuration and ingress rules.
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['ZeroTrustTunnelCloudflaredConfigConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
        origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the tunnel.
        """
        return pulumi.get(self, "tunnel_id")

    @tunnel_id.setter
    def tunnel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tunnel_id", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[float]]:
        """
        The version of the Tunnel Configuration.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "version", value)


class ZeroTrustTunnelCloudflaredConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Union['ZeroTrustTunnelCloudflaredConfigConfigArgs', 'ZeroTrustTunnelCloudflaredConfigConfigArgsDict']]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZeroTrustTunnelCloudflaredConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[Union['ZeroTrustTunnelCloudflaredConfigConfigArgs', 'ZeroTrustTunnelCloudflaredConfigConfigArgsDict']] config: The tunnel configuration and ingress rules.
        :param pulumi.Input[str] source: Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
               origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        :param pulumi.Input[str] tunnel_id: UUID of the tunnel.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZeroTrustTunnelCloudflaredConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZeroTrustTunnelCloudflaredConfig resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZeroTrustTunnelCloudflaredConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZeroTrustTunnelCloudflaredConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Union['ZeroTrustTunnelCloudflaredConfigConfigArgs', 'ZeroTrustTunnelCloudflaredConfigConfigArgsDict']]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 tunnel_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZeroTrustTunnelCloudflaredConfigArgs.__new__(ZeroTrustTunnelCloudflaredConfigArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["config"] = config
            __props__.__dict__["source"] = source
            if tunnel_id is None and not opts.urn:
                raise TypeError("Missing required property 'tunnel_id'")
            __props__.__dict__["tunnel_id"] = tunnel_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["version"] = None
        super(ZeroTrustTunnelCloudflaredConfig, __self__).__init__(
            'cloudflare:index/zeroTrustTunnelCloudflaredConfig:ZeroTrustTunnelCloudflaredConfig',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[Union['ZeroTrustTunnelCloudflaredConfigConfigArgs', 'ZeroTrustTunnelCloudflaredConfigConfigArgsDict']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            tunnel_id: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[float]] = None) -> 'ZeroTrustTunnelCloudflaredConfig':
        """
        Get an existing ZeroTrustTunnelCloudflaredConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[Union['ZeroTrustTunnelCloudflaredConfigConfigArgs', 'ZeroTrustTunnelCloudflaredConfigConfigArgsDict']] config: The tunnel configuration and ingress rules.
        :param pulumi.Input[str] source: Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
               origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        :param pulumi.Input[str] tunnel_id: UUID of the tunnel.
        :param pulumi.Input[float] version: The version of the Tunnel Configuration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZeroTrustTunnelCloudflaredConfigState.__new__(_ZeroTrustTunnelCloudflaredConfigState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["config"] = config
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["source"] = source
        __props__.__dict__["tunnel_id"] = tunnel_id
        __props__.__dict__["version"] = version
        return ZeroTrustTunnelCloudflaredConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.ZeroTrustTunnelCloudflaredConfigConfig']:
        """
        The tunnel configuration and ingress rules.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        Indicates if this is a locally or remotely configured tunnel. If `local`, manage the tunnel using a YAML file on the
        origin machine. If `cloudflare`, manage the tunnel's configuration on the Zero Trust dashboard.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="tunnelId")
    def tunnel_id(self) -> pulumi.Output[str]:
        """
        UUID of the tunnel.
        """
        return pulumi.get(self, "tunnel_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[float]:
        """
        The version of the Tunnel Configuration.
        """
        return pulumi.get(self, "version")

