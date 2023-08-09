# 0x18. Webstack monitoring
##### `DevOps` `SysAdmin` `monitoring`

### Concepts
For this project, we expect you to look at these concepts:

* [Monitoring](https://intranet.alxswe.com/concepts/13)
* [Server](https://intranet.alxswe.com/concepts/67)

## Resources
**Read or watch:**

* [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
* [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
* [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
* [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

## Tasks
0. Sign up for Datadog and install datadog-agent
* Sign up for Datadog - **Please make sure you are using the US website of Datagog (https://app.datadoghq.com)**
* Use the US1 region
* Install `datadog-agent` on `web-01`
* Create an `application key`
* Copy-paste in your Intranet user profile [(here)](https://intranet.alxswe.com/users/my_profile) your DataDog `API key` and your DataDog `application key`.
* Your server `web-01` should be visible in Datadog under the host name `XX-web-01`
	* You can validate it by using this [API](https://docs.datadoghq.com/api/latest/hosts/)
	* If needed, you will need to update the hostname of your server

1. Monitor some metrics
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some `monitors` within the `Datadog` dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/).
* Set up a monitor that checks the number of read requests issued to the device per second.
* Set up a monitor that checks the number of write requests issued to the device per second.

2. Create a dashboard
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

* Create a new `dashboard`
* Add at least 4 `widgets` to your dashboard. They can be of any type and monitor whatever you’d like
* Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. **Note:** in order to get the id of your dashboard, you may need to use [Datadog’s API](https://docs.datadoghq.com/api/?lang=python#get-all-dashboards)
