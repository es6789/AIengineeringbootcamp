# Project Canvas: AI sales co-pilot for pharmacies

## 1. Problem Statement

Pharmacies' revenues are driven by one of the two following factors:

1) Number of customers

2) Average ticket per customer

With this project, the goal is to focus on increasing the average ticket per customer. The main challenges for a pharmacist to be good at maximising the sales per customer are:

1) Knowing which medicines to use for a specific pathology and how to combine multiple medicines with different active principles

2) Constantly staying updated on the latest trends and news in scientific research

3) Remember all the medicines available

4) structurally collect feedback and apply it to the recommendation loop

AI would provide a superpower to pharmacists by processing these large quantities of information and providing tailored suggestions.


## 2. Data & Knowledge

Data sources will be:

1) Database of all the medicines commercially available in the country (Italy as a start) - it contains all info about medicines like:

  - Name

  - List of active ingredients

  - Application description

  - price

  - and many other

2) Company inventory - this is important since the system wants to prioritise medicines that are in stock (for items not available, we will have to think of a different approach)

3) Scientific literature - to provide the needed knowledge on which active principle to use for a specific issue, how to associate them or what to avoid etc…

4) Customer reviews - this could be useful to integrate customer feedback into the knowledge loop (i.e. Redcare)

All these data should be free of privacy and or accessibility issues. Therefore, there is no apparent major risk to availability.

## 3. AI Approach & Methodology
TBD


## 4. Performance Metrics & Evaluation Rules

North-star metrics:
1. Average ticket per customer
2. Average ticket increase compared to the baseline

Additional metrics that will be monitored will be:
1. Speed of the system response. It would not be feasible to wait more than a few seconds for the agent's suggestion
2. Prescription accuracy - how accurate are the suggestions from the system? Will it allucinate too much due to the quality or amount of inbound info?
3. Customer satisfaction - are customers actually improving their health conditions thanks to the system's recommendations?

## 5. Resources & Stakeholders
Stakeholders engaged/to engage:
1. AI engineer - to build the system
2. Pharmacists to test and provide technical guidance

Required resources consist of:
- costs for interacting with LLMs through the API;
- cost of accessing to the DB (relatively low);
- cost of accessing to scientific literature (TBD).

## 6. Risks & Mitigation

**Anticipated Risks**:
- Handling large-scale data with LLMs, ensuring data privacy, and managing potential biases in outputs.

**Mitigation Strategies**:
- Implement robust data management and regular bias checks.
- Implement continuous monitoring for associated costs.
- Implement continuous monitoring for technical metrics (defined above).
- Continuously assess risks and adapt mitigation strategies accordingly.

## 7. Deployment & Integration
TBD

## 8. Timeline & Milestones
TBD

