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

__all__ = ['ZeroTrustAccessIdentityProviderArgs', 'ZeroTrustAccessIdentityProvider']

@pulumi.input_type
class ZeroTrustAccessIdentityProviderArgs:
    def __init__(__self__, *,
                 config: pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs'],
                 type: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scim_config: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ZeroTrustAccessIdentityProvider resource.
        :param pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs'] config: The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
               to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] type: The type of identity provider. To determine the value for a specific provider, refer to our [developer
               documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        :param pulumi.Input[str] name: The name of the identity provider, shown to users on the login page.
        :param pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs'] scim_config: The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        :param pulumi.Input[str] zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "type", type)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scim_config is not None:
            pulumi.set(__self__, "scim_config", scim_config)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs']:
        """
        The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
        to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs']):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of identity provider. To determine the value for a specific provider, refer to our [developer
        documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the identity provider, shown to users on the login page.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scimConfig")
    def scim_config(self) -> Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']]:
        """
        The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        """
        return pulumi.get(self, "scim_config")

    @scim_config.setter
    def scim_config(self, value: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']]):
        pulumi.set(self, "scim_config", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _ZeroTrustAccessIdentityProviderState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scim_config: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZeroTrustAccessIdentityProvider resources.
        :param pulumi.Input[str] account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        :param pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs'] config: The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
               to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] name: The name of the identity provider, shown to users on the login page.
        :param pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs'] scim_config: The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        :param pulumi.Input[str] type: The type of identity provider. To determine the value for a specific provider, refer to our [developer
               documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if scim_config is not None:
            pulumi.set(__self__, "scim_config", scim_config)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs']]:
        """
        The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
        to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderConfigArgs']]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the identity provider, shown to users on the login page.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="scimConfig")
    def scim_config(self) -> Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']]:
        """
        The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        """
        return pulumi.get(self, "scim_config")

    @scim_config.setter
    def scim_config(self, value: Optional[pulumi.Input['ZeroTrustAccessIdentityProviderScimConfigArgs']]):
        pulumi.set(self, "scim_config", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of identity provider. To determine the value for a specific provider, refer to our [developer
        documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class ZeroTrustAccessIdentityProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderConfigArgs', 'ZeroTrustAccessIdentityProviderConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scim_config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderScimConfigArgs', 'ZeroTrustAccessIdentityProviderScimConfigArgsDict']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ZeroTrustAccessIdentityProvider resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        :param pulumi.Input[Union['ZeroTrustAccessIdentityProviderConfigArgs', 'ZeroTrustAccessIdentityProviderConfigArgsDict']] config: The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
               to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] name: The name of the identity provider, shown to users on the login page.
        :param pulumi.Input[Union['ZeroTrustAccessIdentityProviderScimConfigArgs', 'ZeroTrustAccessIdentityProviderScimConfigArgsDict']] scim_config: The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        :param pulumi.Input[str] type: The type of identity provider. To determine the value for a specific provider, refer to our [developer
               documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZeroTrustAccessIdentityProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZeroTrustAccessIdentityProvider resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZeroTrustAccessIdentityProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZeroTrustAccessIdentityProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderConfigArgs', 'ZeroTrustAccessIdentityProviderConfigArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scim_config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderScimConfigArgs', 'ZeroTrustAccessIdentityProviderScimConfigArgsDict']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZeroTrustAccessIdentityProviderArgs.__new__(ZeroTrustAccessIdentityProviderArgs)

            __props__.__dict__["account_id"] = account_id
            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            __props__.__dict__["name"] = name
            __props__.__dict__["scim_config"] = scim_config
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["zone_id"] = zone_id
        super(ZeroTrustAccessIdentityProvider, __self__).__init__(
            'cloudflare:index/zeroTrustAccessIdentityProvider:ZeroTrustAccessIdentityProvider',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderConfigArgs', 'ZeroTrustAccessIdentityProviderConfigArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            scim_config: Optional[pulumi.Input[Union['ZeroTrustAccessIdentityProviderScimConfigArgs', 'ZeroTrustAccessIdentityProviderScimConfigArgsDict']]] = None,
            type: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ZeroTrustAccessIdentityProvider':
        """
        Get an existing ZeroTrustAccessIdentityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        :param pulumi.Input[Union['ZeroTrustAccessIdentityProviderConfigArgs', 'ZeroTrustAccessIdentityProviderConfigArgsDict']] config: The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
               to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] name: The name of the identity provider, shown to users on the login page.
        :param pulumi.Input[Union['ZeroTrustAccessIdentityProviderScimConfigArgs', 'ZeroTrustAccessIdentityProviderScimConfigArgsDict']] scim_config: The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        :param pulumi.Input[str] type: The type of identity provider. To determine the value for a specific provider, refer to our [developer
               documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        :param pulumi.Input[str] zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZeroTrustAccessIdentityProviderState.__new__(_ZeroTrustAccessIdentityProviderState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["config"] = config
        __props__.__dict__["name"] = name
        __props__.__dict__["scim_config"] = scim_config
        __props__.__dict__["type"] = type
        __props__.__dict__["zone_id"] = zone_id
        return ZeroTrustAccessIdentityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output['outputs.ZeroTrustAccessIdentityProviderConfig']:
        """
        The configuration parameters for the identity provider. To view the required parameters for a specific provider, refer
        to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the identity provider, shown to users on the login page.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scimConfig")
    def scim_config(self) -> pulumi.Output['outputs.ZeroTrustAccessIdentityProviderScimConfig']:
        """
        The configuration settings for enabling a System for Cross-Domain Identity Management (SCIM) with the identity provider.
        """
        return pulumi.get(self, "scim_config")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of identity provider. To determine the value for a specific provider, refer to our [developer
        documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.
        """
        return pulumi.get(self, "zone_id")

