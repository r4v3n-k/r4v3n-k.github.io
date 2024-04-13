---
layout: resume
permalink: /
title: EUNJIN KWON
description: <p><span>gej48443@gmail.com</span><b>|</b><span><a href="https://www.linkedin.com/in/eunjin-kwon-a1636114a/">LinkedIn</a></span><b>|</b><span>Work Permit (Need)</span></p>

---

<!-- 
### Professional Summary

Software Engineer specializing in AI with a focus on MLOps.
Expert in problem definition, solution articulation, and collaborative ideation.
Proficient in Kubernetes, distributed data processing, and large-scale ML model management, dedicated to automating and optimizing AI systems for seamless operation.
-->

### Employment

<div class="resume-item-title">
    <h4><b>Software Engineer, MLOps, Platform Engineering</b></h4>
    <h4>NAVER LABS Corp, Seongnam-si, South Korea</h4>
    <h4>April 2022 - Present</h4>
</div>

<!--
How to reduce operational cost for ML pipelines:
    Some pipelines can want the same scale of k8s resources.
    One returns the resource if not needed soon after using.
    Simultaneously another can use it before a pipeline with the one completes.

How to diminish release cycle time: release deployment period: 3 months to 1 month

data merging is a process where data is unified from multiple sources to represent a single point of reference.
Official: 512GB -> 24 min (multi core)
Test:
    2000 records := 0.018 gb = 18 mb ------ single core ( 298 sec ) vs. multi core ( 127 sec ) : improved 57%
    6000 records := 0.05 gb = 50 mb ------- single core ( 560 sec ) vs. multi core ( 117 sec ) : improved 79%
-->
- Collaborated with the Autonomous Driving and Computer Vision research teams to elevate ML and ETL systems to a service level.
- Created REST APIs to build and maintain Kubeflow pipelines with standardized and reusable components.
- Implemented automation algorithms to remove idle Kubernetes instances occupying GPU nodes in pipeline runtime or post-completion, reducing operational costs.
- Built Apache Airflow to run on NAVER cloud infrastructures and a CI/CD pipeline using Helm Chart and Github Action to deploy on an independent environment per research team.
- Contributed to data pipeline creation and monitoring of multi-cluster operation in Airflow.
- Improved data extraction time by 57% by developing a data serialization application with Apache Spark and documented the implementation and use.

<div class="resume-item-title">
    <h4><b>Software Engineer, Robot Service, Platform Engineering</b></h4>
    <h4>NAVER LABS Corp, Seongnam-si, South Korea</h4>
    <h4>September 2021 - March 2022</h4>
</div>

<!-- reduced daily parcel non-delivery rate (6/30 = 0.2 -> 2/30 = 0.07) 13% : 미발송 택배 일 6 of 30 건 발생 -> 2건 발생 -->
- Focused on the back-end development of Robot Delivery service with Go and MySQL, refactoring the logging module to keep track of robots inside a building through Webhook.
- Lessened the daily parcel non-delivery rate by 13% by developing the notification for parcel managers.

<div class="resume-item-title">
    <h4><b>Software Engineer Intern, Machine Learning Platform, AI Research</b></h4>
    <h4>HYPERCONNECT, Seoul, South Korea</h4>
    <h4>March 2021 - April 2021</h4>
</div>

- Created a web application in Python to examine the dialogue level of chatbots through AWS MTurk.
- Developed REST APIs that perform queries on examination results in MySQL to simplify data analysis.

<div class="resume-item-title">
    <h4><b>Software Engineer Intern, Speech-To-Text, AI Research</b></h4>
    <h4>Skelter Labs, Seoul, South Korea</h4>
    <h4>August 2020 -  November 2020</h4>
</div>

- Increased model accuracy by 0.03% by developing a data cleansing tool and refactoring a data loader.
- Streamlined a model evaluation process by writing a multiprocessing program in Python.

### Technical Skills

<div class="resume-item-title">
    <h4><b>Languages:</b> Python, Go, SQL, C++, Bash</h4>
</div>

<div class="resume-item-title">
    <h4><b>Frameworks and Libraries:</b> FastAPI, Airflow, Kubeflow, Spark</h4>
</div>

<div class="resume-item-title">
    <h4><b>Databases:</b> PostgreSQL, MySQL, Hive, HBase, Redis</h4>
</div>

<div class="resume-item-title">
    <h4><b>Tools:</b> Git, Linux, Docker, Kubernetes, Github (Action, Kanban), Helm, Bazel, Elastic-search, Kibana</h4>
</div>

### Education

<div class="resume-item-title">
    <h4><b>Bachelor of Science in Computer Science and Engineering</b></h4>
    <h4>University of Seoul, Seoul, South Korea</h4>
    <h4>March 2016 - February 2021</h4>
</div>

