
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.collections_api import CollectionsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from aqualink_sdk.api.aggregate_api import AggregateApi
from aqualink_sdk.api.collections_api import CollectionsApi
from aqualink_sdk.api.data_uploads_api import DataUploadsApi
from aqualink_sdk.api.google_cloud_storage_api import GoogleCloudStorageApi
from aqualink_sdk.api.health_check_api import HealthCheckApi
from aqualink_sdk.api.regions_api import RegionsApi
from aqualink_sdk.api.sensors_api import SensorsApi
from aqualink_sdk.api.site_applications_api import SiteApplicationsApi
from aqualink_sdk.api.site_points_of_interest_api import SitePointsOfInterestApi
from aqualink_sdk.api.sites_api import SitesApi
from aqualink_sdk.api.surveys_api import SurveysApi
from aqualink_sdk.api.time_series_api import TimeSeriesApi
from aqualink_sdk.api.users_api import UsersApi
