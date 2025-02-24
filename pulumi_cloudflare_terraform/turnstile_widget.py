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

__all__ = ['TurnstileWidgetArgs', 'TurnstileWidget']

@pulumi.input_type
class TurnstileWidgetArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 domains: pulumi.Input[Sequence[pulumi.Input[str]]],
                 mode: pulumi.Input[str],
                 bot_fight_mode: Optional[pulumi.Input[bool]] = None,
                 clearance_level: Optional[pulumi.Input[str]] = None,
                 ephemeral_id: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offlabel: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TurnstileWidget resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[str] mode: Widget Mode
        :param pulumi.Input[bool] bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
               (ENT only).
        :param pulumi.Input[str] clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
               determine the clearance level to be set
        :param pulumi.Input[bool] ephemeral_id: Return the Ephemeral ID in /siteverify (ENT only).
        :param pulumi.Input[str] name: Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
               to identify your widget, and where it is used.
        :param pulumi.Input[bool] offlabel: Do not show any Cloudflare branding on the widget (ENT only).
        :param pulumi.Input[str] region: Region where this widget can be used.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "domains", domains)
        pulumi.set(__self__, "mode", mode)
        if bot_fight_mode is not None:
            pulumi.set(__self__, "bot_fight_mode", bot_fight_mode)
        if clearance_level is not None:
            pulumi.set(__self__, "clearance_level", clearance_level)
        if ephemeral_id is not None:
            pulumi.set(__self__, "ephemeral_id", ephemeral_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offlabel is not None:
            pulumi.set(__self__, "offlabel", offlabel)
        if region is not None:
            pulumi.set(__self__, "region", region)

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
    @pulumi.getter
    def domains(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[str]:
        """
        Widget Mode
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="botFightMode")
    def bot_fight_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
        (ENT only).
        """
        return pulumi.get(self, "bot_fight_mode")

    @bot_fight_mode.setter
    def bot_fight_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bot_fight_mode", value)

    @property
    @pulumi.getter(name="clearanceLevel")
    def clearance_level(self) -> Optional[pulumi.Input[str]]:
        """
        If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
        determine the clearance level to be set
        """
        return pulumi.get(self, "clearance_level")

    @clearance_level.setter
    def clearance_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "clearance_level", value)

    @property
    @pulumi.getter(name="ephemeralId")
    def ephemeral_id(self) -> Optional[pulumi.Input[bool]]:
        """
        Return the Ephemeral ID in /siteverify (ENT only).
        """
        return pulumi.get(self, "ephemeral_id")

    @ephemeral_id.setter
    def ephemeral_id(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ephemeral_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
        to identify your widget, and where it is used.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def offlabel(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not show any Cloudflare branding on the widget (ENT only).
        """
        return pulumi.get(self, "offlabel")

    @offlabel.setter
    def offlabel(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "offlabel", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where this widget can be used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _TurnstileWidgetState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bot_fight_mode: Optional[pulumi.Input[bool]] = None,
                 clearance_level: Optional[pulumi.Input[str]] = None,
                 created_on: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ephemeral_id: Optional[pulumi.Input[bool]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 modified_on: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offlabel: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 sitekey: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TurnstileWidget resources.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[bool] bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
               (ENT only).
        :param pulumi.Input[str] clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
               determine the clearance level to be set
        :param pulumi.Input[str] created_on: When the widget was created.
        :param pulumi.Input[bool] ephemeral_id: Return the Ephemeral ID in /siteverify (ENT only).
        :param pulumi.Input[str] mode: Widget Mode
        :param pulumi.Input[str] modified_on: When the widget was modified.
        :param pulumi.Input[str] name: Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
               to identify your widget, and where it is used.
        :param pulumi.Input[bool] offlabel: Do not show any Cloudflare branding on the widget (ENT only).
        :param pulumi.Input[str] region: Region where this widget can be used.
        :param pulumi.Input[str] secret: Secret key for this widget.
        :param pulumi.Input[str] sitekey: Widget item identifier tag.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if bot_fight_mode is not None:
            pulumi.set(__self__, "bot_fight_mode", bot_fight_mode)
        if clearance_level is not None:
            pulumi.set(__self__, "clearance_level", clearance_level)
        if created_on is not None:
            pulumi.set(__self__, "created_on", created_on)
        if domains is not None:
            pulumi.set(__self__, "domains", domains)
        if ephemeral_id is not None:
            pulumi.set(__self__, "ephemeral_id", ephemeral_id)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if modified_on is not None:
            pulumi.set(__self__, "modified_on", modified_on)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offlabel is not None:
            pulumi.set(__self__, "offlabel", offlabel)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if sitekey is not None:
            pulumi.set(__self__, "sitekey", sitekey)

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
    @pulumi.getter(name="botFightMode")
    def bot_fight_mode(self) -> Optional[pulumi.Input[bool]]:
        """
        If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
        (ENT only).
        """
        return pulumi.get(self, "bot_fight_mode")

    @bot_fight_mode.setter
    def bot_fight_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "bot_fight_mode", value)

    @property
    @pulumi.getter(name="clearanceLevel")
    def clearance_level(self) -> Optional[pulumi.Input[str]]:
        """
        If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
        determine the clearance level to be set
        """
        return pulumi.get(self, "clearance_level")

    @clearance_level.setter
    def clearance_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "clearance_level", value)

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> Optional[pulumi.Input[str]]:
        """
        When the widget was created.
        """
        return pulumi.get(self, "created_on")

    @created_on.setter
    def created_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_on", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter(name="ephemeralId")
    def ephemeral_id(self) -> Optional[pulumi.Input[bool]]:
        """
        Return the Ephemeral ID in /siteverify (ENT only).
        """
        return pulumi.get(self, "ephemeral_id")

    @ephemeral_id.setter
    def ephemeral_id(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ephemeral_id", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        Widget Mode
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> Optional[pulumi.Input[str]]:
        """
        When the widget was modified.
        """
        return pulumi.get(self, "modified_on")

    @modified_on.setter
    def modified_on(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_on", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
        to identify your widget, and where it is used.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def offlabel(self) -> Optional[pulumi.Input[bool]]:
        """
        Do not show any Cloudflare branding on the widget (ENT only).
        """
        return pulumi.get(self, "offlabel")

    @offlabel.setter
    def offlabel(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "offlabel", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region where this widget can be used.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        Secret key for this widget.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter
    def sitekey(self) -> Optional[pulumi.Input[str]]:
        """
        Widget item identifier tag.
        """
        return pulumi.get(self, "sitekey")

    @sitekey.setter
    def sitekey(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sitekey", value)


class TurnstileWidget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bot_fight_mode: Optional[pulumi.Input[bool]] = None,
                 clearance_level: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ephemeral_id: Optional[pulumi.Input[bool]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offlabel: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a TurnstileWidget resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[bool] bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
               (ENT only).
        :param pulumi.Input[str] clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
               determine the clearance level to be set
        :param pulumi.Input[bool] ephemeral_id: Return the Ephemeral ID in /siteverify (ENT only).
        :param pulumi.Input[str] mode: Widget Mode
        :param pulumi.Input[str] name: Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
               to identify your widget, and where it is used.
        :param pulumi.Input[bool] offlabel: Do not show any Cloudflare branding on the widget (ENT only).
        :param pulumi.Input[str] region: Region where this widget can be used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TurnstileWidgetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a TurnstileWidget resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param TurnstileWidgetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TurnstileWidgetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 bot_fight_mode: Optional[pulumi.Input[bool]] = None,
                 clearance_level: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ephemeral_id: Optional[pulumi.Input[bool]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offlabel: Optional[pulumi.Input[bool]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TurnstileWidgetArgs.__new__(TurnstileWidgetArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["bot_fight_mode"] = bot_fight_mode
            __props__.__dict__["clearance_level"] = clearance_level
            if domains is None and not opts.urn:
                raise TypeError("Missing required property 'domains'")
            __props__.__dict__["domains"] = domains
            __props__.__dict__["ephemeral_id"] = ephemeral_id
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            __props__.__dict__["name"] = name
            __props__.__dict__["offlabel"] = offlabel
            __props__.__dict__["region"] = region
            __props__.__dict__["created_on"] = None
            __props__.__dict__["modified_on"] = None
            __props__.__dict__["secret"] = None
            __props__.__dict__["sitekey"] = None
        super(TurnstileWidget, __self__).__init__(
            'cloudflare:index/turnstileWidget:TurnstileWidget',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            bot_fight_mode: Optional[pulumi.Input[bool]] = None,
            clearance_level: Optional[pulumi.Input[str]] = None,
            created_on: Optional[pulumi.Input[str]] = None,
            domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ephemeral_id: Optional[pulumi.Input[bool]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            modified_on: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            offlabel: Optional[pulumi.Input[bool]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            sitekey: Optional[pulumi.Input[str]] = None) -> 'TurnstileWidget':
        """
        Get an existing TurnstileWidget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Identifier
        :param pulumi.Input[bool] bot_fight_mode: If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
               (ENT only).
        :param pulumi.Input[str] clearance_level: If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
               determine the clearance level to be set
        :param pulumi.Input[str] created_on: When the widget was created.
        :param pulumi.Input[bool] ephemeral_id: Return the Ephemeral ID in /siteverify (ENT only).
        :param pulumi.Input[str] mode: Widget Mode
        :param pulumi.Input[str] modified_on: When the widget was modified.
        :param pulumi.Input[str] name: Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
               to identify your widget, and where it is used.
        :param pulumi.Input[bool] offlabel: Do not show any Cloudflare branding on the widget (ENT only).
        :param pulumi.Input[str] region: Region where this widget can be used.
        :param pulumi.Input[str] secret: Secret key for this widget.
        :param pulumi.Input[str] sitekey: Widget item identifier tag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TurnstileWidgetState.__new__(_TurnstileWidgetState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["bot_fight_mode"] = bot_fight_mode
        __props__.__dict__["clearance_level"] = clearance_level
        __props__.__dict__["created_on"] = created_on
        __props__.__dict__["domains"] = domains
        __props__.__dict__["ephemeral_id"] = ephemeral_id
        __props__.__dict__["mode"] = mode
        __props__.__dict__["modified_on"] = modified_on
        __props__.__dict__["name"] = name
        __props__.__dict__["offlabel"] = offlabel
        __props__.__dict__["region"] = region
        __props__.__dict__["secret"] = secret
        __props__.__dict__["sitekey"] = sitekey
        return TurnstileWidget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="botFightMode")
    def bot_fight_mode(self) -> pulumi.Output[bool]:
        """
        If bot_fight_mode is set to `true`, Cloudflare issues computationally expensive challenges in response to malicious bots
        (ENT only).
        """
        return pulumi.get(self, "bot_fight_mode")

    @property
    @pulumi.getter(name="clearanceLevel")
    def clearance_level(self) -> pulumi.Output[Optional[str]]:
        """
        If Turnstile is embedded on a Cloudflare site and the widget should grant challenge clearance, this setting can
        determine the clearance level to be set
        """
        return pulumi.get(self, "clearance_level")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        When the widget was created.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter(name="ephemeralId")
    def ephemeral_id(self) -> pulumi.Output[Optional[bool]]:
        """
        Return the Ephemeral ID in /siteverify (ENT only).
        """
        return pulumi.get(self, "ephemeral_id")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        Widget Mode
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[str]:
        """
        When the widget was modified.
        """
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Human readable widget name. Not unique. Cloudflare suggests that you set this to a meaningful string to make it easier
        to identify your widget, and where it is used.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def offlabel(self) -> pulumi.Output[bool]:
        """
        Do not show any Cloudflare branding on the widget (ENT only).
        """
        return pulumi.get(self, "offlabel")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Region where this widget can be used.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        Secret key for this widget.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def sitekey(self) -> pulumi.Output[str]:
        """
        Widget item identifier tag.
        """
        return pulumi.get(self, "sitekey")

