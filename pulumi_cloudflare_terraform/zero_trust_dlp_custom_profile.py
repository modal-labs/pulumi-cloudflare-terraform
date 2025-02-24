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

__all__ = ['ZeroTrustDlpCustomProfileArgs', 'ZeroTrustDlpCustomProfile']

@pulumi.input_type
class ZeroTrustDlpCustomProfileArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 ai_context_enabled: Optional[pulumi.Input[bool]] = None,
                 allowed_match_count: Optional[pulumi.Input[float]] = None,
                 confidence_threshold: Optional[pulumi.Input[str]] = None,
                 context_awareness: Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocr_enabled: Optional[pulumi.Input[bool]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]] = None,
                 shared_entries: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]] = None):
        """
        The set of arguments for constructing a ZeroTrustDlpCustomProfile resource.
        :param pulumi.Input[float] allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.
        :param pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs'] context_awareness: Scan the context of predefined entries to only return matches surrounded by keywords.
        :param pulumi.Input[str] description: The description of the profile
        :param pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]] shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        """
        pulumi.set(__self__, "account_id", account_id)
        if ai_context_enabled is not None:
            pulumi.set(__self__, "ai_context_enabled", ai_context_enabled)
        if allowed_match_count is not None:
            pulumi.set(__self__, "allowed_match_count", allowed_match_count)
        if confidence_threshold is not None:
            pulumi.set(__self__, "confidence_threshold", confidence_threshold)
        if context_awareness is not None:
            pulumi.set(__self__, "context_awareness", context_awareness)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ocr_enabled is not None:
            pulumi.set(__self__, "ocr_enabled", ocr_enabled)
        if profiles is not None:
            pulumi.set(__self__, "profiles", profiles)
        if shared_entries is not None:
            pulumi.set(__self__, "shared_entries", shared_entries)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="aiContextEnabled")
    def ai_context_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ai_context_enabled")

    @ai_context_enabled.setter
    def ai_context_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ai_context_enabled", value)

    @property
    @pulumi.getter(name="allowedMatchCount")
    def allowed_match_count(self) -> Optional[pulumi.Input[float]]:
        """
        Related DLP policies will trigger when the match count exceeds the number set.
        """
        return pulumi.get(self, "allowed_match_count")

    @allowed_match_count.setter
    def allowed_match_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "allowed_match_count", value)

    @property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "confidence_threshold")

    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "confidence_threshold", value)

    @property
    @pulumi.getter(name="contextAwareness")
    def context_awareness(self) -> Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']]:
        """
        Scan the context of predefined entries to only return matches surrounded by keywords.
        """
        return pulumi.get(self, "context_awareness")

    @context_awareness.setter
    def context_awareness(self, value: Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']]):
        pulumi.set(self, "context_awareness", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the profile
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]]:
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ocrEnabled")
    def ocr_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ocr_enabled")

    @ocr_enabled.setter
    def ocr_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ocr_enabled", value)

    @property
    @pulumi.getter
    def profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]]:
        return pulumi.get(self, "profiles")

    @profiles.setter
    def profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]]):
        pulumi.set(self, "profiles", value)

    @property
    @pulumi.getter(name="sharedEntries")
    def shared_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]]:
        """
        Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        """
        return pulumi.get(self, "shared_entries")

    @shared_entries.setter
    def shared_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]]):
        pulumi.set(self, "shared_entries", value)


