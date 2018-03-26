# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.link import Link  # noqa: F401,E501
from tapi_server import util


class GetLinkDetailsRPCOutputSchema(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, link: Link=None):  # noqa: E501
        """GetLinkDetailsRPCOutputSchema - a model defined in Swagger

        :param link: The link of this GetLinkDetailsRPCOutputSchema.  # noqa: E501
        :type link: Link
        """
        self.swagger_types = {
            'link': Link
        }

        self.attribute_map = {
            'link': 'link'
        }

        self._link = link

    @classmethod
    def from_dict(cls, dikt) -> 'GetLinkDetailsRPCOutputSchema':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The get-link-detailsRPC_output_schema of this GetLinkDetailsRPCOutputSchema.  # noqa: E501
        :rtype: GetLinkDetailsRPCOutputSchema
        """
        return util.deserialize_model(dikt, cls)

    @property
    def link(self) -> Link:
        """Gets the link of this GetLinkDetailsRPCOutputSchema.


        :return: The link of this GetLinkDetailsRPCOutputSchema.
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link: Link):
        """Sets the link of this GetLinkDetailsRPCOutputSchema.


        :param link: The link of this GetLinkDetailsRPCOutputSchema.
        :type link: Link
        """

        self._link = link