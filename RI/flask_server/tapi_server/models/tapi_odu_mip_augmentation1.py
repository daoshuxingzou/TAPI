# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_odu_odu_mip_spec import TapiOduOduMipSpec  # noqa: F401,E501
from tapi_server import util


class TapiOduMipAugmentation1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, odu_mip_spec=None):  # noqa: E501
        """TapiOduMipAugmentation1 - a model defined in OpenAPI

        :param odu_mip_spec: The odu_mip_spec of this TapiOduMipAugmentation1.  # noqa: E501
        :type odu_mip_spec: TapiOduOduMipSpec
        """
        self.openapi_types = {
            'odu_mip_spec': TapiOduOduMipSpec
        }

        self.attribute_map = {
            'odu_mip_spec': 'odu-mip-spec'
        }

        self._odu_mip_spec = odu_mip_spec

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduMipAugmentation1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.MipAugmentation1 of this TapiOduMipAugmentation1.  # noqa: E501
        :rtype: TapiOduMipAugmentation1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def odu_mip_spec(self):
        """Gets the odu_mip_spec of this TapiOduMipAugmentation1.


        :return: The odu_mip_spec of this TapiOduMipAugmentation1.
        :rtype: TapiOduOduMipSpec
        """
        return self._odu_mip_spec

    @odu_mip_spec.setter
    def odu_mip_spec(self, odu_mip_spec):
        """Sets the odu_mip_spec of this TapiOduMipAugmentation1.


        :param odu_mip_spec: The odu_mip_spec of this TapiOduMipAugmentation1.
        :type odu_mip_spec: TapiOduOduMipSpec
        """

        self._odu_mip_spec = odu_mip_spec
