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

class CreateSiteSurveyPointDto(object):
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
        'name': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'survey_point_label_id': 'float',
        'image_url': 'str',
        'site_id': 'float'
    }

    attribute_map = {
        'name': 'name',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'survey_point_label_id': 'surveyPointLabelId',
        'image_url': 'imageUrl',
        'site_id': 'siteId'
    }

    def __init__(self, name=None, latitude=None, longitude=None, survey_point_label_id=None, image_url=None, site_id=None):  # noqa: E501
        """CreateSiteSurveyPointDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._latitude = None
        self._longitude = None
        self._survey_point_label_id = None
        self._image_url = None
        self._site_id = None
        self.discriminator = None
        self.name = name
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if survey_point_label_id is not None:
            self.survey_point_label_id = survey_point_label_id
        if image_url is not None:
            self.image_url = image_url
        self.site_id = site_id

    @property
    def name(self):
        """Gets the name of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The name of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSiteSurveyPointDto.


        :param name: The name of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def latitude(self):
        """Gets the latitude of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The latitude of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CreateSiteSurveyPointDto.


        :param latitude: The latitude of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The longitude of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CreateSiteSurveyPointDto.


        :param longitude: The longitude of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def survey_point_label_id(self):
        """Gets the survey_point_label_id of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The survey_point_label_id of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: float
        """
        return self._survey_point_label_id

    @survey_point_label_id.setter
    def survey_point_label_id(self, survey_point_label_id):
        """Sets the survey_point_label_id of this CreateSiteSurveyPointDto.


        :param survey_point_label_id: The survey_point_label_id of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: float
        """

        self._survey_point_label_id = survey_point_label_id

    @property
    def image_url(self):
        """Gets the image_url of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The image_url of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this CreateSiteSurveyPointDto.


        :param image_url: The image_url of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def site_id(self):
        """Gets the site_id of this CreateSiteSurveyPointDto.  # noqa: E501


        :return: The site_id of this CreateSiteSurveyPointDto.  # noqa: E501
        :rtype: float
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this CreateSiteSurveyPointDto.


        :param site_id: The site_id of this CreateSiteSurveyPointDto.  # noqa: E501
        :type: float
        """
        if site_id is None:
            raise ValueError("Invalid value for `site_id`, must not be `None`")  # noqa: E501

        self._site_id = site_id

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
        if issubclass(CreateSiteSurveyPointDto, dict):
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
        if not isinstance(other, CreateSiteSurveyPointDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
