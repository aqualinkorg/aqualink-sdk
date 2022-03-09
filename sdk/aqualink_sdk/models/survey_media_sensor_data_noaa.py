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

class SurveyMediaSensorDataNoaa(object):
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
        'satellite_temperature': 'TimeSeriesPoint'
    }

    attribute_map = {
        'satellite_temperature': 'satellite_temperature'
    }

    def __init__(self, satellite_temperature=None):  # noqa: E501
        """SurveyMediaSensorDataNoaa - a model defined in Swagger"""  # noqa: E501
        self._satellite_temperature = None
        self.discriminator = None
        if satellite_temperature is not None:
            self.satellite_temperature = satellite_temperature

    @property
    def satellite_temperature(self):
        """Gets the satellite_temperature of this SurveyMediaSensorDataNoaa.  # noqa: E501


        :return: The satellite_temperature of this SurveyMediaSensorDataNoaa.  # noqa: E501
        :rtype: TimeSeriesPoint
        """
        return self._satellite_temperature

    @satellite_temperature.setter
    def satellite_temperature(self, satellite_temperature):
        """Sets the satellite_temperature of this SurveyMediaSensorDataNoaa.


        :param satellite_temperature: The satellite_temperature of this SurveyMediaSensorDataNoaa.  # noqa: E501
        :type: TimeSeriesPoint
        """

        self._satellite_temperature = satellite_temperature

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
        if issubclass(SurveyMediaSensorDataNoaa, dict):
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
        if not isinstance(other, SurveyMediaSensorDataNoaa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
