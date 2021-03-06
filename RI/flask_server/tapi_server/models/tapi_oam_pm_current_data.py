# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_common_local_class import TapiCommonLocalClass  # noqa: F401,E501
from tapi_server.models.tapi_common_name_and_value import TapiCommonNameAndValue  # noqa: F401,E501
from tapi_server.models.tapi_common_time_interval import TapiCommonTimeInterval  # noqa: F401,E501
from tapi_server.models.tapi_common_time_period import TapiCommonTimePeriod  # noqa: F401,E501
from tapi_server.models.tapi_oam_pm_history_data import TapiOamPmHistoryData  # noqa: F401,E501
from tapi_server import util


class TapiOamPmCurrentData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, local_id=None, elapsed_time=None, pm_history_data=None, granularity_period=None, suspect_interval_flag=False, timestamp=None):  # noqa: E501
        """TapiOamPmCurrentData - a model defined in OpenAPI

        :param name: The name of this TapiOamPmCurrentData.  # noqa: E501
        :type name: List[TapiCommonNameAndValue]
        :param local_id: The local_id of this TapiOamPmCurrentData.  # noqa: E501
        :type local_id: str
        :param elapsed_time: The elapsed_time of this TapiOamPmCurrentData.  # noqa: E501
        :type elapsed_time: TapiCommonTimeInterval
        :param pm_history_data: The pm_history_data of this TapiOamPmCurrentData.  # noqa: E501
        :type pm_history_data: List[TapiOamPmHistoryData]
        :param granularity_period: The granularity_period of this TapiOamPmCurrentData.  # noqa: E501
        :type granularity_period: TapiCommonTimePeriod
        :param suspect_interval_flag: The suspect_interval_flag of this TapiOamPmCurrentData.  # noqa: E501
        :type suspect_interval_flag: bool
        :param timestamp: The timestamp of this TapiOamPmCurrentData.  # noqa: E501
        :type timestamp: str
        """
        self.openapi_types = {
            'name': List[TapiCommonNameAndValue],
            'local_id': str,
            'elapsed_time': TapiCommonTimeInterval,
            'pm_history_data': List[TapiOamPmHistoryData],
            'granularity_period': TapiCommonTimePeriod,
            'suspect_interval_flag': bool,
            'timestamp': str
        }

        self.attribute_map = {
            'name': 'name',
            'local_id': 'local-id',
            'elapsed_time': 'elapsed-time',
            'pm_history_data': 'pm-history-data',
            'granularity_period': 'granularity-period',
            'suspect_interval_flag': 'suspect-interval-flag',
            'timestamp': 'timestamp'
        }

        self._name = name
        self._local_id = local_id
        self._elapsed_time = elapsed_time
        self._pm_history_data = pm_history_data
        self._granularity_period = granularity_period
        self._suspect_interval_flag = suspect_interval_flag
        self._timestamp = timestamp

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOamPmCurrentData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.oam.PmCurrentData of this TapiOamPmCurrentData.  # noqa: E501
        :rtype: TapiOamPmCurrentData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this TapiOamPmCurrentData.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this TapiOamPmCurrentData.
        :rtype: List[TapiCommonNameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TapiOamPmCurrentData.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this TapiOamPmCurrentData.
        :type name: List[TapiCommonNameAndValue]
        """

        self._name = name

    @property
    def local_id(self):
        """Gets the local_id of this TapiOamPmCurrentData.

        none  # noqa: E501

        :return: The local_id of this TapiOamPmCurrentData.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id):
        """Sets the local_id of this TapiOamPmCurrentData.

        none  # noqa: E501

        :param local_id: The local_id of this TapiOamPmCurrentData.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this TapiOamPmCurrentData.


        :return: The elapsed_time of this TapiOamPmCurrentData.
        :rtype: TapiCommonTimeInterval
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this TapiOamPmCurrentData.


        :param elapsed_time: The elapsed_time of this TapiOamPmCurrentData.
        :type elapsed_time: TapiCommonTimeInterval
        """

        self._elapsed_time = elapsed_time

    @property
    def pm_history_data(self):
        """Gets the pm_history_data of this TapiOamPmCurrentData.

        in case of 24hr Current Data, at least 1 History Data.                      In case of 15min Current Data, at least 16 History Data.                      In case of <15min, the number of History Data shall be able to cover a span of 4 hours.  # noqa: E501

        :return: The pm_history_data of this TapiOamPmCurrentData.
        :rtype: List[TapiOamPmHistoryData]
        """
        return self._pm_history_data

    @pm_history_data.setter
    def pm_history_data(self, pm_history_data):
        """Sets the pm_history_data of this TapiOamPmCurrentData.

        in case of 24hr Current Data, at least 1 History Data.                      In case of 15min Current Data, at least 16 History Data.                      In case of <15min, the number of History Data shall be able to cover a span of 4 hours.  # noqa: E501

        :param pm_history_data: The pm_history_data of this TapiOamPmCurrentData.
        :type pm_history_data: List[TapiOamPmHistoryData]
        """

        self._pm_history_data = pm_history_data

    @property
    def granularity_period(self):
        """Gets the granularity_period of this TapiOamPmCurrentData.


        :return: The granularity_period of this TapiOamPmCurrentData.
        :rtype: TapiCommonTimePeriod
        """
        return self._granularity_period

    @granularity_period.setter
    def granularity_period(self, granularity_period):
        """Sets the granularity_period of this TapiOamPmCurrentData.


        :param granularity_period: The granularity_period of this TapiOamPmCurrentData.
        :type granularity_period: TapiCommonTimePeriod
        """

        self._granularity_period = granularity_period

    @property
    def suspect_interval_flag(self):
        """Gets the suspect_interval_flag of this TapiOamPmCurrentData.

        This attribute is used to indicate that the performance data for the current period may not be reliable. Some reasons for this to occur are:                      � Suspect data were detected by the actual resource doing data collection.                      � Transition of the administrativeState attribute to/from the 'lock' state.                      � Transition of the operationalState to/from the 'disabled' state.                      � Scheduler setting that inhibits the collection function.                      � The performance counters were reset during the interval.                      � The currentData (or subclass) object instance was created during the monitoring period.  # noqa: E501

        :return: The suspect_interval_flag of this TapiOamPmCurrentData.
        :rtype: bool
        """
        return self._suspect_interval_flag

    @suspect_interval_flag.setter
    def suspect_interval_flag(self, suspect_interval_flag):
        """Sets the suspect_interval_flag of this TapiOamPmCurrentData.

        This attribute is used to indicate that the performance data for the current period may not be reliable. Some reasons for this to occur are:                      � Suspect data were detected by the actual resource doing data collection.                      � Transition of the administrativeState attribute to/from the 'lock' state.                      � Transition of the operationalState to/from the 'disabled' state.                      � Scheduler setting that inhibits the collection function.                      � The performance counters were reset during the interval.                      � The currentData (or subclass) object instance was created during the monitoring period.  # noqa: E501

        :param suspect_interval_flag: The suspect_interval_flag of this TapiOamPmCurrentData.
        :type suspect_interval_flag: bool
        """

        self._suspect_interval_flag = suspect_interval_flag

    @property
    def timestamp(self):
        """Gets the timestamp of this TapiOamPmCurrentData.

        This attribute indicates the start of the current monitoring interval.                      The value is bound to the quarter of an hour in case of a 15 minute interval and bound to the hour in case of a 24 hour interval.  # noqa: E501

        :return: The timestamp of this TapiOamPmCurrentData.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TapiOamPmCurrentData.

        This attribute indicates the start of the current monitoring interval.                      The value is bound to the quarter of an hour in case of a 15 minute interval and bound to the hour in case of a 24 hour interval.  # noqa: E501

        :param timestamp: The timestamp of this TapiOamPmCurrentData.
        :type timestamp: str
        """

        self._timestamp = timestamp
