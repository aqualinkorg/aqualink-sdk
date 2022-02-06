# Site

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**sensor_id** | **str** |  | 
**polygon** | [**RegionPolygon**](RegionPolygon.md) |  | 
**depth** | **float** |  | 
**max_monthly_mean** | **float** |  | 
**timezone** | **str** |  | 
**status** | **str** |  | 
**video_stream** | **str** |  | 
**display** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**region** | **AllOfSiteRegion** |  | 
**stream** | **AllOfSiteStream** |  | 
**admins** | [**list[User]**](User.md) |  | 
**surveys** | [**list[Survey]**](Survey.md) |  | 
**site_application** | [**SiteApplication**](SiteApplication.md) |  | [optional] 
**historical_monthly_mean** | [**list[HistoricalMonthlyMean]**](HistoricalMonthlyMean.md) |  | 
**has_hobo** | **bool** |  | 
**live_data** | [**list[SofarLiveDataDto]**](SofarLiveDataDto.md) |  | [optional] 
**collection_data** | [**CollectionDataDto**](CollectionDataDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

