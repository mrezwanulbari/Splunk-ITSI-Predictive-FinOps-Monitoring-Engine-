# Splunk ITSI Predictive Monitoring Engine - Predictive monitoring for performance using Splunk ITSI
This engine uses **Splunk ITSI** to predict and monitor, providing real-time insights into resource usage, configuration, and security best practices.


![Splunk](https://img.shields.io/badge/Splunk-000000?style=for-the-badge&logo=splunk&logoColor=white)
![ITSI](https://img.shields.io/badge/ITSI-Service_Intelligence-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> Enterprise ITSI configurations, KPI definitions, service trees, glass tables, correlation searches, and operational intelligence frameworks for IT and security service monitoring.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Service Definitions](#service-definitions)
- [KPI Reference](#kpi-reference)
- [Notable Event Aggregation](#notable-event-aggregation)
- [Glass Tables](#glass-tables)
- [Correlation Searches](#correlation-searches)
- [Implementation Guide](#implementation-guide)
- [Contributing](#contributing)

---

## Overview

**Splunk ITSI** is a premium analytics and monitoring solution that uses machine learning, event analytics, and adaptive thresholding to provide real-time visibility into the health and performance of IT services and infrastructure.

### Key Capabilities

| Capability | Description |
|---|---|
| **Service Trees** | Hierarchical modeling of business and IT services |
| **KPI Monitoring** | Real-time Key Performance Indicators with adaptive thresholds |
| **Glass Tables** | Visual dashboards showing service health at a glance |
| **Notable Events** | AI-driven event grouping and prioritization |
| **Predictive Analytics** | ML-based anomaly detection and capacity planning |
| **MTTD/MTTR Reduction** | Accelerate detection and resolution of service issues |

### Use Cases

| Use Case | Description |
|---|---|
| IT Operations Monitoring | Monitor infrastructure health across hybrid environments |
| Security Operations | Track SOC metrics and security service health |
| Application Performance | End-to-end application monitoring with SLA tracking |
| Cloud Infrastructure | Monitor AWS, Azure, and GCP service health |
| Network Operations | Network device and circuit health monitoring |
| Business Service Monitoring | Map IT services to business outcomes |

---

## Architecture

### ITSI Service Model

```
                    ┌─────────────────────────┐
                    │   Business Service       │
                    │   "E-Commerce Platform"  │
                    │   Score: 87/100          │
                    └───────────┬──────────────┘
                                │
          ┌─────────────────────┼────────────────────┐
          │                     │                     │
┌─────────▼──────────┐ ┌───────▼─────────┐ ┌────────▼────────┐
│  Web Tier           │ │  App Tier        │ │  Data Tier       │
│  Score: 92/100      │ │  Score: 85/100   │ │  Score: 78/100   │
│  ┌──────────────┐   │ │  ┌────────────┐  │ │  ┌────────────┐  │
│  │ KPI: Latency │   │ │  │ KPI: CPU   │  │ │  │ KPI: IOPS  │  │
│  │ KPI: Error % │   │ │  │ KPI: Memory│  │ │  │ KPI: Lag   │  │
│  │ KPI: Uptime  │   │ │  │ KPI: Queue │  │ │  │ KPI: Conns │  │
│  └──────────────┘   │ │  └────────────┘  │ │  └────────────┘  │
└─────────────────────┘ └──────────────────┘ └──────────────────┘
          │                      │                     │
    ┌─────▼──────┐        ┌─────▼──────┐        ┌─────▼──────┐
    │  Entities  │        │  Entities  │        │  Entities  │
    │ web-01..05 │        │ app-01..10 │        │ db-01..03  │
    └────────────┘        └────────────┘        └────────────┘
```

---

## Repository Structure

```
splunk-itsi/
├── README.md
├── services/
│   ├── security-operations/
│   │   ├── soc-service-tree.json
│   │   ├── siem-health-service.json
│   │   └── threat-detection-service.json
│   ├── infrastructure/
│   │   ├── network-service.json
│   │   ├── compute-service.json
│   │   └── storage-service.json
│   ├── application/
│   │   ├── web-application-service.json
│   │   └── api-platform-service.json
│   └── cloud/
│       ├── aws-service.json
│       └── azure-service.json
├── kpis/
│   ├── security-kpis.json
│   ├── infrastructure-kpis.json
│   ├── application-kpis.json
│   └── cloud-kpis.json
├── correlation-searches/
│   ├── security-correlations.conf
│   ├── infrastructure-correlations.conf
│   └── service-health-correlations.conf
├── glass-tables/
│   ├── soc-overview.json
│   ├── infrastructure-health.json
│   └── executive-dashboard.json
├── notable-event-policies/
│   ├── aggregation-policies.json
│   └── episode-review-config.json
├── entity-definitions/
│   ├── entity-discovery-searches.conf
│   ├── entity-types.json
│   └── entity-import-template.csv
├── saved-searches/
│   ├── kpi-base-searches.conf
│   └── entity-health-searches.conf
├── docs/
│   ├── implementation-guide.md
│   ├── service-modeling-guide.md
│   ├── kpi-design-patterns.md
│   └── glass-table-design.md
└── scripts/
    ├── backup_itsi_config.py
    └── import_services.py
```

---

## Service Definitions

### Security Operations Service Tree

```
Security Operations (Business Service)
├── SIEM Health
│   ├── KPI: Indexing Rate (EPS)
│   ├── KPI: Search Concurrency
│   ├── KPI: License Usage %
│   ├── KPI: Forwarder Health
│   └── KPI: Index Latency
├── Threat Detection
│   ├── KPI: Notable Events/Hour
│   ├── KPI: Detection Coverage (MITRE %)
│   ├── KPI: False Positive Rate
│   ├── KPI: Mean Time to Detect (MTTD)
│   └── KPI: Correlation Search Health
├── Incident Response
│   ├── KPI: Open Incidents Count
│   ├── KPI: Mean Time to Respond (MTTR)
│   ├── KPI: SLA Compliance %
│   ├── KPI: Analyst Utilization
│   └── KPI: Escalation Rate
├── Vulnerability Management
│   ├── KPI: Critical Vulns Count
│   ├── KPI: Patch Compliance %
│   ├── KPI: Scan Coverage %
│   └── KPI: Mean Time to Remediate
└── Identity & Access
    ├── KPI: Failed Auth Rate
    ├── KPI: Privileged Account Activity
    ├── KPI: MFA Adoption %
    └── KPI: Account Lockout Rate
```

### Infrastructure Service Tree

```
Infrastructure (Business Service)
├── Network
│   ├── KPI: Interface Utilization %
│   ├── KPI: Error/Drop Rate
│   ├── KPI: BGP Session Health
│   ├── KPI: Latency (ms)
│   └── KPI: Device Availability %
├── Compute
│   ├── KPI: CPU Utilization %
│   ├── KPI: Memory Usage %
│   ├── KPI: Disk I/O Wait
│   └── KPI: Process Health
├── Storage
│   ├── KPI: Capacity Usage %
│   ├── KPI: IOPS
│   ├── KPI: Latency (ms)
│   └── KPI: Replication Lag
└── Cloud
    ├── KPI: Cloud Spend vs Budget
    ├── KPI: Instance Health
    ├── KPI: API Error Rate
    └── KPI: Region Availability
```

---

## KPI Reference

### Security Operations KPIs

| KPI Name | Search | Threshold (Warning) | Threshold (Critical) | Unit |
|---|---|---|---|---|
| Indexing Rate | `index=_internal source=*metrics.log group=per_index_thruput \| stats sum(kb) as total_kb` | < 500 MB/min | < 100 MB/min | MB/min |
| Notable Events/Hour | `\| from datamodel:"Notable_Events" \| timechart span=1h count` | > 500 | > 1000 | count/hr |
| Mean Time to Detect | `index=notable \| eval mttd=(_time - trigger_time)/60 \| stats avg(mttd)` | > 30 | > 60 | minutes |
| False Positive Rate | `index=notable \| stats count(eval(status="closed_fp")) as fp, count as total \| eval rate=fp/total*100` | > 30% | > 50% | percent |
| Forwarder Health | `index=_internal source=*metrics.log group=tcpin_connections \| stats dc(hostname)` | < 95% expected | < 90% expected | percent |

### Infrastructure KPIs

| KPI Name | Search | Threshold (Warning) | Threshold (Critical) | Unit |
|---|---|---|---|---|
| CPU Utilization | `index=os_metrics sourcetype=cpu \| stats avg(pctUsed) by host` | > 80% | > 95% | percent |
| Memory Usage | `index=os_metrics sourcetype=vmstat \| stats avg(memUsedPct) by host` | > 85% | > 95% | percent |
| Disk Usage | `index=os_metrics sourcetype=df \| stats max(UsePct) by host, filesystem` | > 80% | > 90% | percent |
| Network Interface Errors | `index=network sourcetype=snmp \| stats sum(ifInErrors) by device` | > 100/hr | > 1000/hr | errors/hr |

---

## Correlation Searches

### Security Correlation Examples

```ini
# =============================================================================
# correlation-searches/security-correlations.conf
# =============================================================================

# --- Multiple Failed Logins Followed by Success ---
[Multiple Failed Logins Followed by Success]
search = index=auth action=failure | stats count as failures by src_ip, user | where failures > 5 | join src_ip [search index=auth action=success | stats latest(_time) as success_time by src_ip, user] | where isnotnull(success_time)
description = Detects potential brute force attacks where multiple failed logins are followed by a successful login from the same source IP
severity = high
drilldown_search = index=auth src_ip=$src_ip$ user=$user$ | sort _time
entity_filter = host
rule_title = Brute Force Login: $user$ from $src_ip$ ($failures$ failures)
recommended_actions = notable, email

# --- Abnormal Data Exfiltration ---
[Abnormal Data Exfiltration]
search = index=proxy OR index=firewall action=allowed | stats sum(bytes_out) as total_bytes by src_ip, user | where total_bytes > 1073741824 | eval gb_transferred=round(total_bytes/1073741824,2)
description = Detects unusually high outbound data transfer from internal hosts
severity = high
drilldown_search = index=proxy OR index=firewall src_ip=$src_ip$ | stats sum(bytes_out) as bytes by dest_ip | sort -bytes
entity_filter = src_ip
rule_title = Data Exfiltration: $user$ transferred $gb_transferred$ GB
recommended_actions = notable, email

# --- Critical Service Degradation ---
[Critical Service Degradation]
search = | `service_health_kpi_summary_lookup` | where health_score < 50 AND service_priority="critical"
description = Fires when a critical business service health score drops below 50
severity = critical
rule_title = Critical Service Degradation: $service_name$ (Score: $health_score$)
recommended_actions = notable, email, pagerduty
```

---

## Glass Tables

### SOC Overview Glass Table

The SOC Overview glass table provides a real-time visual representation of:

- **Service Health Scores** — Color-coded status of all security services
- **Active Notable Events** — Count and severity distribution
- **Analyst Workload** — Current case assignments and utilization
- **MTTD/MTTR Trends** — Rolling averages with sparklines
- **Threat Intelligence** — Active IOC matches and threat feeds
- **Compliance Status** — Regulatory framework adherence percentages

### Design Principles

1. **Hierarchy**: Most critical services at the top
2. **Color Coding**: Green (healthy) → Yellow (warning) → Red (critical)
3. **Actionability**: Every element links to a drilldown
4. **Real-time**: All metrics refresh every 60 seconds
5. **Minimal Clutter**: Show only what drives decisions

---

## Implementation Guide

### Phase 1: Foundation (Weeks 1-2)
1. Install ITSI on the search head (cluster)
2. Configure entity discovery searches
3. Import entity definitions from CMDB/ServiceNow
4. Define entity types and aliases

### Phase 2: Service Modeling (Weeks 3-4)
1. Identify critical business services
2. Build service dependency trees
3. Define KPIs with base searches
4. Configure adaptive thresholds (requires 7+ days of data)

### Phase 3: Visualization (Weeks 5-6)
1. Create glass tables for each service tier
2. Build executive dashboards
3. Configure notable event aggregation policies
4. Set up episode review workflows

### Phase 4: Optimization (Ongoing)
1. Tune KPI thresholds based on operational feedback
2. Reduce false positive notable events
3. Add predictive analytics modules
4. Integrate with ITSM (ServiceNow, Jira)

---

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

## License

This project is licensed under the MIT License.

---

> **Maintained by [Shakil Md. Rezwanul Bari](https://github.com/mrezwanulbari)** — Cybersecurity & SIEM Engineer focused on enterprise security operations and critical infrastructure protection.
