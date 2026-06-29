# DEMO 3 — String Transformation
# Real-world scenario: normalizing cloud region codes for a config file

regions = ["ap-south-1", "us-east-1", "eu-west-1"]

upper_regions = [region.upper() for region in regions]

print(upper_regions)
# Output: ['AP-SOUTH-1', 'US-EAST-1', 'EU-WEST-1']


# Another common DevOps use case — stripping whitespace from env variable names
raw_env_keys = [" API_KEY ", "DB_HOST  ", "  REDIS_PORT"]

clean_env_keys = [key.strip() for key in raw_env_keys]

print(clean_env_keys)
# Output: ['API_KEY', 'DB_HOST', 'REDIS_PORT']
