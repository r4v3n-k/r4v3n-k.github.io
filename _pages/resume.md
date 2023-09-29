---
layout: resume
permalink: /
title: Eunjin Kwon
description: <p><span>gej48443@gmail.com</span><b>|</b><span><a href="https://www.linkedin.com/in/eunjin-kwon-a1636114a/">LinkedIn</a></span></p>

---


### TECHNICAL SKILLS

<div class="resume-item-title">
    <h4><b>Languages:</b> Python, Go, C++, SQL, Bash</h4>
</div>

<div class="resume-item-title">
    <h4><b>Technologies/Frameworks:</b> FastAPI, Airflow, Kubeflow, Spark</h4>
</div>

<div class="resume-item-title">
    <h4><b>Databases:</b> PostgreSQL, Hive, HBase, MySQL, Redis</h4>
</div>

<div class="resume-item-title">
    <h4><b>Software and Tools:</b> Git, Github, Postman, Helm, Bazel, Elastic-search, Kibana</h4>
</div>

<div class="resume-item-title">
    <h4><b>Platforms:</b> Kubernetes, Docker, Linux, MacOS</h4>
</div>


### WORK EXPERIENCE

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

- Designed and developed a framework to configure ML pipelines with standardized components.
- Created RESTful backend server enabling a cloud-based ML system operation for robots.
- Implemented idle Kubernetes resource elimination algorithms, reducing pipeline operational costs.
- Constructed a CI/CD pipeline for a core service, diminishing release cycle time by 66%.
- Developed a data merging application with Apache Spark, improving data extraction time by 57%.
- Built a custom integration between Apache Airflow and NAVER cloud infrastructure.

<div class="resume-item-title">
    <h4><b>Software Engineer, Robot Service, Platform Engineering</b></h4>
    <h4>NAVER LABS Corp, Seongnam-si, South Korea</h4>
    <h4>September 2021 - March 2022</h4>
</div>

<!-- reduced daily parcel non-delivery rate (6/30 = 0.2 -> 2/30 = 0.07) 13% : 미발송 택배 일 6 of 30 건 발생 -> 2건 발생 -->
- Focused on backend development with Echo framework and MySQL for the Robot Delivery service.
- Lessened the daily parcel non-delivery rate by 13% by implementing the notification for parcel managers.

<div class="resume-item-title">
    <h4><b>Software Engineer Intern, Machine Learning Platform, AI Research</b></h4>
    <h4>HYPERCONNECT, Seoul, South Korea</h4>
    <h4>March 2021 - April 2021</h4>
</div>

<!-- 1:1 대화 -> 3번의 조사 -> 2번 이상 false 를 받은 사람 탐색 (abusing people), true dataset 확보 -->
<!-- 생성된 데이터를 조회하는 인터페이스를 개발하여 연구원들의 실험 시간을 3시간 -> 20분 정도 단축 (SQL 문에 익숙하지 않아서) -->
- Developed a Python web application to examine the dialogue level of chat bots through AWS MTurk.
- Streamlined frequent SQL queries on survey data with Web API, reducing data analysis time.

<div class="resume-item-title">
    <h4><b>Software Engineer Intern, Speech-To-Text, AI Research</b></h4>
    <h4>Skelter Labs, Seoul, South Korea</h4>
    <h4>August 2020 -  November 2020</h4>
</div>

- Created a normalization tool for large audio data sets. Conducted noise augmentation experiments.
- Refactored training data fetching methods of the Speech-To-Text model, increasing the accuracy by 0.03%.
- Automated evaluation process of Speaker Diarization models by multiprocessing programs in Python.


### EDUCATION

<div class="resume-item-title">
    <h4><b>Bachelor of Science in Computer Science and Engineering</b></h4>
    <h4>University of Seoul, Seoul, South Korea</h4>
    <h4>March 2016 - February 2021</h4>
</div>

