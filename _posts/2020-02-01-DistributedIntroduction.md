---
title: "Distributed Systems: Introduction"
tags: [Distributed Systems]
categories:
  - Distributed Systems
date: 2020-02-01
---

## **1. Introduction to Distributed Systems**

**Definition of a DS**

|                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------- |
| \[Tannenbaum\] – A collection of autonomous computing elements that appears to its users as a single coherent system |

  - Explanation: <span class="underline">A collection of elements</span>
    that as a user myself can see the connection of the system as a
    <span class="underline">one single system</span>. - one single
    coherent view
  - **Autonomous computing elements**  then u think about nodes\! Nodes
    could be hardware or software side of things  nodes need to talk
    and collaborate with each other\!
  - Because u have number of nodes, each machine has its own block (time
    wise) hard to have a global clock. Hence, those gotta synchronise 
    concept of **TIME**\!\!
  - Need to communicate w/ each other thru msgs  these msgs need to go
    thru network\!
  - **the idea of network is important\!\!**

|                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------ |
| \[Colouris\] – A collection of autonomous computing elements that appears to its users as a single coherent system |

  - Collection of network elements are networked, and communicate via
    message passing
  - Single coherent system – nodes as a whole is dealing with one
    system. No matter where when and how the interaction takes place.
  - Examples
      - You access mobile phone and u access a server, but u have no
        idea with where the computation is taking place.
      - Q : Do we know where google services are stored?
          - Nope we don’t\!  it should be irrelevant to an application.
      - They replicate your data. 3 copies securely stored.  the fact
        that data is replicated
  - Transparency is KEY\!

|                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Transparency** : concealment from the user of the separated components in a distributed system so that its seen as a whole rather than as a collection of independent components |

