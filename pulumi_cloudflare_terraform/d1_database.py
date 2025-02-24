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

__all__ = ['D1DatabaseArgs', 'D1Database']

@pulumi.input_type
class D1DatabaseArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 primary_location_hint: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a D1Database resource.
        :param pulumi.Input[str] account_id: Account identifier tag.
        :param pulumi.Input[str] name: D1 database name.
        :param pulumi.Input[str] primary_location_hint: Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
               possible to the current user.
        """
        pulumi.set(__self__, "account_id", account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if primary_location_hint is not None:
            pulumi.set(__self__, "primary_location_hint", primary_location_hint)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Account identifier tag.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        D1 database name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="primaryLocationHint")
    def primary_location_hint(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
        possible to the current user.
        """
        return pulumi.get(self, "primary_location_hint")

    @primary_location_hint.setter
    def primary_location_hint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_location_hint", value)


@pulumi.input_type
class _D1DatabaseState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 file_size: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 num_tables: Optional[pulumi.Input[float]] = None,
                 primary_location_hint: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering D1Database resources.
        :param pulumi.Input[str] account_id: Account identifier tag.
        :param pulumi.Input[str] created_at: Specifies the timestamp the resource was created as an ISO8601 string.
        :param pulumi.Input[float] file_size: The D1 database's size, in bytes.
        :param pulumi.Input[str] name: D1 database name.
        :param pulumi.Input[str] primary_location_hint: Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
               possible to the current user.
        :param pulumi.Input[str] uuid: D1 database identifier (UUID).
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if file_size is not None:
            pulumi.set(__self__, "file_size", file_size)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if num_tables is not None:
            pulumi.set(__self__, "num_tables", num_tables)
        if primary_location_hint is not None:
            pulumi.set(__self__, "primary_location_hint", primary_location_hint)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account identifier tag.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the timestamp the resource was created as an ISO8601 string.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[pulumi.Input[float]]:
        """
        The D1 database's size, in bytes.
        """
        return pulumi.get(self, "file_size")

    @file_size.setter
    def file_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "file_size", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        D1 database name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="numTables")
    def num_tables(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "num_tables")

    @num_tables.setter
    def num_tables(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "num_tables", value)

    @property
    @pulumi.getter(name="primaryLocationHint")
    def primary_location_hint(self) -> Optional[pulumi.Input[str]]:
        """
        Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
        possible to the current user.
        """
        return pulumi.get(self, "primary_location_hint")

    @primary_location_hint.setter
    def primary_location_hint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_location_hint", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        D1 database identifier (UUID).
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class D1Database(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_location_hint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a D1Database resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier tag.
        :param pulumi.Input[str] name: D1 database name.
        :param pulumi.Input[str] primary_location_hint: Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
               possible to the current user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: D1DatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a D1Database resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param D1DatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(D1DatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 primary_location_hint: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = D1DatabaseArgs.__new__(D1DatabaseArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["name"] = name
            __props__.__dict__["primary_location_hint"] = primary_location_hint
            __props__.__dict__["created_at"] = None
            __props__.__dict__["file_size"] = None
            __props__.__dict__["num_tables"] = None
            __props__.__dict__["uuid"] = None
            __props__.__dict__["version"] = None
        super(D1Database, __self__).__init__(
            'cloudflare:index/d1Database:D1Database',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            file_size: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            num_tables: Optional[pulumi.Input[float]] = None,
            primary_location_hint: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'D1Database':
        """
        Get an existing D1Database resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Account identifier tag.
        :param pulumi.Input[str] created_at: Specifies the timestamp the resource was created as an ISO8601 string.
        :param pulumi.Input[float] file_size: The D1 database's size, in bytes.
        :param pulumi.Input[str] name: D1 database name.
        :param pulumi.Input[str] primary_location_hint: Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
               possible to the current user.
        :param pulumi.Input[str] uuid: D1 database identifier (UUID).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _D1DatabaseState.__new__(_D1DatabaseState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["file_size"] = file_size
        __props__.__dict__["name"] = name
        __props__.__dict__["num_tables"] = num_tables
        __props__.__dict__["primary_location_hint"] = primary_location_hint
        __props__.__dict__["uuid"] = uuid
        __props__.__dict__["version"] = version
        return D1Database(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Account identifier tag.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Specifies the timestamp the resource was created as an ISO8601 string.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> pulumi.Output[float]:
        """
        The D1 database's size, in bytes.
        """
        return pulumi.get(self, "file_size")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        D1 database name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numTables")
    def num_tables(self) -> pulumi.Output[float]:
        return pulumi.get(self, "num_tables")

    @property
    @pulumi.getter(name="primaryLocationHint")
    def primary_location_hint(self) -> pulumi.Output[Optional[str]]:
        """
        Specify the region to create the D1 primary, if available. If this option is omitted, the D1 will be created as close as
        possible to the current user.
        """
        return pulumi.get(self, "primary_location_hint")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        D1 database identifier (UUID).
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "version")

