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

class InlineResponse200Metlog(object):
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
        'wind_gust_speed': 'list[InlineResponse200MetlogWindGustSpeed]',
        'rh': 'list[InlineResponse200MetlogWindGustSpeed]',
        'precipitation': 'list[InlineResponse200MetlogWindGustSpeed]',
        'pressure': 'list[InlineResponse200MetlogWindGustSpeed]',
        'sonde_cable_power_voltage': 'list[InlineResponse200MetlogWindGustSpeed]',
        'sonde_battery_voltage': 'list[InlineResponse200MetlogWindGustSpeed]',
        'ph_mv': 'list[InlineResponse200MetlogWindGustSpeed]',
        'ph': 'list[InlineResponse200MetlogWindGustSpeed]',
        'sonde_wiper_position': 'list[InlineResponse200MetlogWindGustSpeed]',
        'total_suspended_solids': 'list[InlineResponse200MetlogWindGustSpeed]',
        'turbidity': 'list[InlineResponse200MetlogWindGustSpeed]',
        'tds': 'list[InlineResponse200MetlogWindGustSpeed]',
        'specific_conductance': 'list[InlineResponse200MetlogWindGustSpeed]',
        'salinity': 'list[InlineResponse200MetlogWindGustSpeed]',
        'odo_concentration': 'list[InlineResponse200MetlogWindGustSpeed]',
        'odo_saturation': 'list[InlineResponse200MetlogWindGustSpeed]',
        'water_depth': 'list[InlineResponse200MetlogWindGustSpeed]',
        'conductivity': 'list[InlineResponse200MetlogWindGustSpeed]',
        'cholorophyll_concentration': 'list[InlineResponse200MetlogWindGustSpeed]',
        'cholorophyll_rfu': 'list[InlineResponse200MetlogWindGustSpeed]',
        'wind_direction': 'list[InlineResponse200MetlogWindGustSpeed]',
        'wind_speed': 'list[InlineResponse200MetlogWindGustSpeed]',
        'wave_mean_direction': 'list[InlineResponse200MetlogWindGustSpeed]',
        'wave_peak_period': 'list[InlineResponse200MetlogWindGustSpeed]',
        'wave_mean_period': 'list[InlineResponse200MetlogWindGustSpeed]',
        'significant_wave_height': 'list[InlineResponse200MetlogWindGustSpeed]',
        'sst_anomaly': 'list[InlineResponse200MetlogWindGustSpeed]',
        'bottom_temperature': 'list[InlineResponse200MetlogWindGustSpeed]',
        'top_temperature': 'list[InlineResponse200MetlogWindGustSpeed]',
        'air_temperature': 'list[InlineResponse200MetlogWindGustSpeed]',
        'satellite_temperature': 'list[InlineResponse200MetlogWindGustSpeed]',
        'dhw': 'list[InlineResponse200MetlogWindGustSpeed]',
        'temp_weekly_alert': 'list[InlineResponse200MetlogWindGustSpeed]',
        'temp_alert': 'list[InlineResponse200MetlogWindGustSpeed]'
    }

    attribute_map = {
        'wind_gust_speed': 'wind_gust_speed',
        'rh': 'rh',
        'precipitation': 'precipitation',
        'pressure': 'pressure',
        'sonde_cable_power_voltage': 'sonde_cable_power_voltage',
        'sonde_battery_voltage': 'sonde_battery_voltage',
        'ph_mv': 'ph_mv',
        'ph': 'ph',
        'sonde_wiper_position': 'sonde_wiper_position',
        'total_suspended_solids': 'total_suspended_solids',
        'turbidity': 'turbidity',
        'tds': 'tds',
        'specific_conductance': 'specific_conductance',
        'salinity': 'salinity',
        'odo_concentration': 'odo_concentration',
        'odo_saturation': 'odo_saturation',
        'water_depth': 'water_depth',
        'conductivity': 'conductivity',
        'cholorophyll_concentration': 'cholorophyll_concentration',
        'cholorophyll_rfu': 'cholorophyll_rfu',
        'wind_direction': 'wind_direction',
        'wind_speed': 'wind_speed',
        'wave_mean_direction': 'wave_mean_direction',
        'wave_peak_period': 'wave_peak_period',
        'wave_mean_period': 'wave_mean_period',
        'significant_wave_height': 'significant_wave_height',
        'sst_anomaly': 'sst_anomaly',
        'bottom_temperature': 'bottom_temperature',
        'top_temperature': 'top_temperature',
        'air_temperature': 'air_temperature',
        'satellite_temperature': 'satellite_temperature',
        'dhw': 'dhw',
        'temp_weekly_alert': 'temp_weekly_alert',
        'temp_alert': 'temp_alert'
    }

    def __init__(self, wind_gust_speed=None, rh=None, precipitation=None, pressure=None, sonde_cable_power_voltage=None, sonde_battery_voltage=None, ph_mv=None, ph=None, sonde_wiper_position=None, total_suspended_solids=None, turbidity=None, tds=None, specific_conductance=None, salinity=None, odo_concentration=None, odo_saturation=None, water_depth=None, conductivity=None, cholorophyll_concentration=None, cholorophyll_rfu=None, wind_direction=None, wind_speed=None, wave_mean_direction=None, wave_peak_period=None, wave_mean_period=None, significant_wave_height=None, sst_anomaly=None, bottom_temperature=None, top_temperature=None, air_temperature=None, satellite_temperature=None, dhw=None, temp_weekly_alert=None, temp_alert=None):  # noqa: E501
        """InlineResponse200Metlog - a model defined in Swagger"""  # noqa: E501
        self._wind_gust_speed = None
        self._rh = None
        self._precipitation = None
        self._pressure = None
        self._sonde_cable_power_voltage = None
        self._sonde_battery_voltage = None
        self._ph_mv = None
        self._ph = None
        self._sonde_wiper_position = None
        self._total_suspended_solids = None
        self._turbidity = None
        self._tds = None
        self._specific_conductance = None
        self._salinity = None
        self._odo_concentration = None
        self._odo_saturation = None
        self._water_depth = None
        self._conductivity = None
        self._cholorophyll_concentration = None
        self._cholorophyll_rfu = None
        self._wind_direction = None
        self._wind_speed = None
        self._wave_mean_direction = None
        self._wave_peak_period = None
        self._wave_mean_period = None
        self._significant_wave_height = None
        self._sst_anomaly = None
        self._bottom_temperature = None
        self._top_temperature = None
        self._air_temperature = None
        self._satellite_temperature = None
        self._dhw = None
        self._temp_weekly_alert = None
        self._temp_alert = None
        self.discriminator = None
        if wind_gust_speed is not None:
            self.wind_gust_speed = wind_gust_speed
        if rh is not None:
            self.rh = rh
        if precipitation is not None:
            self.precipitation = precipitation
        if pressure is not None:
            self.pressure = pressure
        if sonde_cable_power_voltage is not None:
            self.sonde_cable_power_voltage = sonde_cable_power_voltage
        if sonde_battery_voltage is not None:
            self.sonde_battery_voltage = sonde_battery_voltage
        if ph_mv is not None:
            self.ph_mv = ph_mv
        if ph is not None:
            self.ph = ph
        if sonde_wiper_position is not None:
            self.sonde_wiper_position = sonde_wiper_position
        if total_suspended_solids is not None:
            self.total_suspended_solids = total_suspended_solids
        if turbidity is not None:
            self.turbidity = turbidity
        if tds is not None:
            self.tds = tds
        if specific_conductance is not None:
            self.specific_conductance = specific_conductance
        if salinity is not None:
            self.salinity = salinity
        if odo_concentration is not None:
            self.odo_concentration = odo_concentration
        if odo_saturation is not None:
            self.odo_saturation = odo_saturation
        if water_depth is not None:
            self.water_depth = water_depth
        if conductivity is not None:
            self.conductivity = conductivity
        if cholorophyll_concentration is not None:
            self.cholorophyll_concentration = cholorophyll_concentration
        if cholorophyll_rfu is not None:
            self.cholorophyll_rfu = cholorophyll_rfu
        if wind_direction is not None:
            self.wind_direction = wind_direction
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if wave_mean_direction is not None:
            self.wave_mean_direction = wave_mean_direction
        if wave_peak_period is not None:
            self.wave_peak_period = wave_peak_period
        if wave_mean_period is not None:
            self.wave_mean_period = wave_mean_period
        if significant_wave_height is not None:
            self.significant_wave_height = significant_wave_height
        if sst_anomaly is not None:
            self.sst_anomaly = sst_anomaly
        if bottom_temperature is not None:
            self.bottom_temperature = bottom_temperature
        if top_temperature is not None:
            self.top_temperature = top_temperature
        if air_temperature is not None:
            self.air_temperature = air_temperature
        if satellite_temperature is not None:
            self.satellite_temperature = satellite_temperature
        if dhw is not None:
            self.dhw = dhw
        if temp_weekly_alert is not None:
            self.temp_weekly_alert = temp_weekly_alert
        if temp_alert is not None:
            self.temp_alert = temp_alert

    @property
    def wind_gust_speed(self):
        """Gets the wind_gust_speed of this InlineResponse200Metlog.  # noqa: E501


        :return: The wind_gust_speed of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wind_gust_speed

    @wind_gust_speed.setter
    def wind_gust_speed(self, wind_gust_speed):
        """Sets the wind_gust_speed of this InlineResponse200Metlog.


        :param wind_gust_speed: The wind_gust_speed of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wind_gust_speed = wind_gust_speed

    @property
    def rh(self):
        """Gets the rh of this InlineResponse200Metlog.  # noqa: E501


        :return: The rh of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._rh

    @rh.setter
    def rh(self, rh):
        """Sets the rh of this InlineResponse200Metlog.


        :param rh: The rh of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._rh = rh

    @property
    def precipitation(self):
        """Gets the precipitation of this InlineResponse200Metlog.  # noqa: E501


        :return: The precipitation of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._precipitation

    @precipitation.setter
    def precipitation(self, precipitation):
        """Sets the precipitation of this InlineResponse200Metlog.


        :param precipitation: The precipitation of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._precipitation = precipitation

    @property
    def pressure(self):
        """Gets the pressure of this InlineResponse200Metlog.  # noqa: E501


        :return: The pressure of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this InlineResponse200Metlog.


        :param pressure: The pressure of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._pressure = pressure

    @property
    def sonde_cable_power_voltage(self):
        """Gets the sonde_cable_power_voltage of this InlineResponse200Metlog.  # noqa: E501


        :return: The sonde_cable_power_voltage of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._sonde_cable_power_voltage

    @sonde_cable_power_voltage.setter
    def sonde_cable_power_voltage(self, sonde_cable_power_voltage):
        """Sets the sonde_cable_power_voltage of this InlineResponse200Metlog.


        :param sonde_cable_power_voltage: The sonde_cable_power_voltage of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._sonde_cable_power_voltage = sonde_cable_power_voltage

    @property
    def sonde_battery_voltage(self):
        """Gets the sonde_battery_voltage of this InlineResponse200Metlog.  # noqa: E501


        :return: The sonde_battery_voltage of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._sonde_battery_voltage

    @sonde_battery_voltage.setter
    def sonde_battery_voltage(self, sonde_battery_voltage):
        """Sets the sonde_battery_voltage of this InlineResponse200Metlog.


        :param sonde_battery_voltage: The sonde_battery_voltage of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._sonde_battery_voltage = sonde_battery_voltage

    @property
    def ph_mv(self):
        """Gets the ph_mv of this InlineResponse200Metlog.  # noqa: E501


        :return: The ph_mv of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._ph_mv

    @ph_mv.setter
    def ph_mv(self, ph_mv):
        """Sets the ph_mv of this InlineResponse200Metlog.


        :param ph_mv: The ph_mv of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._ph_mv = ph_mv

    @property
    def ph(self):
        """Gets the ph of this InlineResponse200Metlog.  # noqa: E501


        :return: The ph of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._ph

    @ph.setter
    def ph(self, ph):
        """Sets the ph of this InlineResponse200Metlog.


        :param ph: The ph of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._ph = ph

    @property
    def sonde_wiper_position(self):
        """Gets the sonde_wiper_position of this InlineResponse200Metlog.  # noqa: E501


        :return: The sonde_wiper_position of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._sonde_wiper_position

    @sonde_wiper_position.setter
    def sonde_wiper_position(self, sonde_wiper_position):
        """Sets the sonde_wiper_position of this InlineResponse200Metlog.


        :param sonde_wiper_position: The sonde_wiper_position of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._sonde_wiper_position = sonde_wiper_position

    @property
    def total_suspended_solids(self):
        """Gets the total_suspended_solids of this InlineResponse200Metlog.  # noqa: E501


        :return: The total_suspended_solids of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._total_suspended_solids

    @total_suspended_solids.setter
    def total_suspended_solids(self, total_suspended_solids):
        """Sets the total_suspended_solids of this InlineResponse200Metlog.


        :param total_suspended_solids: The total_suspended_solids of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._total_suspended_solids = total_suspended_solids

    @property
    def turbidity(self):
        """Gets the turbidity of this InlineResponse200Metlog.  # noqa: E501


        :return: The turbidity of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._turbidity

    @turbidity.setter
    def turbidity(self, turbidity):
        """Sets the turbidity of this InlineResponse200Metlog.


        :param turbidity: The turbidity of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._turbidity = turbidity

    @property
    def tds(self):
        """Gets the tds of this InlineResponse200Metlog.  # noqa: E501


        :return: The tds of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._tds

    @tds.setter
    def tds(self, tds):
        """Sets the tds of this InlineResponse200Metlog.


        :param tds: The tds of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._tds = tds

    @property
    def specific_conductance(self):
        """Gets the specific_conductance of this InlineResponse200Metlog.  # noqa: E501


        :return: The specific_conductance of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._specific_conductance

    @specific_conductance.setter
    def specific_conductance(self, specific_conductance):
        """Sets the specific_conductance of this InlineResponse200Metlog.


        :param specific_conductance: The specific_conductance of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._specific_conductance = specific_conductance

    @property
    def salinity(self):
        """Gets the salinity of this InlineResponse200Metlog.  # noqa: E501


        :return: The salinity of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._salinity

    @salinity.setter
    def salinity(self, salinity):
        """Sets the salinity of this InlineResponse200Metlog.


        :param salinity: The salinity of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._salinity = salinity

    @property
    def odo_concentration(self):
        """Gets the odo_concentration of this InlineResponse200Metlog.  # noqa: E501


        :return: The odo_concentration of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._odo_concentration

    @odo_concentration.setter
    def odo_concentration(self, odo_concentration):
        """Sets the odo_concentration of this InlineResponse200Metlog.


        :param odo_concentration: The odo_concentration of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._odo_concentration = odo_concentration

    @property
    def odo_saturation(self):
        """Gets the odo_saturation of this InlineResponse200Metlog.  # noqa: E501


        :return: The odo_saturation of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._odo_saturation

    @odo_saturation.setter
    def odo_saturation(self, odo_saturation):
        """Sets the odo_saturation of this InlineResponse200Metlog.


        :param odo_saturation: The odo_saturation of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._odo_saturation = odo_saturation

    @property
    def water_depth(self):
        """Gets the water_depth of this InlineResponse200Metlog.  # noqa: E501


        :return: The water_depth of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._water_depth

    @water_depth.setter
    def water_depth(self, water_depth):
        """Sets the water_depth of this InlineResponse200Metlog.


        :param water_depth: The water_depth of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._water_depth = water_depth

    @property
    def conductivity(self):
        """Gets the conductivity of this InlineResponse200Metlog.  # noqa: E501


        :return: The conductivity of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._conductivity

    @conductivity.setter
    def conductivity(self, conductivity):
        """Sets the conductivity of this InlineResponse200Metlog.


        :param conductivity: The conductivity of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._conductivity = conductivity

    @property
    def cholorophyll_concentration(self):
        """Gets the cholorophyll_concentration of this InlineResponse200Metlog.  # noqa: E501


        :return: The cholorophyll_concentration of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._cholorophyll_concentration

    @cholorophyll_concentration.setter
    def cholorophyll_concentration(self, cholorophyll_concentration):
        """Sets the cholorophyll_concentration of this InlineResponse200Metlog.


        :param cholorophyll_concentration: The cholorophyll_concentration of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._cholorophyll_concentration = cholorophyll_concentration

    @property
    def cholorophyll_rfu(self):
        """Gets the cholorophyll_rfu of this InlineResponse200Metlog.  # noqa: E501


        :return: The cholorophyll_rfu of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._cholorophyll_rfu

    @cholorophyll_rfu.setter
    def cholorophyll_rfu(self, cholorophyll_rfu):
        """Sets the cholorophyll_rfu of this InlineResponse200Metlog.


        :param cholorophyll_rfu: The cholorophyll_rfu of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._cholorophyll_rfu = cholorophyll_rfu

    @property
    def wind_direction(self):
        """Gets the wind_direction of this InlineResponse200Metlog.  # noqa: E501


        :return: The wind_direction of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wind_direction

    @wind_direction.setter
    def wind_direction(self, wind_direction):
        """Sets the wind_direction of this InlineResponse200Metlog.


        :param wind_direction: The wind_direction of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wind_direction = wind_direction

    @property
    def wind_speed(self):
        """Gets the wind_speed of this InlineResponse200Metlog.  # noqa: E501


        :return: The wind_speed of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, wind_speed):
        """Sets the wind_speed of this InlineResponse200Metlog.


        :param wind_speed: The wind_speed of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wind_speed = wind_speed

    @property
    def wave_mean_direction(self):
        """Gets the wave_mean_direction of this InlineResponse200Metlog.  # noqa: E501


        :return: The wave_mean_direction of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wave_mean_direction

    @wave_mean_direction.setter
    def wave_mean_direction(self, wave_mean_direction):
        """Sets the wave_mean_direction of this InlineResponse200Metlog.


        :param wave_mean_direction: The wave_mean_direction of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wave_mean_direction = wave_mean_direction

    @property
    def wave_peak_period(self):
        """Gets the wave_peak_period of this InlineResponse200Metlog.  # noqa: E501


        :return: The wave_peak_period of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wave_peak_period

    @wave_peak_period.setter
    def wave_peak_period(self, wave_peak_period):
        """Sets the wave_peak_period of this InlineResponse200Metlog.


        :param wave_peak_period: The wave_peak_period of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wave_peak_period = wave_peak_period

    @property
    def wave_mean_period(self):
        """Gets the wave_mean_period of this InlineResponse200Metlog.  # noqa: E501


        :return: The wave_mean_period of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._wave_mean_period

    @wave_mean_period.setter
    def wave_mean_period(self, wave_mean_period):
        """Sets the wave_mean_period of this InlineResponse200Metlog.


        :param wave_mean_period: The wave_mean_period of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._wave_mean_period = wave_mean_period

    @property
    def significant_wave_height(self):
        """Gets the significant_wave_height of this InlineResponse200Metlog.  # noqa: E501


        :return: The significant_wave_height of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._significant_wave_height

    @significant_wave_height.setter
    def significant_wave_height(self, significant_wave_height):
        """Sets the significant_wave_height of this InlineResponse200Metlog.


        :param significant_wave_height: The significant_wave_height of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._significant_wave_height = significant_wave_height

    @property
    def sst_anomaly(self):
        """Gets the sst_anomaly of this InlineResponse200Metlog.  # noqa: E501


        :return: The sst_anomaly of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._sst_anomaly

    @sst_anomaly.setter
    def sst_anomaly(self, sst_anomaly):
        """Sets the sst_anomaly of this InlineResponse200Metlog.


        :param sst_anomaly: The sst_anomaly of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._sst_anomaly = sst_anomaly

    @property
    def bottom_temperature(self):
        """Gets the bottom_temperature of this InlineResponse200Metlog.  # noqa: E501


        :return: The bottom_temperature of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._bottom_temperature

    @bottom_temperature.setter
    def bottom_temperature(self, bottom_temperature):
        """Sets the bottom_temperature of this InlineResponse200Metlog.


        :param bottom_temperature: The bottom_temperature of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._bottom_temperature = bottom_temperature

    @property
    def top_temperature(self):
        """Gets the top_temperature of this InlineResponse200Metlog.  # noqa: E501


        :return: The top_temperature of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._top_temperature

    @top_temperature.setter
    def top_temperature(self, top_temperature):
        """Sets the top_temperature of this InlineResponse200Metlog.


        :param top_temperature: The top_temperature of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._top_temperature = top_temperature

    @property
    def air_temperature(self):
        """Gets the air_temperature of this InlineResponse200Metlog.  # noqa: E501


        :return: The air_temperature of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._air_temperature

    @air_temperature.setter
    def air_temperature(self, air_temperature):
        """Sets the air_temperature of this InlineResponse200Metlog.


        :param air_temperature: The air_temperature of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._air_temperature = air_temperature

    @property
    def satellite_temperature(self):
        """Gets the satellite_temperature of this InlineResponse200Metlog.  # noqa: E501


        :return: The satellite_temperature of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._satellite_temperature

    @satellite_temperature.setter
    def satellite_temperature(self, satellite_temperature):
        """Sets the satellite_temperature of this InlineResponse200Metlog.


        :param satellite_temperature: The satellite_temperature of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._satellite_temperature = satellite_temperature

    @property
    def dhw(self):
        """Gets the dhw of this InlineResponse200Metlog.  # noqa: E501


        :return: The dhw of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._dhw

    @dhw.setter
    def dhw(self, dhw):
        """Sets the dhw of this InlineResponse200Metlog.


        :param dhw: The dhw of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._dhw = dhw

    @property
    def temp_weekly_alert(self):
        """Gets the temp_weekly_alert of this InlineResponse200Metlog.  # noqa: E501


        :return: The temp_weekly_alert of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._temp_weekly_alert

    @temp_weekly_alert.setter
    def temp_weekly_alert(self, temp_weekly_alert):
        """Sets the temp_weekly_alert of this InlineResponse200Metlog.


        :param temp_weekly_alert: The temp_weekly_alert of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._temp_weekly_alert = temp_weekly_alert

    @property
    def temp_alert(self):
        """Gets the temp_alert of this InlineResponse200Metlog.  # noqa: E501


        :return: The temp_alert of this InlineResponse200Metlog.  # noqa: E501
        :rtype: list[InlineResponse200MetlogWindGustSpeed]
        """
        return self._temp_alert

    @temp_alert.setter
    def temp_alert(self, temp_alert):
        """Sets the temp_alert of this InlineResponse200Metlog.


        :param temp_alert: The temp_alert of this InlineResponse200Metlog.  # noqa: E501
        :type: list[InlineResponse200MetlogWindGustSpeed]
        """

        self._temp_alert = temp_alert

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
        if issubclass(InlineResponse200Metlog, dict):
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
        if not isinstance(other, InlineResponse200Metlog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
