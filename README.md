# Metrics API

## Metrics

All endpoints have prefix `/v1`.

All endpoints have fields: `id`, `time_start`, `time_end`.

All fields of endpoints is *required*.

### Activity

Period with count of steps.

Endpoints:
* `/activity` - List of metrics.
* `/activity/{id}` - Retrieve metric.

Additional fiels:
* `value` - count of steps.

### Locations

Period with point on the map.

Endpoints:
* `/locations` - List of metrics.
* `/locations/{id}` - Retrieve metric.

Additional fiels:
* `latitude` - Latitude of point.
* `longitude` - Longitude of point.

### Sleep

Period only.

Endpoints:
* `/sleep` - List of metrics.
* `/sleep/{id}` - Retrieve metric.

## Common filters

As GET parameters:

* `time_start` - `time_start` of metric is greater than or equal to value.
* `time_end` - `time_start` of metric is less than value.

## Install

For local environment:
```
pip install -r requirements/local.txt
```