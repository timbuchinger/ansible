# Ansible Plugins

## Prometheus Push Gateway

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install [RELEASE_NAME] prometheus-community/prometheus-pushgateway
```
See the [Prometheus-Pushgateway chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-pushgateway) for more information.
