# coding: utf-8

"""
    Aqualink API documentation

    The Aqualink public API documentation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2001MetlogWindGustSpeed(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'max_date': 'datetime',
        'min_date': 'datetime'
    }

    attribute_map = {
        'max_date': 'maxDate',
        'min_date': 'minDate'
    }

    def __init__(self, max_date=None, min_date=None):  # noqa: E501
        """InlineResponse2001MetlogWindGustSpeed - a model defined in Swagger"""  # noqa: E501
        self._max_date = None
        self._min_date = None
        self.discriminator = None
        if max_date is not None:
            self.max_date = max_date
        if min_date is not None:
            self.min_date = min_date

    @property
    def max_date(self):
        """Gets the max_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501


        :return: The max_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501
        :rtype: datetime
        """
        return self._max_date

    @max_date.setter
    def max_date(self, max_date):
        """Sets the max_date of this InlineResponse2001MetlogWindGustSpeed.


        :param max_date: The max_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501
        :type: datetime
        """

        self._max_date = max_date

    @property
    def min_date(self):
        """Gets the min_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501


        :return: The min_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501
        :rtype: datetime
        """
        return self._min_date

    @min_date.setter
    def min_date(self, min_date):
        """Sets the min_date of this InlineResponse2001MetlogWindGustSpeed.


        :param min_date: The min_date of this InlineResponse2001MetlogWindGustSpeed.  # noqa: E501
        :type: datetime
        """

        self._min_date = min_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse2001MetlogWindGustSpeed, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001MetlogWindGustSpeed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
