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

__all__ = ['MagicNetworkMonitoringConfigurationArgs', 'MagicNetworkMonitoringConfiguration']

@pulumi.input_type
class MagicNetworkMonitoringConfigurationArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 default_sampling: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 warp_devices: Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]] = None):
        """
        The set of arguments for constructing a MagicNetworkMonitoringConfiguration resource.
        :param pulumi.Input[float] default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
               configured on the router.
        :param pulumi.Input[str] name: The account name.
        """
        pulumi.set(__self__, "account_id", account_id)
        if default_sampling is not None:
            pulumi.set(__self__, "default_sampling", default_sampling)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if router_ips is not None:
            pulumi.set(__self__, "router_ips", router_ips)
        if warp_devices is not None:
            pulumi.set(__self__, "warp_devices", warp_devices)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="defaultSampling")
    def default_sampling(self) -> Optional[pulumi.Input[float]]:
        """
        Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
        configured on the router.
        """
        return pulumi.get(self, "default_sampling")

    @default_sampling.setter
    def default_sampling(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "default_sampling", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The account name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routerIps")
    def router_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "router_ips")

    @router_ips.setter
    def router_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "router_ips", value)

    @property
    @pulumi.getter(name="warpDevices")
    def warp_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]]:
        return pulumi.get(self, "warp_devices")

    @warp_devices.setter
    def warp_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]]):
        pulumi.set(self, "warp_devices", value)


@pulumi.input_type
class _MagicNetworkMonitoringConfigurationState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 default_sampling: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 warp_devices: Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]] = None):
        """
        Input properties used for looking up and filtering MagicNetworkMonitoringConfiguration resources.
        :param pulumi.Input[float] default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
               configured on the router.
        :param pulumi.Input[str] name: The account name.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if default_sampling is not None:
            pulumi.set(__self__, "default_sampling", default_sampling)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if router_ips is not None:
            pulumi.set(__self__, "router_ips", router_ips)
        if warp_devices is not None:
            pulumi.set(__self__, "warp_devices", warp_devices)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="defaultSampling")
    def default_sampling(self) -> Optional[pulumi.Input[float]]:
        """
        Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
        configured on the router.
        """
        return pulumi.get(self, "default_sampling")

    @default_sampling.setter
    def default_sampling(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "default_sampling", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The account name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routerIps")
    def router_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "router_ips")

    @router_ips.setter
    def router_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "router_ips", value)

    @property
    @pulumi.getter(name="warpDevices")
    def warp_devices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]]:
        return pulumi.get(self, "warp_devices")

    @warp_devices.setter
    def warp_devices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MagicNetworkMonitoringConfigurationWarpDeviceArgs']]]]):
        pulumi.set(self, "warp_devices", value)


class MagicNetworkMonitoringConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 default_sampling: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 warp_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MagicNetworkMonitoringConfigurationWarpDeviceArgs', 'MagicNetworkMonitoringConfigurationWarpDeviceArgsDict']]]]] = None,
                 __props__=None):
        """
        Create a MagicNetworkMonitoringConfiguration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
               configured on the router.
        :param pulumi.Input[str] name: The account name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MagicNetworkMonitoringConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MagicNetworkMonitoringConfiguration resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MagicNetworkMonitoringConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MagicNetworkMonitoringConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 default_sampling: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 warp_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MagicNetworkMonitoringConfigurationWarpDeviceArgs', 'MagicNetworkMonitoringConfigurationWarpDeviceArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MagicNetworkMonitoringConfigurationArgs.__new__(MagicNetworkMonitoringConfigurationArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["default_sampling"] = default_sampling
            __props__.__dict__["name"] = name
            __props__.__dict__["router_ips"] = router_ips
            __props__.__dict__["warp_devices"] = warp_devices
        super(MagicNetworkMonitoringConfiguration, __self__).__init__(
            'cloudflare:index/magicNetworkMonitoringConfiguration:MagicNetworkMonitoringConfiguration',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            default_sampling: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            router_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            warp_devices: Optional[pulumi.Input[Sequence[pulumi.Input[Union['MagicNetworkMonitoringConfigurationWarpDeviceArgs', 'MagicNetworkMonitoringConfigurationWarpDeviceArgsDict']]]]] = None) -> 'MagicNetworkMonitoringConfiguration':
        """
        Get an existing MagicNetworkMonitoringConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] default_sampling: Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
               configured on the router.
        :param pulumi.Input[str] name: The account name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MagicNetworkMonitoringConfigurationState.__new__(_MagicNetworkMonitoringConfigurationState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["default_sampling"] = default_sampling
        __props__.__dict__["name"] = name
        __props__.__dict__["router_ips"] = router_ips
        __props__.__dict__["warp_devices"] = warp_devices
        return MagicNetworkMonitoringConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="defaultSampling")
    def default_sampling(self) -> pulumi.Output[float]:
        """
        Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate
        configured on the router.
        """
        return pulumi.get(self, "default_sampling")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The account name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routerIps")
    def router_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "router_ips")

    @property
    @pulumi.getter(name="warpDevices")
    def warp_devices(self) -> pulumi.Output[Sequence['outputs.MagicNetworkMonitoringConfigurationWarpDevice']]:
        return pulumi.get(self, "warp_devices")