**Examples of Dist. sys**
  - The internet/ intranets – cluster of computers connected
      - Doesn’t fulfil the <span class="underline">transparency</span> –
        as it is easy to guess the IP. So u know exactly where and what
  - The world wide web – to have access to data, information and
    knowledge
  - A cellular mobile phone – interesting one\! We are travelling from
    Leeds to London in a train. My communication is handled
    transparently thru the journey\!  is a true distributed system as
    it fulfils the concept of
    **<span class="underline">transparency</span>**

  - Google Hamina – a data centre for google in Finland in a middle of
    nowhere by the seaside.
      - Such large data centre, so cooling system is needed.
          - Google uses water from sea to cool the centre.  renewable
            energy
      - Data needs to be stored somewhere. It is distributed over a
        number of machines so they gotta communicate, so latency is v
        important & always an issue. And then they need to process this
        data
      - ![image](https://user-images.githubusercontent.com/33334078/74332806-7d3bfe80-4d8e-11ea-9c3a-eda851942596.png)



**Middleware**
  - 4 machines are running at the same time. && Each machine has its own
    OS, and msg passing algorithm.
  - Middleware (distributed system a) is the key layer – sits btwn
    application and OS
      - Layer that makes the OS look like a single coherent system
      - It contains commonly used components and functions that all
        applications can use
  - The middleware extends over multiple machines


**Challenges for Distributed Systems**
  - Architecture, performance, synchronization, security, transparency,
    protocols, data management, reliability, fault tolerance, failure
    \!\!
      - Would it fail all together?


**Goals for Distributed Systems**
1.  **<span class="underline">Sharing of resources -</span>** data,
    files, services, networks etc

<!-- end list -->

1.  Cloud based shared storage
    1.  Data could be stored on different remote machines, and
        synchronization is need to keep it up to date
2.  File sharing Peer to Peer networks – concept of
    <span class="underline">transparency</span>
    1.  E.g. BitTorrent – spreading of a file through many peer computer
        nodes. Since every participant is a content provider, no
        dependency on a single party
3.  Shared mail services (office 365) – again the fact that his email
    box is somewhere on the cloud. Yet he can send and receive email
    from a local machine  transparency
4.  Shared web hosting
    1.  Content distribution network  NETFLIX\! They will ensure that
        what we need to access is in the server. And it looks up the
        closet server (for low latency)
    2.  interesting is the fact that data is duplicated here and there
    3.  concept of <span class="underline">outsourcing</span> seems to
        be common

<!-- end list -->

2.  **<span class="underline">Transparency</span>**

<!-- end list -->

  - We have machine, OS, middleware, kernel  and we need them to talk
    to each other\!
  - So far we know network services as socket programming, TCP
      - Socket- <span class="underline">transparency is limited</span>.
          - I am a server and I’m writing in this socket – as my client
            will need to look at where exactly the server is. Also we
            need to know the port no.  v limited transparency
      - In this module, we gonna ensure that the transparency is
        actually there  this is where **middleware** comes in\!

|                                                                               |
| ----------------------------------------------------------------------------- |
| **Goal**: to hide heterogeneity of the underlying platforms from applications |

  - Q: What do we mean by transparency?
      - **Access** – if I look at computers in the network, some are in
        Windows, Linux, java, python. So how do they talk to each other?
         hide differences in machine architecture\!
      - **Location** – interesting – if I access a service, I have no
        idea where its coming from.
      - **Migration**- possible for data/ service to move from one to
        another. One way to access the service is all that matters to
        me.
          - Phone call, regardless of ppl moving, mobile will allow us
            to keep talking.
      - **Relocation** – object may be moved while in use. Entire site
        may have been moved from one data centre to another.
      - **Replication** – we don’t know google has 3 copies of our
        data\!
      - **Concurrency** – data may be shared by several users at the
        same time
      - **Failure** – Even if the object fails, my application shouldn’t
        fail\!

<!-- end list -->

3.  **<span class="underline">Middleware and Openness</span>**

<!-- end list -->

  - Concept of <span class="underline">openness</span> (free
    interaction) is the key – irrespective of the underlying
    environment.
      - They have diff architecture, but brings it together is the
        <span class="underline">middleware</span>\!
          - The middleware we provide have same programming interface\!
              - So the interface that they communicate with each other
                are known
              - As a <span class="underline">common protocol</span> so
                that Windows can talk to Linux
          - Interoperate – two apps, they talk to each other to
            interoperate by relying on a specified common standard\!
              - One key that will make this two systems interoperate, is
                the concept of **standards \!\! (wrote in board)–** it
                brings ppl together, and if I’m Microsoft and there’s a
                standard out there**,** make sure that my app can
                interoperate with other apps
              - This will ensure that in DS, these apps could be
                implemented and interoperate with other apps
          - Portability – to support data program written in x and y
            architecture
          - Extensible – can take this programming interfaces, and
            extend it yourself the notion of interoperability and
            portability are fulfilled

<!-- end list -->

4.  **<span class="underline">Scalability –</span>** whether a DS scales
    in terms of

<!-- end list -->

  - Size – We can add more users, machines, and resource, and it remains
    effective after a significant increase in the resources
      - Scalable in terms of users, machines, processes running in the
        machine
      - E.g. internet is designed to scale.
      - Poor scalability if cost of supporting n users is worse than
        O(n)  info needs to be organized hierarchically\! O(logn)
          - If the structure is in array, from 0-n, can u find exact x
            element\!  will take v long
          - However if we use tree structure the computation time will
            go down Hierarchical
      - PG 18 – See the growth of number of domains and how it scaled\!
        More than 1 billion now
          - It rly shows that the internet is there to grow – but we do
            not see that happening, and <span class="underline">we don’t
            see any difference in accessing the data we need\!</span> 중요

  - **\!\!** Geographically – Users and resources can lie far apart, but
    the communication delays is hardly noticed
      - Nodes in Leeds, Dublin, London
      - Geography will bring 2 imp aspect – bandwidth and
        latency\!\!\!\!\!
      - Distance itself will affect the response time – depending on the
        congestion of the network

  - \!\! Administration – number of administrative domains
      - Can still be easily managed even if it spans many independent
        administrative organizations.
      - Leeds Sheffield and York bringing together the resources  3
        admins can have conflicting system with diff security policies 
        this will impact how we use the dist sys. But keep in mind that
        this could be problematic

  -  concept of geographic and admin is v imp\!

**Scaling Techniques -** 1. Hiding communication latencies

  - Client machine on LHS and server RHS. Suppose that we input in
    client form, and this form is sent to server and is checked. Then
    server process the form.
  - Second eg says what if the client itself checks the form? If its
    correct THEN send
  -  Diff when it comes to network resources and how its implemented.
    It how we DESIGN the dis sys

**Scaling techniques – 2. DNS**

  - The name table for internet was a single master file – centralized
    approach so it didn’t scale well. And we have 1 billion machines\!\!
     gotta think how we gonna structure\!
  - Soooo the DNS is a table that is distributed, and is administered
    locally.  hierarchical nature.
      - If we have 1 bil, but 2 bil – it still works. Because of its
        hierarchical nature
  - E.g. DNS structure – \[2 pdf 22\]
      - There are 3 zones, 1 2 3. Generic/countries \~\~ local
        administrative
      - Lets say we are looking for computing department in uni of ams
          - We first look for nl – z1
          - When we get to nl, we wanna look up where ams uni is? - z2
          - And then we found the uni, and access server for cs – z3
          -  hierarchical, and it takes short time
      - Q; how often is DNS gonna change? Which zone has info that
        barely changes.
          - Zone 1 doesn’t change often – unlikely ull have a new
            country. But down zone 3, organizational layer, it changes v
            regularly


**Scaling techniques –** 3. Replication- another imp
  - Replication of data bc components of DS is likely to fail. So we
    want higher availability,
  - Pros
      - To increase availability for when it fails
      - Shares the load btwn components so that it could be accessed
      - Can hide communication latency problem
          - E.g. Netflix, we stream it from the server near you\! Less
            latency

  - Drawbacks

      - Multiple copies could be inconsistent. U gotta change and update
        ALL copies
      - To keep the copies consistent, u’ll need ur servers to
        communicate w each other  u require global synchronization
        after each modification.  VERY imp
      - Precludes large scale solutions – number of copies and servers u
        may have, and geography\!\! Will be easy to replicate things
        locally, lots of bandwidth with low latency. But in global
        scale, u may have low bandwidth, high latency  issue that u
        need to keep in mind

**Summary**

  - Defined a distributed system as a collection of independent
    computers giving the appearance of a single coherent system  
  - Introduced challenges as they apply to distributed systems
