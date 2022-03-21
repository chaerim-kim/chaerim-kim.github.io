---
title: "[EdgeCloudSim] - How to generate EdgeCloudSim MATLAB graphs"
tags: [Projects, Edge Computing]
permalink: /projects/edge-computing/ecs/
categories:
  - Projects
header:
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/EdgeCloudSim"
---

> 👩🏻‍💻 A Final Year Project on Edge Computing that simulates and evaluates different edge architectures


[Project Overview Post](https://chaerim-kim.github.io/projects/edge-computing/)


## 👁‍🗨 How to invoke MATLAB graphs for EdgeCloudSim
There isn't a lot of documentation about EdgeCloudSim, more so of how to actually generate these beautiful MATLAB graphs.
In this post I'll go through a step by step of how to do so.

(A)  100 Mbps | (B)  300 Mbps | (C)  500 Mbps
-- | -- | --
![image](https://user-images.githubusercontent.com/33334078/100761284-129ba280-3436-11eb-918f-8c67e236d4c7.png) | ![image](https://user-images.githubusercontent.com/33334078/100761308-19c2b080-3436-11eb-8c3a-1b5c8302a875.png) | ![image](https://user-images.githubusercontent.com/33334078/100761343-22b38200-3436-11eb-85f3-13b6772ff800.png)


### 1. Run the simulation
Please refer to my previous [post](https://chaerim-kim.github.io/projects/edge-computing/)'s Installation section to see how to run the simulation.
- The output will be saved at `sample_app1/output/`
- The simulator outputs the results of n iterations, where the ‘ite.log’ files are provided as a human-readable log of the simulation results, and files in folder ite’n’ to be fed to MATLAB for plot generation


### 2. Edit `getConfiguration.m` file to define your output log folder path
The file resides on `sample_app1/matlab/getConfiguration.m`. Make sure you define the path with ite output logs like below.

![Screenshot 2022-03-21 at 2 05 35 pm](https://user-images.githubusercontent.com/33334078/159207923-ab6cfa72-593b-4a16-9955-e698750c2d36.png)


#### Filepath
```
ret_val = '/Users/chaerim/EdgeCloudSim-master/scripts/sample_app1/output/02-04-2020_21-16/default_config';
```
![Screenshot 2022-03-21 at 1 55 51 pm](https://user-images.githubusercontent.com/33334078/159207305-4124a322-b2e9-43db-b375-ca52af944917.png)

Change this line depending on your configuration.


### 2-2. For Mac/Linux user: edit 'plotGenericResults.m' 's filepath line from '\' to '/'(line 24)

Below code will parse the path for individual files and feed it to the functions. You might need to fiddle with these two files a little - the problematic part that took me a while to figure out.🤣

```
filePath = strcat(folderPath,'/ite',int2str(s),'/SIMRESULT_',char(scenarioType(i)),'_NEXT_FIT_',int2str(mobileDeviceNumber),'DEVICES_',appType,'_GENERIC.log');
```
![Screenshot 2022-03-21 at 2 01 28 pm](https://user-images.githubusercontent.com/33334078/159207678-f7337d55-3093-433c-90a7-c561466dff21.png)


### 3. Invoke plot__.m files as you need (NOT the plotGenericResults file)


### 4. Voila! Repeat the above for different simulation output folders.


Hope this helped. Let me know if you need any further clarification.


- [EdgeCloudSim](https://github.com/CagataySonmez/EdgeCloudSim)