@pulumi.input_type
class _ZeroTrustDlpCustomProfileState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ai_context_enabled: Optional[pulumi.Input[bool]] = None,
                 allowed_match_count: Optional[pulumi.Input[float]] = None,
                 confidence_threshold: Optional[pulumi.Input[str]] = None,
                 context_awareness: Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocr_enabled: Optional[pulumi.Input[bool]] = None,
                 open_access: Optional[pulumi.Input[bool]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]] = None,
                 shared_entries: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ZeroTrustDlpCustomProfile resources.
        :param pulumi.Input[float] allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.
        :param pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs'] context_awareness: Scan the context of predefined entries to only return matches surrounded by keywords.
        :param pulumi.Input[str] created_at: When the profile was created
        :param pulumi.Input[str] description: The description of the profile
        :param pulumi.Input[bool] open_access: Whether this profile can be accessed by anyone
        :param pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]] shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        :param pulumi.Input[str] updated_at: When the profile was lasted updated
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if ai_context_enabled is not None:
            pulumi.set(__self__, "ai_context_enabled", ai_context_enabled)
        if allowed_match_count is not None:
            pulumi.set(__self__, "allowed_match_count", allowed_match_count)
        if confidence_threshold is not None:
            pulumi.set(__self__, "confidence_threshold", confidence_threshold)
        if context_awareness is not None:
            pulumi.set(__self__, "context_awareness", context_awareness)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if entries is not None:
            pulumi.set(__self__, "entries", entries)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ocr_enabled is not None:
            pulumi.set(__self__, "ocr_enabled", ocr_enabled)
        if open_access is not None:
            pulumi.set(__self__, "open_access", open_access)
        if profiles is not None:
            pulumi.set(__self__, "profiles", profiles)
        if shared_entries is not None:
            pulumi.set(__self__, "shared_entries", shared_entries)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="aiContextEnabled")
    def ai_context_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ai_context_enabled")

    @ai_context_enabled.setter
    def ai_context_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ai_context_enabled", value)

    @property
    @pulumi.getter(name="allowedMatchCount")
    def allowed_match_count(self) -> Optional[pulumi.Input[float]]:
        """
        Related DLP policies will trigger when the match count exceeds the number set.
        """
        return pulumi.get(self, "allowed_match_count")

    @allowed_match_count.setter
    def allowed_match_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "allowed_match_count", value)

    @property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "confidence_threshold")

    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "confidence_threshold", value)

    @property
    @pulumi.getter(name="contextAwareness")
    def context_awareness(self) -> Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']]:
        """
        Scan the context of predefined entries to only return matches surrounded by keywords.
        """
        return pulumi.get(self, "context_awareness")

    @context_awareness.setter
    def context_awareness(self, value: Optional[pulumi.Input['ZeroTrustDlpCustomProfileContextAwarenessArgs']]):
        pulumi.set(self, "context_awareness", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the profile was created
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the profile
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]]:
        return pulumi.get(self, "entries")

    @entries.setter
    def entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileEntryArgs']]]]):
        pulumi.set(self, "entries", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ocrEnabled")
    def ocr_enabled(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "ocr_enabled")

    @ocr_enabled.setter
    def ocr_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ocr_enabled", value)

    @property
    @pulumi.getter(name="openAccess")
    def open_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this profile can be accessed by anyone
        """
        return pulumi.get(self, "open_access")

    @open_access.setter
    def open_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "open_access", value)

    @property
    @pulumi.getter
    def profiles(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]]:
        return pulumi.get(self, "profiles")

    @profiles.setter
    def profiles(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileProfileArgs']]]]):
        pulumi.set(self, "profiles", value)

    @property
    @pulumi.getter(name="sharedEntries")
    def shared_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]]:
        """
        Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        """
        return pulumi.get(self, "shared_entries")

    @shared_entries.setter
    def shared_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZeroTrustDlpCustomProfileSharedEntryArgs']]]]):
        pulumi.set(self, "shared_entries", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        When the profile was lasted updated
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class ZeroTrustDlpCustomProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ai_context_enabled: Optional[pulumi.Input[bool]] = None,
                 allowed_match_count: Optional[pulumi.Input[float]] = None,
                 confidence_threshold: Optional[pulumi.Input[str]] = None,
                 context_awareness: Optional[pulumi.Input[Union['ZeroTrustDlpCustomProfileContextAwarenessArgs', 'ZeroTrustDlpCustomProfileContextAwarenessArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileEntryArgs', 'ZeroTrustDlpCustomProfileEntryArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocr_enabled: Optional[pulumi.Input[bool]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileProfileArgs', 'ZeroTrustDlpCustomProfileProfileArgsDict']]]]] = None,
                 shared_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileSharedEntryArgs', 'ZeroTrustDlpCustomProfileSharedEntryArgsDict']]]]] = None,
                 __props__=None):
        """
        Create a ZeroTrustDlpCustomProfile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.
        :param pulumi.Input[Union['ZeroTrustDlpCustomProfileContextAwarenessArgs', 'ZeroTrustDlpCustomProfileContextAwarenessArgsDict']] context_awareness: Scan the context of predefined entries to only return matches surrounded by keywords.
        :param pulumi.Input[str] description: The description of the profile
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileSharedEntryArgs', 'ZeroTrustDlpCustomProfileSharedEntryArgsDict']]]] shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ZeroTrustDlpCustomProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ZeroTrustDlpCustomProfile resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ZeroTrustDlpCustomProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZeroTrustDlpCustomProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 ai_context_enabled: Optional[pulumi.Input[bool]] = None,
                 allowed_match_count: Optional[pulumi.Input[float]] = None,
                 confidence_threshold: Optional[pulumi.Input[str]] = None,
                 context_awareness: Optional[pulumi.Input[Union['ZeroTrustDlpCustomProfileContextAwarenessArgs', 'ZeroTrustDlpCustomProfileContextAwarenessArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileEntryArgs', 'ZeroTrustDlpCustomProfileEntryArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ocr_enabled: Optional[pulumi.Input[bool]] = None,
                 profiles: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileProfileArgs', 'ZeroTrustDlpCustomProfileProfileArgsDict']]]]] = None,
                 shared_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileSharedEntryArgs', 'ZeroTrustDlpCustomProfileSharedEntryArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZeroTrustDlpCustomProfileArgs.__new__(ZeroTrustDlpCustomProfileArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["ai_context_enabled"] = ai_context_enabled
            __props__.__dict__["allowed_match_count"] = allowed_match_count
            __props__.__dict__["confidence_threshold"] = confidence_threshold
            __props__.__dict__["context_awareness"] = context_awareness
            __props__.__dict__["description"] = description
            __props__.__dict__["entries"] = entries
            __props__.__dict__["name"] = name
            __props__.__dict__["ocr_enabled"] = ocr_enabled
            __props__.__dict__["profiles"] = profiles
            __props__.__dict__["shared_entries"] = shared_entries
            __props__.__dict__["created_at"] = None
            __props__.__dict__["open_access"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        super(ZeroTrustDlpCustomProfile, __self__).__init__(
            'cloudflare:index/zeroTrustDlpCustomProfile:ZeroTrustDlpCustomProfile',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            ai_context_enabled: Optional[pulumi.Input[bool]] = None,
            allowed_match_count: Optional[pulumi.Input[float]] = None,
            confidence_threshold: Optional[pulumi.Input[str]] = None,
            context_awareness: Optional[pulumi.Input[Union['ZeroTrustDlpCustomProfileContextAwarenessArgs', 'ZeroTrustDlpCustomProfileContextAwarenessArgsDict']]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileEntryArgs', 'ZeroTrustDlpCustomProfileEntryArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ocr_enabled: Optional[pulumi.Input[bool]] = None,
            open_access: Optional[pulumi.Input[bool]] = None,
            profiles: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileProfileArgs', 'ZeroTrustDlpCustomProfileProfileArgsDict']]]]] = None,
            shared_entries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileSharedEntryArgs', 'ZeroTrustDlpCustomProfileSharedEntryArgsDict']]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'ZeroTrustDlpCustomProfile':
        """
        Get an existing ZeroTrustDlpCustomProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] allowed_match_count: Related DLP policies will trigger when the match count exceeds the number set.
        :param pulumi.Input[Union['ZeroTrustDlpCustomProfileContextAwarenessArgs', 'ZeroTrustDlpCustomProfileContextAwarenessArgsDict']] context_awareness: Scan the context of predefined entries to only return matches surrounded by keywords.
        :param pulumi.Input[str] created_at: When the profile was created
        :param pulumi.Input[str] description: The description of the profile
        :param pulumi.Input[bool] open_access: Whether this profile can be accessed by anyone
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZeroTrustDlpCustomProfileSharedEntryArgs', 'ZeroTrustDlpCustomProfileSharedEntryArgsDict']]]] shared_entries: Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        :param pulumi.Input[str] updated_at: When the profile was lasted updated
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZeroTrustDlpCustomProfileState.__new__(_ZeroTrustDlpCustomProfileState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["ai_context_enabled"] = ai_context_enabled
        __props__.__dict__["allowed_match_count"] = allowed_match_count
        __props__.__dict__["confidence_threshold"] = confidence_threshold
        __props__.__dict__["context_awareness"] = context_awareness
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["description"] = description
        __props__.__dict__["entries"] = entries
        __props__.__dict__["name"] = name
        __props__.__dict__["ocr_enabled"] = ocr_enabled
        __props__.__dict__["open_access"] = open_access
        __props__.__dict__["profiles"] = profiles
        __props__.__dict__["shared_entries"] = shared_entries
        __props__.__dict__["type"] = type
        __props__.__dict__["updated_at"] = updated_at
        return ZeroTrustDlpCustomProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="aiContextEnabled")
    def ai_context_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "ai_context_enabled")

    @property
    @pulumi.getter(name="allowedMatchCount")
    def allowed_match_count(self) -> pulumi.Output[float]:
        """
        Related DLP policies will trigger when the match count exceeds the number set.
        """
        return pulumi.get(self, "allowed_match_count")

    @property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "confidence_threshold")

    @property
    @pulumi.getter(name="contextAwareness")
    def context_awareness(self) -> pulumi.Output['outputs.ZeroTrustDlpCustomProfileContextAwareness']:
        """
        Scan the context of predefined entries to only return matches surrounded by keywords.
        """
        return pulumi.get(self, "context_awareness")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        When the profile was created
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the profile
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def entries(self) -> pulumi.Output[Sequence['outputs.ZeroTrustDlpCustomProfileEntry']]:
        return pulumi.get(self, "entries")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ocrEnabled")
    def ocr_enabled(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "ocr_enabled")

    @property
    @pulumi.getter(name="openAccess")
    def open_access(self) -> pulumi.Output[bool]:
        """
        Whether this profile can be accessed by anyone
        """
        return pulumi.get(self, "open_access")

    @property
    @pulumi.getter
    def profiles(self) -> pulumi.Output[Sequence['outputs.ZeroTrustDlpCustomProfileProfile']]:
        return pulumi.get(self, "profiles")

    @property
    @pulumi.getter(name="sharedEntries")
    def shared_entries(self) -> pulumi.Output[Sequence['outputs.ZeroTrustDlpCustomProfileSharedEntry']]:
        """
        Entries from other profiles (e.g. pre-defined Cloudflare profiles, or your Microsoft Information Protection profiles).
        """
        return pulumi.get(self, "shared_entries")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        When the profile was lasted updated
        """
        return pulumi.get(self, "updated_at")

