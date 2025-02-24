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

__all__ = ['NotificationPolicyArgs', 'NotificationPolicy']

@pulumi.input_type
class NotificationPolicyArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 alert_type: pulumi.Input[str],
                 mechanisms: pulumi.Input['NotificationPolicyMechanismsArgs'],
                 alert_interval: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input['NotificationPolicyFiltersArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NotificationPolicy resource.
        :param pulumi.Input[str] account_id: The account id
        :param pulumi.Input[str] alert_type: Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
               then will give you a list of possible values.
        :param pulumi.Input['NotificationPolicyMechanismsArgs'] mechanisms: List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        :param pulumi.Input[str] alert_interval: Optional specification of how often to re-alert from the same incident, not support on all alert types.
        :param pulumi.Input[str] description: Optional description for the Notification policy.
        :param pulumi.Input[bool] enabled: Whether or not the Notification policy is enabled.
        :param pulumi.Input['NotificationPolicyFiltersArgs'] filters: Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
               This is only available for select alert types. See alert type documentation for more details.
        :param pulumi.Input[str] name: Name of the policy.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "alert_type", alert_type)
        pulumi.set(__self__, "mechanisms", mechanisms)
        if alert_interval is not None:
            pulumi.set(__self__, "alert_interval", alert_interval)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        The account id
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> pulumi.Input[str]:
        """
        Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
        then will give you a list of possible values.
        """
        return pulumi.get(self, "alert_type")

    @alert_type.setter
    def alert_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_type", value)

    @property
    @pulumi.getter
    def mechanisms(self) -> pulumi.Input['NotificationPolicyMechanismsArgs']:
        """
        List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        """
        return pulumi.get(self, "mechanisms")

    @mechanisms.setter
    def mechanisms(self, value: pulumi.Input['NotificationPolicyMechanismsArgs']):
        pulumi.set(self, "mechanisms", value)

    @property
    @pulumi.getter(name="alertInterval")
    def alert_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Optional specification of how often to re-alert from the same incident, not support on all alert types.
        """
        return pulumi.get(self, "alert_interval")

    @alert_interval.setter
    def alert_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_interval", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional description for the Notification policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the Notification policy is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['NotificationPolicyFiltersArgs']]:
        """
        Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
        This is only available for select alert types. See alert type documentation for more details.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['NotificationPolicyFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NotificationPolicyState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alert_interval: Optional[pulumi.Input[str]] = None,
                 alert_type: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input['NotificationPolicyFiltersArgs']] = None,
                 mechanisms: Optional[pulumi.Input['NotificationPolicyMechanismsArgs']] = None,
                 modified: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NotificationPolicy resources.
        :param pulumi.Input[str] account_id: The account id
        :param pulumi.Input[str] alert_interval: Optional specification of how often to re-alert from the same incident, not support on all alert types.
        :param pulumi.Input[str] alert_type: Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
               then will give you a list of possible values.
        :param pulumi.Input[str] description: Optional description for the Notification policy.
        :param pulumi.Input[bool] enabled: Whether or not the Notification policy is enabled.
        :param pulumi.Input['NotificationPolicyFiltersArgs'] filters: Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
               This is only available for select alert types. See alert type documentation for more details.
        :param pulumi.Input['NotificationPolicyMechanismsArgs'] mechanisms: List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        :param pulumi.Input[str] name: Name of the policy.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if alert_interval is not None:
            pulumi.set(__self__, "alert_interval", alert_interval)
        if alert_type is not None:
            pulumi.set(__self__, "alert_type", alert_type)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if mechanisms is not None:
            pulumi.set(__self__, "mechanisms", mechanisms)
        if modified is not None:
            pulumi.set(__self__, "modified", modified)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account id
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="alertInterval")
    def alert_interval(self) -> Optional[pulumi.Input[str]]:
        """
        Optional specification of how often to re-alert from the same incident, not support on all alert types.
        """
        return pulumi.get(self, "alert_interval")

    @alert_interval.setter
    def alert_interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_interval", value)

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> Optional[pulumi.Input[str]]:
        """
        Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
        then will give you a list of possible values.
        """
        return pulumi.get(self, "alert_type")

    @alert_type.setter
    def alert_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_type", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional description for the Notification policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not the Notification policy is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input['NotificationPolicyFiltersArgs']]:
        """
        Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
        This is only available for select alert types. See alert type documentation for more details.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input['NotificationPolicyFiltersArgs']]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def mechanisms(self) -> Optional[pulumi.Input['NotificationPolicyMechanismsArgs']]:
        """
        List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        """
        return pulumi.get(self, "mechanisms")

    @mechanisms.setter
    def mechanisms(self, value: Optional[pulumi.Input['NotificationPolicyMechanismsArgs']]):
        pulumi.set(self, "mechanisms", value)

    @property
    @pulumi.getter
    def modified(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "modified")

    @modified.setter
    def modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class NotificationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alert_interval: Optional[pulumi.Input[str]] = None,
                 alert_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[Union['NotificationPolicyFiltersArgs', 'NotificationPolicyFiltersArgsDict']]] = None,
                 mechanisms: Optional[pulumi.Input[Union['NotificationPolicyMechanismsArgs', 'NotificationPolicyMechanismsArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a NotificationPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account id
        :param pulumi.Input[str] alert_interval: Optional specification of how often to re-alert from the same incident, not support on all alert types.
        :param pulumi.Input[str] alert_type: Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
               then will give you a list of possible values.
        :param pulumi.Input[str] description: Optional description for the Notification policy.
        :param pulumi.Input[bool] enabled: Whether or not the Notification policy is enabled.
        :param pulumi.Input[Union['NotificationPolicyFiltersArgs', 'NotificationPolicyFiltersArgsDict']] filters: Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
               This is only available for select alert types. See alert type documentation for more details.
        :param pulumi.Input[Union['NotificationPolicyMechanismsArgs', 'NotificationPolicyMechanismsArgsDict']] mechanisms: List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        :param pulumi.Input[str] name: Name of the policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotificationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a NotificationPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param NotificationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotificationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 alert_interval: Optional[pulumi.Input[str]] = None,
                 alert_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 filters: Optional[pulumi.Input[Union['NotificationPolicyFiltersArgs', 'NotificationPolicyFiltersArgsDict']]] = None,
                 mechanisms: Optional[pulumi.Input[Union['NotificationPolicyMechanismsArgs', 'NotificationPolicyMechanismsArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotificationPolicyArgs.__new__(NotificationPolicyArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["alert_interval"] = alert_interval
            if alert_type is None and not opts.urn:
                raise TypeError("Missing required property 'alert_type'")
            __props__.__dict__["alert_type"] = alert_type
            __props__.__dict__["description"] = description
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["filters"] = filters
            if mechanisms is None and not opts.urn:
                raise TypeError("Missing required property 'mechanisms'")
            __props__.__dict__["mechanisms"] = mechanisms
            __props__.__dict__["name"] = name
            __props__.__dict__["created"] = None
            __props__.__dict__["modified"] = None
        super(NotificationPolicy, __self__).__init__(
            'cloudflare:index/notificationPolicy:NotificationPolicy',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            alert_interval: Optional[pulumi.Input[str]] = None,
            alert_type: Optional[pulumi.Input[str]] = None,
            created: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            filters: Optional[pulumi.Input[Union['NotificationPolicyFiltersArgs', 'NotificationPolicyFiltersArgsDict']]] = None,
            mechanisms: Optional[pulumi.Input[Union['NotificationPolicyMechanismsArgs', 'NotificationPolicyMechanismsArgsDict']]] = None,
            modified: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'NotificationPolicy':
        """
        Get an existing NotificationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account id
        :param pulumi.Input[str] alert_interval: Optional specification of how often to re-alert from the same incident, not support on all alert types.
        :param pulumi.Input[str] alert_type: Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
               then will give you a list of possible values.
        :param pulumi.Input[str] description: Optional description for the Notification policy.
        :param pulumi.Input[bool] enabled: Whether or not the Notification policy is enabled.
        :param pulumi.Input[Union['NotificationPolicyFiltersArgs', 'NotificationPolicyFiltersArgsDict']] filters: Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
               This is only available for select alert types. See alert type documentation for more details.
        :param pulumi.Input[Union['NotificationPolicyMechanismsArgs', 'NotificationPolicyMechanismsArgsDict']] mechanisms: List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        :param pulumi.Input[str] name: Name of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotificationPolicyState.__new__(_NotificationPolicyState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["alert_interval"] = alert_interval
        __props__.__dict__["alert_type"] = alert_type
        __props__.__dict__["created"] = created
        __props__.__dict__["description"] = description
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["filters"] = filters
        __props__.__dict__["mechanisms"] = mechanisms
        __props__.__dict__["modified"] = modified
        __props__.__dict__["name"] = name
        return NotificationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account id
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="alertInterval")
    def alert_interval(self) -> pulumi.Output[Optional[str]]:
        """
        Optional specification of how often to re-alert from the same incident, not support on all alert types.
        """
        return pulumi.get(self, "alert_interval")

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> pulumi.Output[str]:
        """
        Refers to which event will trigger a Notification dispatch. You can use the endpoint to get available alert types which
        then will give you a list of possible values.
        """
        return pulumi.get(self, "alert_type")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Optional description for the Notification policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether or not the Notification policy is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output['outputs.NotificationPolicyFilters']:
        """
        Optional filters that allow you to be alerted only on a subset of events for that alert type based on some criteria.
        This is only available for select alert types. See alert type documentation for more details.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def mechanisms(self) -> pulumi.Output['outputs.NotificationPolicyMechanisms']:
        """
        List of IDs that will be used when dispatching a notification. IDs for email type will be the email address.
        """
        return pulumi.get(self, "mechanisms")

    @property
    @pulumi.getter
    def modified(self) -> pulumi.Output[str]:
        return pulumi.get(self, "modified")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the policy.
        """
        return pulumi.get(self, "name")

