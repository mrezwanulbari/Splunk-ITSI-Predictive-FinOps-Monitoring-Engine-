# ITSI Service Modeling Guide

## Introduction

Service modeling is the foundation of ITSI. A well-designed service model accurately reflects the relationships between business services, applications, and infrastructure components.

## Service Modeling Principles

### 1. Top-Down Approach
Start with business services that stakeholders care about, then decompose into supporting technical services.

### 2. Entity-Centric Design
Every KPI should be measurable at the entity level. Entities are the building blocks of services.

### 3. Meaningful KPIs
Each KPI should answer a specific operational question:
- **Is the service available?** (Availability KPIs)
- **Is the service performing well?** (Performance KPIs)
- **Is the service secure?** (Security KPIs)
- **Is the service compliant?** (Compliance KPIs)

## Service Modeling Workflow

```
1. Identify Business Services
   └── Interview stakeholders, review CMDB
2. Map Dependencies
   └── Service → Application → Infrastructure
3. Define Entities
   └── Servers, devices, containers, cloud resources
4. Create KPIs
   └── Availability, performance, security metrics
5. Set Thresholds
   └── Static initially, switch to adaptive after 7 days
6. Build Glass Tables
   └── Visual representation for each audience
7. Configure Alerting
   └── Notable events, aggregation policies
```

## Best Practices

| Practice | Description |
|---|---|
| Limit service depth to 3-4 levels | Deeper trees are harder to troubleshoot |
| 5-10 KPIs per service | Too many KPIs create noise |
| Use entity splitting | Allows per-entity threshold analysis |
| Enable adaptive thresholds | Reduces manual tuning and false alerts |
| Document KPI ownership | Each KPI should have a responsible team |
| Review service models quarterly | Services evolve — models should too |

## Common Anti-Patterns

| Anti-Pattern | Problem | Solution |
|---|---|---|
| Too many KPIs | Alert fatigue, poor performance | Consolidate to 5-10 meaningful KPIs |
| No entity splitting | Can't identify which component is unhealthy | Split by host, device, or instance |
| Static thresholds only | High maintenance, doesn't adapt to patterns | Enable adaptive thresholding |
| Flat service model | No dependency visibility | Build hierarchical service trees |
| KPIs with no owner | Nobody investigates when they fire | Assign team ownership to each KPI |
