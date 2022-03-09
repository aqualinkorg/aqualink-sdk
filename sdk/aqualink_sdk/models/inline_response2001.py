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

class InlineResponse2001(object):
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
        'metlog': 'InlineResponse2001Metlog',
        'sonde': 'InlineResponse2001Metlog',
        'spotter': 'InlineResponse2001Metlog',
        'noaa': 'InlineResponse2001Metlog',
        'hobo': 'InlineResponse2001Metlog',
        'gfs': 'InlineResponse2001Metlog'
    }

    attribute_map = {
        'metlog': 'metlog',
        'sonde': 'sonde',
        'spotter': 'spotter',
        'noaa': 'noaa',
        'hobo': 'hobo',
        'gfs': 'gfs'
    }

    def __init__(self, metlog=None, sonde=None, spotter=None, noaa=None, hobo=None, gfs=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger"""  # noqa: E501
        self._metlog = None
        self._sonde = None
        self._spotter = None
        self._noaa = None
        self._hobo = None
        self._gfs = None
        self.discriminator = None
        if metlog is not None:
            self.metlog = metlog
        if sonde is not None:
            self.sonde = sonde
        if spotter is not None:
            self.spotter = spotter
        if noaa is not None:
            self.noaa = noaa
        if hobo is not None:
            self.hobo = hobo
        if gfs is not None:
            self.gfs = gfs

    @property
    def metlog(self):
        """Gets the metlog of this InlineResponse2001.  # noqa: E501


        :return: The metlog of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._metlog

    @metlog.setter
    def metlog(self, metlog):
        """Sets the metlog of this InlineResponse2001.


        :param metlog: The metlog of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._metlog = metlog

    @property
    def sonde(self):
        """Gets the sonde of this InlineResponse2001.  # noqa: E501


        :return: The sonde of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._sonde

    @sonde.setter
    def sonde(self, sonde):
        """Sets the sonde of this InlineResponse2001.


        :param sonde: The sonde of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._sonde = sonde

    @property
    def spotter(self):
        """Gets the spotter of this InlineResponse2001.  # noqa: E501


        :return: The spotter of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._spotter

    @spotter.setter
    def spotter(self, spotter):
        """Sets the spotter of this InlineResponse2001.


        :param spotter: The spotter of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._spotter = spotter

    @property
    def noaa(self):
        """Gets the noaa of this InlineResponse2001.  # noqa: E501


        :return: The noaa of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._noaa

    @noaa.setter
    def noaa(self, noaa):
        """Sets the noaa of this InlineResponse2001.


        :param noaa: The noaa of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._noaa = noaa

    @property
    def hobo(self):
        """Gets the hobo of this InlineResponse2001.  # noqa: E501


        :return: The hobo of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._hobo

    @hobo.setter
    def hobo(self, hobo):
        """Sets the hobo of this InlineResponse2001.


        :param hobo: The hobo of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._hobo = hobo

    @property
    def gfs(self):
        """Gets the gfs of this InlineResponse2001.  # noqa: E501


        :return: The gfs of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001Metlog
        """
        return self._gfs

    @gfs.setter
    def gfs(self, gfs):
        """Sets the gfs of this InlineResponse2001.


        :param gfs: The gfs of this InlineResponse2001.  # noqa: E501
        :type: InlineResponse2001Metlog
        """

        self._gfs = gfs

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
        if issubclass(InlineResponse2001, dict):
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
        if not isinstance(other, InlineResponse2001):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
