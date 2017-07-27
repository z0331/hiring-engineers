Your answers to the questions go here.
<h1>Level One</h1>
<h2>Bonus Question 1: In your own words, what is the Agent?</h2>
The Datadog Agent is code that is installed and runs on your hosts with the overall purpose of collecting, aggregating, and forwarding system data and metrics to Datadog. The Agent comprises a few components: First, the <b>collector</b> gathers general system metrics, such as memory and CPU, as well as information about any Datadog integrations that might be installed on the host. 
<br><br>
Second, it includes the **DogStatsD** service, an implementation of the StatsD protocol with a few Datadog-specific components added in, including the histogram metric type, support for service checks and events, and the ability to add tags. DogStatD provides a set of libraries to aggregate and send custom application metrics. For more unique applications or systems that perhaps aren't covered by an integration, the AgentCheck interface allows for the creation of Agent Checks that can gather and send custom metrics and information. 
<br><br>
Finally, the **forwarder** combines all information gathered by the collector and DogStatsD and sends it on to Datadog.
<br><br>
Host and tags on Host Map page
<img src='img/hostsAndTags.jpg'>

<h1>Level Two</h1>
<h2>Bonus Question 2: What is the difference between a timeboard and a screenboard?</h2>

<br><br>
TK
Snapshot of test.support.random
<br><br>
<h1>Level Three</h1>
TK
Monitor alert email
<br><br>
TK
Scheduled downtime email
<br><br>
