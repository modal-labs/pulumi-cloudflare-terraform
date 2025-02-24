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

__all__ = ['ObservatoryScheduledTestArgs', 'ObservatoryScheduledTest']

@pulumi.input_type
class ObservatoryScheduledTestArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 zone_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ObservatoryScheduledTest resource.
        :param pulumi.Input[str] url: A URL.
        :param pulumi.Input[str] zone_id: Identifier
        """
        pulumi.set(__self__, "url", url)
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        A URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

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


@pulumi.input_type
class _ObservatoryScheduledTestState:
    def __init__(__self__, *,
                 frequency: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 schedule: Optional[pulumi.Input['ObservatoryScheduledTestScheduleArgs']] = None,
                 test: Optional[pulumi.Input['ObservatoryScheduledTestTestArgs']] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ObservatoryScheduledTest resources.
        :param pulumi.Input[str] frequency: The frequency of the test.
        :param pulumi.Input[str] region: A test region.
        :param pulumi.Input['ObservatoryScheduledTestScheduleArgs'] schedule: The test schedule.
        :param pulumi.Input[str] url: A URL.
        :param pulumi.Input[str] zone_id: Identifier
        """
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if test is not None:
            pulumi.set(__self__, "test", test)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[str]]:
        """
        The frequency of the test.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        A test region.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input['ObservatoryScheduledTestScheduleArgs']]:
        """
        The test schedule.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input['ObservatoryScheduledTestScheduleArgs']]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter
    def test(self) -> Optional[pulumi.Input['ObservatoryScheduledTestTestArgs']]:
        return pulumi.get(self, "test")

    @test.setter
    def test(self, value: Optional[pulumi.Input['ObservatoryScheduledTestTestArgs']]):
        pulumi.set(self, "test", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        A URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

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


class ObservatoryScheduledTest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a ObservatoryScheduledTest resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] url: A URL.
        :param pulumi.Input[str] zone_id: Identifier
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ObservatoryScheduledTestArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ObservatoryScheduledTest resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ObservatoryScheduledTestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ObservatoryScheduledTestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ObservatoryScheduledTestArgs.__new__(ObservatoryScheduledTestArgs)

            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["frequency"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["schedule"] = None
            __props__.__dict__["test"] = None
        super(ObservatoryScheduledTest, __self__).__init__(
            'cloudflare:index/observatoryScheduledTest:ObservatoryScheduledTest',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            frequency: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            schedule: Optional[pulumi.Input[Union['ObservatoryScheduledTestScheduleArgs', 'ObservatoryScheduledTestScheduleArgsDict']]] = None,
            test: Optional[pulumi.Input[Union['ObservatoryScheduledTestTestArgs', 'ObservatoryScheduledTestTestArgsDict']]] = None,
            url: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ObservatoryScheduledTest':
        """
        Get an existing ObservatoryScheduledTest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] frequency: The frequency of the test.
        :param pulumi.Input[str] region: A test region.
        :param pulumi.Input[Union['ObservatoryScheduledTestScheduleArgs', 'ObservatoryScheduledTestScheduleArgsDict']] schedule: The test schedule.
        :param pulumi.Input[str] url: A URL.
        :param pulumi.Input[str] zone_id: Identifier
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ObservatoryScheduledTestState.__new__(_ObservatoryScheduledTestState)

        __props__.__dict__["frequency"] = frequency
        __props__.__dict__["region"] = region
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["test"] = test
        __props__.__dict__["url"] = url
        __props__.__dict__["zone_id"] = zone_id
        return ObservatoryScheduledTest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[str]:
        """
        The frequency of the test.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        A test region.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output['outputs.ObservatoryScheduledTestSchedule']:
        """
        The test schedule.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def test(self) -> pulumi.Output['outputs.ObservatoryScheduledTestTest']:
        return pulumi.get(self, "test")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        A URL.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        Identifier
        """
        return pulumi.get(self, "zone_id")

