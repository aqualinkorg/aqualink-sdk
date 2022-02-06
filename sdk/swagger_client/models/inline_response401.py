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

class InlineResponse401(object):
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
        'status_code': 'float',
        'message': 'str',
        'error': 'str'
    }

    attribute_map = {
        'status_code': 'statusCode',
        'message': 'message',
        'error': 'error'
    }

    def __init__(self, status_code=None, message=None, error=None):  # noqa: E501
        """InlineResponse401 - a model defined in Swagger"""  # noqa: E501
        self._status_code = None
        self._message = None
        self._error = None
        self.discriminator = None
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message
        if error is not None:
            self.error = error

    @property
    def status_code(self):
        """Gets the status_code of this InlineResponse401.  # noqa: E501


        :return: The status_code of this InlineResponse401.  # noqa: E501
        :rtype: float
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this InlineResponse401.


        :param status_code: The status_code of this InlineResponse401.  # noqa: E501
        :type: float
        """

        self._status_code = status_code

    @property
    def message(self):
        """Gets the message of this InlineResponse401.  # noqa: E501


        :return: The message of this InlineResponse401.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse401.


        :param message: The message of this InlineResponse401.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def error(self):
        """Gets the error of this InlineResponse401.  # noqa: E501


        :return: The error of this InlineResponse401.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse401.


        :param error: The error of this InlineResponse401.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(InlineResponse401, dict):
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
        if not isinstance(other, InlineResponse401):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
