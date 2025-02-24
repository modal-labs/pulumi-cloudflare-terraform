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

__all__ = ['ApiShieldSchemaValidationSettingsArgs', 'ApiShieldSchemaValidationSettings']

@pulumi.input_type
class ApiShieldSchemaValidationSettingsArgs:
    def __init__(__self__, *,
                 validation_default_mitigation_action: pulumi.Input[str],
                 zone_id: pulumi.Input[str],
                 validation_override_mitigation_action: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ApiShieldSchemaValidationSettings resource.
        :param pulumi.Input[str] validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
               follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
               does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
               when there is no mitigation action defined on the operation
        :param pulumi.Input[str] zone_id: Identifier
        :param pulumi.Input[str] validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
               validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
               special value `disable_override` or `null`
        """
        pulumi.set(__self__, "validation_default_mitigation_action", validation_default_mitigation_action)
        pulumi.set(__self__, "zone_id", zone_id)
        if validation_override_mitigation_action is not None:
            pulumi.set(__self__, "validation_override_mitigation_action", validation_override_mitigation_action)

    @property
    @pulumi.getter(name="validationDefaultMitigationAction")
    def validation_default_mitigation_action(self) -> pulumi.Input[str]:
        """
        The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
        follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
        does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
        when there is no mitigation action defined on the operation
        """
        return pulumi.get(self, "validation_default_mitigation_action")

    @validation_default_mitigation_action.setter
    def validation_default_mitigation_action(self, value: pulumi.Input[str]):
        pulumi.set(self, "validation_default_mitigation_action", value)

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
    @pulumi.getter(name="validationOverrideMitigationAction")
    def validation_override_mitigation_action(self) -> Optional[pulumi.Input[str]]:
        """
        When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
        validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
        special value `disable_override` or `null`
        """
        return pulumi.get(self, "validation_override_mitigation_action")

    @validation_override_mitigation_action.setter
    def validation_override_mitigation_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_override_mitigation_action", value)


@pulumi.input_type
class _ApiShieldSchemaValidationSettingsState:
    def __init__(__self__, *,
                 validation_default_mitigation_action: Optional[pulumi.Input[str]] = None,
                 validation_override_mitigation_action: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ApiShieldSchemaValidationSettings resources.
        :param pulumi.Input[str] validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
               follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
               does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
               when there is no mitigation action defined on the operation
        :param pulumi.Input[str] validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
               validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
               special value `disable_override` or `null`
        :param pulumi.Input[str] zone_id: Identifier
        """
        if validation_default_mitigation_action is not None:
            pulumi.set(__self__, "validation_default_mitigation_action", validation_default_mitigation_action)
        if validation_override_mitigation_action is not None:
            pulumi.set(__self__, "validation_override_mitigation_action", validation_override_mitigation_action)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="validationDefaultMitigationAction")
    def validation_default_mitigation_action(self) -> Optional[pulumi.Input[str]]:
        """
        The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
        follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
        does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
        when there is no mitigation action defined on the operation
        """
        return pulumi.get(self, "validation_default_mitigation_action")

    @validation_default_mitigation_action.setter
    def validation_default_mitigation_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_default_mitigation_action", value)

    @property
    @pulumi.getter(name="validationOverrideMitigationAction")
    def validation_override_mitigation_action(self) -> Optional[pulumi.Input[str]]:
        """
        When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
        validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
        special value `disable_override` or `null`
        """
        return pulumi.get(self, "validation_override_mitigation_action")

    @validation_override_mitigation_action.setter
    def validation_override_mitigation_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "validation_override_mitigation_action", value)

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


class ApiShieldSchemaValidationSettings(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 validation_default_mitigation_action: Optional[pulumi.Input[str]] = None,
                 validation_override_mitigation_action: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ApiShieldSchemaValidationSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
               follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
               does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
               when there is no mitigation action defined on the operation
        :param pulumi.Input[str] validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
               validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
               special value `disable_override` or `null`
        :param pulumi.Input[str] zone_id: Identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiShieldSchemaValidationSettingsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ApiShieldSchemaValidationSettings resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ApiShieldSchemaValidationSettingsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiShieldSchemaValidationSettingsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 validation_default_mitigation_action: Optional[pulumi.Input[str]] = None,
                 validation_override_mitigation_action: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiShieldSchemaValidationSettingsArgs.__new__(ApiShieldSchemaValidationSettingsArgs)

            if validation_default_mitigation_action is None and not opts.urn:
                raise TypeError("Missing required property 'validation_default_mitigation_action'")
            __props__.__dict__["validation_default_mitigation_action"] = validation_default_mitigation_action
            __props__.__dict__["validation_override_mitigation_action"] = validation_override_mitigation_action
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(ApiShieldSchemaValidationSettings, __self__).__init__(
            'cloudflare:index/apiShieldSchemaValidationSettings:ApiShieldSchemaValidationSettings',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            validation_default_mitigation_action: Optional[pulumi.Input[str]] = None,
            validation_override_mitigation_action: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ApiShieldSchemaValidationSettings':
        """
        Get an existing ApiShieldSchemaValidationSettings resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] validation_default_mitigation_action: The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
               follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
               does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
               when there is no mitigation action defined on the operation
        :param pulumi.Input[str] validation_override_mitigation_action: When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
               validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
               special value `disable_override` or `null`
        :param pulumi.Input[str] zone_id: Identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ApiShieldSchemaValidationSettingsState.__new__(_ApiShieldSchemaValidationSettingsState)

        __props__.__dict__["validation_default_mitigation_action"] = validation_default_mitigation_action
        __props__.__dict__["validation_override_mitigation_action"] = validation_override_mitigation_action
        __props__.__dict__["zone_id"] = zone_id
        return ApiShieldSchemaValidationSettings(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="validationDefaultMitigationAction")
    def validation_default_mitigation_action(self) -> pulumi.Output[str]:
        """
        The default mitigation action used when there is no mitigation action defined on the operation Mitigation actions are as
        follows: * `log` - log request when request does not conform to schema * `block` - deny access to the site when request
        does not conform to schema A special value of of `none` will skip running schema validation entirely for the request
        when there is no mitigation action defined on the operation
        """
        return pulumi.get(self, "validation_default_mitigation_action")

    @property
    @pulumi.getter(name="validationOverrideMitigationAction")
    def validation_override_mitigation_action(self) -> pulumi.Output[Optional[str]]:
        """
        When set, this overrides both zone level and operation level mitigation actions. - `none` will skip running schema
        validation entirely for the request - `null` indicates that no override is in place To clear any override, use the
        special value `disable_override` or `null`
        """
        return pulumi.get(self, "validation_override_mitigation_action")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

