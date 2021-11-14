# Ansible Plugins

## Prometheus Callback Plugin

The Prometheus Callback Plugin makes use of the Prometheus Pushgateway to send
metrics from your Ansible runs to Prometheus.

Installing the Pushgateway is easy with the use of Helm:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install [RELEASE_NAME] prometheus-community/prometheus-pushgateway
```

See the [Prometheus-Pushgateway chart repo](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-pushgateway)
for more information.
