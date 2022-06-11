# Lesson 16 Reading

Navigation | [Past Reading](../Read-15/README.md) | [Home Page](../README.md) | [Next Reading](../Read-17/README.md) |

## What is Serverless Computing?

[Source](https://www.ibm.com/cloud/learn/serverless)

### Intro

It's about building simple functions to perform simple logical operations without the hassle of server management and without real backend infrastructure. Those functions are to be deployed on a server, so serverless doesn't mean to git rid of a server in the process of developing / using a web app.

As web-based services are labeled as SaaS (site as a service), those serverless simple functions are called FaaS (function as a service). It's worth mentioning that serverless functions & FaaS are developer-origented. Developers are the targeted audience and users of the concept.

Some applications of the serverless concept...

- Serverless databases and storage
- Event streaming and messaging
- API gateways

### Serverless vs. PaaS, containers, and VMs

| Comparesion Point               | Serverless   | PaaS             | Containers       | VMs              |
| Provisioning time measurement   | milliseconds | minutes to hours | minutes to hours | minutes to hours |
| Administrative burden           | None         | light continuum  | medium continuum | heavy continuum  |
| Maintenance mgmt                | by provider  | by provider      | significant maintenance | significant maintenance |
| Scaling                         | Auto-scaling | automatic but slow scaling | automatic but slow scaling | automatic but slow scaling |
| Capacity planning               | None         | automatic & planning scalability | automatic & planning scalability | automatic & planning scalability |
| Statelessness                   | Inherent     | can leverage HTTP | can leverage HTTP | can leverage HTTP |
| HA & DR                         | Inherent     | require additional cost and management effort | require additional cost and management effort & infrastructure can be restarted automatically | require additional cost and management effort & infrastructure can be restarted automatically |
| Resource utilization            | 100% efficient | some degree of idle capacity | some degree of idle capacity | some degree of idle capacity |
| Billing granularity and savings | 100 milliseconds | by hour or the minute | by hour or the minute | by hour or the minute |

### Pros & Cons of Serverless

#### Pros

- Improved developer productivity
- Pay for execution only
- Develop in any language
- Streamlined development/DevOps cycles
- Cost-effective performance
- Usage visibility

#### Cons

- Unacceptable latency for certain applications
- Higher costs for stable or predictable workloads
- Monitoring and debugging issues
- Vendor lock-in

### Use Cases

- Serverless and microservices
- API backends
- Data processing
- Massively parallel compute/“Map” operations
- Stream processing workloads
