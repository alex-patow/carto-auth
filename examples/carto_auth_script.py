# carto-auth

from carto_auth import CartoAuth

# Authentication
carto_auth = CartoAuth.from_oauth()
# carto_auth = CartoAuth.from_file("./carto_credentials.json")

# Get access token
access_token = carto_auth.get_access_token()

# CARTO Data Warehouse
carto_dw_project, carto_dw_token = carto_auth.get_carto_dw_credentials()
carto_dw_client = carto_auth.get_carto_dw_client()
