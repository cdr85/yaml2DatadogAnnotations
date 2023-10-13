# yaml2DatadogAnnotations
This script converts a Datadog conf.yaml file to a containerized autodiscovery annotation configuration.

If you have a working conf.yaml file or template (ex -> https://github.com/DataDog/integrations-core/blob/master/redisdb/datadog_checks/redisdb/data/conf.yaml.example) that you'd want to automatically convert to Datadog AD Annotation V2 configuration (like here: https://docs.datadoghq.com/getting_started/containers/autodiscovery/?tab=adannotationsv2agent736), this script will read the conf.yaml file and generate a matching set of annotations.
