# Site


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str, none_type** |  | 
**sensor_id** | **str, none_type** |  | 
**polygon** | [**UserLocation**](UserLocation.md) |  | 
**nearest_noaa_location** | [**UserLocation**](UserLocation.md) |  | 
**depth** | **float, none_type** |  | 
**iframe** | **str, none_type** |  | 
**max_monthly_mean** | **float, none_type** |  | 
**timezone** | **str, none_type** |  | 
**status** | **str** |  | 
**video_stream** | **str, none_type** |  | 
**display** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**region** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | 
**admins** | [**[User]**](User.md) |  | 
**reef_check_sites** | [**[ReefCheckSite]**](ReefCheckSite.md) |  | [optional] 
**surveys** | [**[Survey]**](Survey.md) |  | [optional] 
**reef_check_surveys** | [**[ReefCheckSurvey]**](ReefCheckSurvey.md) |  | [optional] 
**historical_monthly_mean** | [**[HistoricalMonthlyMean]**](HistoricalMonthlyMean.md) |  | [optional] 
**has_seaphox** | **bool** |  | [optional] 
**sketch_fab** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**site_application** | [**SiteApplication**](SiteApplication.md) |  | [optional] 
**has_hobo** | **bool** |  | [optional] 
**collection_data** | [**CollectionDataDto**](CollectionDataDto.md) |  | [optional] 
**masked_spotter_api_token** | **str** |  | [optional] 
**water_quality_sources** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


