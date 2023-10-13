# yaml2DatadogAnnotations
This script converts a Datadog ```conf.yaml``` file to a containerized autodiscovery annotation configuration.

If you have a working ```conf.yaml``` [file or template](https://github.com/DataDog/integrations-core/blob/master/redisdb/datadog_checks/redisdb/data/conf.yaml.example) that you'd want to automatically convert to a [Datadog AD Annotation V2 configuration](https://docs.datadoghq.com/getting_started/containers/autodiscovery/?tab=adannotationsv2agent736), this script will generate a matching set of annotations for use in your containerized environment.

# Example:
```example_conf.yaml```
```
logs:
  - type: file
    path: /var/log/redis_6379.log
    source: redis
    service: <SERVICE>

init_config:

instances:
  - name: Example website
    url: https://example.com/

  - name: Example website (staging)
    url: http://staging.example.com/
```

```
$ python yaml2DatadogAnnotations.py

$ What's the name of the check that you want to run?  redisdb
$ What container name should the agent run redisdb on?  redis
$ Please enter the relative filepath to the yaml that you want to convert to AD Annotations:  example_conf.yaml
```
Output:
```
Your AD Annotations v2 are:

annotations:
  ad.datadoghq.com/redis.checks: |
    { 
      "redisdb" {
        "init_config": "{}",
        "instances": [
          {
            "name": "Example website",
            "url": "https://example.com/"
          },
          {
            "name": "Example website (staging)",
            "url": "http://staging.example.com/"
          }
        ]
      }
    }
  ad.datadoghq.com/redis.logs: |
    [
      {
        "type": "file",
        "path": "/var/log/redis_6379.log",
        "source": "redis",
        "service": "<SERVICE>"
      }
    ]
```
