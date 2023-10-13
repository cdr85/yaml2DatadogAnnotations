#!/usr/local/bin/python3

import json
import yaml
from yaml import SafeLoader


def init_config_reformatter(python_dict):
    if "init_config" in python_dict:
        if python_dict["init_config"] is None:
            python_dict["init_config"] = "{}"
    return python_dict


def check_logs_config(python_dict):
    if "logs" in python_dict:
        logs_dict = python_dict["logs"]
        del python_dict["logs"]
        logs = 1
        logs_string = json.dumps(logs_dict, indent=2)
        logs_string = "    ".join(logs_string.splitlines(True))
    else:
        logs = 0
        logs_string = 0
    return logs_string, logs


def print_instances_annotation(python_dict, container_name, check_name):
    json_string = json.dumps(python_dict, indent=2)
    json_string = "      ".join(json_string.splitlines(True))
    print("\nYour AD Annotations v2 are:\n")
    print("annotations:\n  ad.datadoghq.com/" + container_name + ".checks: |")
    print("    {", '\n      "' + check_name + '" ' + json_string + "\n    }")


def print_logs_annotation(container_name, logs_string):
    print("  ad.datadoghq.com/" + container_name + ".logs: |")
    print("    " + logs_string)
    print("\n")


def check_integration_name(check_name):
    integrationsCore = [
        "active_directory",
        "activemq",
        "activemq_xml",
        "aerospike",
        "agent_metrics",
        "airbyte",
        "airflow",
        "amazon_eks",
        "amazon_eks_blueprints",
        "amazon_msk",
        "ambari",
        "apache",
        "arangodb",
        "argocd",
        "aspdotnet",
        "avi_vantage",
        "azure_active_directory",
        "azure_iot_edge",
        "boundary",
        "btrfs",
        "cacti",
        "calico",
        "cassandra",
        "cassandra_nodetool",
        "ceph",
        "cert_manager",
        "cilium",
        "cisco_aci",
        "citrix_hypervisor",
        "clickhouse",
        "cloud_foundry_api",
        "cloudera",
        "cockroachdb",
        "confluent_platform",
        "consul",
        "consul_connect",
        "container",
        "containerd",
        "coredns",
        "couch",
        "couchbase",
        "cri",
        "crio",
        "databricks",
        "datadog_checks_base",
        "datadog_checks_dependency_provider",
        "datadog_checks_dev",
        "datadog_checks_downloader",
        "datadog_checks_tests_helper",
        "datadog_cluster_agent",
        "datadog_operator",
        "dcgm",
        "ddev",
        "directory",
        "disk",
        "dns_check",
        "docker_daemon",
        "docs",
        "dotnetclr",
        "druid",
        "ecs_fargate",
        "eks_anywhere",
        "eks_fargate",
        "elastic",
        "envoy",
        "etcd",
        "exchange_server",
        "external_dns",
        "flink",
        "fluentd",
        "foundationdb",
        "gearmand",
        "gitlab",
        "gitlab_runner",
        "gke",
        "glusterfs",
        "go-metro",
        "go_expvar",
        "gunicorn",
        "haproxy",
        "harbor",
        "hazelcast",
        "hdfs_datanode",
        "hdfs_namenode",
        "helm",
        "hive",
        "hivemq",
        "http_check",
        "hudi",
        "hyperv",
        "iam_access_analyzer",
        "ibm_ace",
        "ibm_db2",
        "ibm_i",
        "ibm_mq",
        "ibm_was",
        "ignite",
        "iis",
        "impala",
        "istio",
        "jboss_wildfly",
        "jmeter",
        "journald",
        "kafka",
        "kafka_consumer",
        "kong",
        "kube_apiserver_metrics",
        "kube_controller_manager",
        "kube_dns",
        "kube_metrics_server",
        "kube_proxy",
        "kube_scheduler",
        "kubelet",
        "kubernetes",
        "kubernetes_state",
        "kubernetes_state_core",
        "kyototycoon",
        "langchain",
        "lighttpd",
        "linkerd",
        "linux_proc_extras",
        "mapr",
        "mapreduce",
        "marathon",
        "marklogic",
        "mcache",
        "mesos_master",
        "mesos_slave",
        "mongo",
        "mysql",
        "nagios",
        "network",
        "nfsstat",
        "nginx",
        "nginx_ingress_controller",
        "ntp",
        "nvidia_jetson",
        "oke",
        "oom_kill",
        "openai",
        "openldap",
        "openmetrics",
        "openshift",
        "openstack",
        "openstack_controller",
        "oracle",
        "otel",
        "pan_firewall",
        "pdh_check",
        "pgbouncer",
        "php_fpm",
        "pivotal_pks",
        "podman",
        "postfix",
        "postgres",
        "powerdns_recursor",
        "presto",
        "process",
        "prometheus",
        "proxysql",
        "pulsar",
        "rabbitmq",
        "ray",
        "redisdb",
        "rethinkdb",
        "riak",
        "riakcs",
        "sap_hana",
        "scylla",
        "sidekiq",
        "silk",
        "singlestore",
        "snmp",
        "snmp_american_power_conversion",
        "snmp_arista",
        "snmp_aruba",
        "snmp_chatsworth_products",
        "snmp_check_point",
        "snmp_cisco",
        "snmp_dell",
        "snmp_f5",
        "snmp_fortinet",
        "snmp_hewlett_packard_enterprise",
        "snmp_juniper",
        "snmp_netapp",
        "snowflake",
        "solr",
        "sonarqube",
        "spark",
        "sqlserver",
        "squid",
        "ssh_check",
        "statsd",
        "strimzi",
        "supervisord",
        "system_core",
        "system_swap",
        "systemd",
        "tcp_check",
        "tcp_queue_length",
        "teamcity",
        "temporal",
        "tenable",
        "teradata",
        "terraform",
        "tls",
        "tokumx",
        "tomcat",
        "torchserve",
        "traffic_server",
        "twemproxy",
        "twistlock",
        "varnish",
        "vault",
        "vertica",
        "voltdb",
        "vsphere",
        "weaviate",
        "weblogic",
        "win32_event_log",
        "wincrashdetect",
        "windows_performance_counters",
        "windows_service",
        "winkmem",
        "wmi_check",
        "yarn",
        "zk",
    ]
    if check_name not in integrationsCore:
        print(
            'WARNING: the "'
            + check_name
            + "\" integration name isn't in the list of standard core"
            + " integrations: https://github.com/DataDog/integrations-core\n"
        )


# --------------------------------------------------------------------------------------

# Main function
# get inputs
check_name = input("What's the name of the check that you want to run?  ")
container_name = input(
    "What container name should the agent run " + check_name + " on?  "
)
yaml_name = input(
    "Please enter the relative filepath to the yaml"
    + " that you want to convert to AD Annotations:  "
)

# load yaml into a python dict
yaml_file = open(yaml_name, "r")
python_dict = yaml.load(yaml_file, Loader=SafeLoader)

# Check for a logs config, reformat into separate dict if so
logs_string, logs = check_logs_config(python_dict)

# If init_config is empty, replace null with {}
python_dict = init_config_reformatter(python_dict)

# print init_config + instances annotation
print_instances_annotation(python_dict, container_name, check_name)

# print logs annotation, if needed
if logs == 1:
    print_logs_annotation(container_name, logs_string)

# add warning if check_name is used that is not in the integrations-core repo
check_integration_name(check_name)