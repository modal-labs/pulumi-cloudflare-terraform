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

__all__ = ['ZeroTrustGatewayLoggingArgs', 'ZeroTrustGatewayLogging']

@pulumi.input_type
class ZeroTrustGatewayLoggingArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 redact_pii: Optional[pulumi.Input[bool]] = None,
                 settings_by_rule_type: Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']] = None):
        """
        The set of arguments for constructing a ZeroTrustGatewayLogging resource.
        :param pulumi.Input[bool] redact_pii: Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
               ID, URL, referrer, user agent).
        :param pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs'] settings_by_rule_type: Logging settings by rule type.
        """
        pulumi.set(__self__, "account_id", account_id)
        if redact_pii is not None:
            pulumi.set(__self__, "redact_pii", redact_pii)
        if settings_by_rule_type is not None:
            pulumi.set(__self__, "settings_by_rule_type", settings_by_rule_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="redactPii")
    def redact_pii(self) -> Optional[pulumi.Input[bool]]:
        """
        Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
        ID, URL, referrer, user agent).
        """
        return pulumi.get(self, "redact_pii")

    @redact_pii.setter
    def redact_pii(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "redact_pii", value)

    @property
    @pulumi.getter(name="settingsByRuleType")
    def settings_by_rule_type(self) -> Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']]:
        """
        Logging settings by rule type.
        """
        return pulumi.get(self, "settings_by_rule_type")

    @settings_by_rule_type.setter
    def settings_by_rule_type(self, value: Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']]):
        pulumi.set(self, "settings_by_rule_type", value)


@pulumi.input_type
class _ZeroTrustGatewayLoggingState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 redact_pii: Optional[pulumi.Input[bool]] = None,
                 settings_by_rule_type: Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']] = None):
        """
        Input properties used for looking up and filtering ZeroTrustGatewayLogging resources.
        :param pulumi.Input[bool] redact_pii: Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
               ID, URL, referrer, user agent).
        :param pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs'] settings_by_rule_type: Logging settings by rule type.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if redact_pii is not None:
            pulumi.set(__self__, "redact_pii", redact_pii)
        if settings_by_rule_type is not None:
            pulumi.set(__self__, "settings_by_rule_type", settings_by_rule_type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="redactPii")
    def redact_pii(self) -> Optional[pulumi.Input[bool]]:
        """
        Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
        ID, URL, referrer, user agent).
        """
        return pulumi.get(self, "redact_pii")

    @redact_pii.setter
    def redact_pii(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "redact_pii", value)

    @property
    @pulumi.getter(name="settingsByRuleType")
    def settings_by_rule_type(self) -> Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']]:
        """
        Logging settings by rule type.
        """
        return pulumi.get(self, "settings_by_rule_type")

    @settings_by_rule_type.setter
    def settings_by_rule_type(self, value: Optional[pulumi.Input['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs']]):
        pulumi.set(self, "settings_by_rule_type", value)


class ZeroTrustGatewayLogging(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 redact_pii: Optional[pulumi.Input[bool]] = None,
                 settings_by_rule_type: Optional[pulumi.Input[Union['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs', 'ZeroTrustGatewayLoggingSettingsByRuleTypeArgsDict']]] = None,
                 __props__=None):
        """
        Create a ZeroTrustGatewayLogging resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] redact_pii: Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
               ID, URL, referrer, user agent).
        :param pulumi.Input[Union['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs', 'ZeroTrustGatewayLoggingSettingsByRuleTypeArgsDict']] settings_by_rule_type: Logging settings by rule type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZeroTrustGatewayLoggingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZeroTrustGatewayLogging resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZeroTrustGatewayLoggingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZeroTrustGatewayLoggingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 redact_pii: Optional[pulumi.Input[bool]] = None,
                 settings_by_rule_type: Optional[pulumi.Input[Union['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs', 'ZeroTrustGatewayLoggingSettingsByRuleTypeArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZeroTrustGatewayLoggingArgs.__new__(ZeroTrustGatewayLoggingArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["redact_pii"] = redact_pii
            __props__.__dict__["settings_by_rule_type"] = settings_by_rule_type
        super(ZeroTrustGatewayLogging, __self__).__init__(
            'cloudflare:index/zeroTrustGatewayLogging:ZeroTrustGatewayLogging',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            redact_pii: Optional[pulumi.Input[bool]] = None,
            settings_by_rule_type: Optional[pulumi.Input[Union['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs', 'ZeroTrustGatewayLoggingSettingsByRuleTypeArgsDict']]] = None) -> 'ZeroTrustGatewayLogging':
        """
        Get an existing ZeroTrustGatewayLogging resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] redact_pii: Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
               ID, URL, referrer, user agent).
        :param pulumi.Input[Union['ZeroTrustGatewayLoggingSettingsByRuleTypeArgs', 'ZeroTrustGatewayLoggingSettingsByRuleTypeArgsDict']] settings_by_rule_type: Logging settings by rule type.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZeroTrustGatewayLoggingState.__new__(_ZeroTrustGatewayLoggingState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["redact_pii"] = redact_pii
        __props__.__dict__["settings_by_rule_type"] = settings_by_rule_type
        return ZeroTrustGatewayLogging(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="redactPii")
    def redact_pii(self) -> pulumi.Output[Optional[bool]]:
        """
        Redact personally identifiable information from activity logging (PII fields are: source IP, user email, user ID, device
        ID, URL, referrer, user agent).
        """
        return pulumi.get(self, "redact_pii")

    @property
    @pulumi.getter(name="settingsByRuleType")
    def settings_by_rule_type(self) -> pulumi.Output['outputs.ZeroTrustGatewayLoggingSettingsByRuleType']:
        """
        Logging settings by rule type.
        """
        return pulumi.get(self, "settings_by_rule_type")

