# Table of Contents

[1. Introduction](#introduction)

[2. General Schema of User Adaptive Systems](#general-schema-of-user-adaptive-systems)

[3. General Schema of User adaptive systems II](#general-schema-of-user-adaptive-systems-ii)

[4. User models and profiles (representation](#user-models-and-profiles-representation)

[5. User models and profiles (representation) II](#user-models-and-profiles-representation-ii)

[6. User Models and Profiles (building)](#user-models-and-profiles-building)

[7. User models and profiles (building) II](#user-models-and-profiles-building-ii)

[8. Example: User engagement modelling](#example-user-engagement-modelling)

[9. Stereotypes (User categories)](#stereotypes-user-categories)

[10. Stereotypes (User categories) II](#stereotypes-user-categories-ii)

[11. Recommender systems (Part 1) – Content-based Recommenders](#recommender-systems-part-1-content-based-recommenders)

[12. Recommender systems (Part 1) – Content-based Recommenders II](#recommender-systems-part-1-content-based-recommenders-ii)

[13. Recommender systems (Part 1) – Knowledge-based recommenders](#recommender-systems-part-1-knowledge-based-recommenders)

[14. Recommender systems (Part 2) – Collaborative filtering](#recommender-systems-part-2-collaborative-filtering)

[15. Recommender systems (Part 3): Hybrid Recommenders](#recommender-systems-part-3-hybrid-recommenders)

[16. Recommender Systems (Part 4): Evaluation](#recommender-systems-part-4-evaluation)

[17. Group recommendations](#group-recommendations)

[18. Adaptive content presentation](#adaptive-content-presentation)

[19. Evaluation of user adaptive systems](#evaluation-of-user-adaptive-systems)

[20. Wrap-up and future direction](#wrap-up-and-future-direction)




## **General Schema of User Adaptive Systems**

**Previous lecture**

  - **Adaptable systems** – USER is able to modify aspects of SYSTEM to
    suit their preferences

  - **\*Adaptive systems** – SYSTEM modifies its own behaviour at least
    partly independently of specifications by USER module focuses here

**This lecture**

  - General schema of a user adaptive system

  - Examples of user-adaptive features

**Schema of user-Adaptive Systems**

  - ![image](https://user-images.githubusercontent.com/33334078/95707698-37c12f80-0c95-11eb-985c-756d9df937e4.png)

<!-- end list -->

1.  **Information collection -** When we start to design UAS, we needa
    think what info system will have about the user (**available info
    about the user**)

2.  **User model acquisition -** Using this information, how can u
    process that information (metrics, and needa analyse them)

    1.  First key – **relevance** of the information with the situation

    2.  Second key – **representation of the data** – is it enough
        information to determine the world? And we need to realize that
        we are not seeing the whole world

    3.  Third – **reliability** – is this really capturing what the user
        is saying

    4.  E.g.

        1.  Is the feedback relevant to the patient and was it enough to
            represent the situation and the real world. Doctor talks for
            30 mins but only writes one sentence. Not good
            representation

3.  **User model -** After processing of the data you come up with a
    **user model**

      - Could be db, XML, knowledge model

      - Is important to represent characteristics you can use for ur application

      - It ties it all together and give meaning and **structure** to
        the data we collected

4.  **User model application** – thinking of ways to interfere with the
    user, given the user model

      - Can use clustering, classification, simple analysis etc

5.  **Adapting to user -** Finally user sees the **interface**

      - Could be that it is larger, colour is different, you get more
        description about an item

<!-- end list -->

  - Need to have confidence in the model and information

**Main definitions**

  - **User model** – **data structure** that contains explicit
    assumptions on all aspects of User that are relevant to the adaptive
    behaviour of the system

  - **User model acquisition –** procedure that incrementally constructs
    the user model and its functions to:

      - Store, update and delete entries in the user model;

      - Maintain user model **consistency** - How we update the user
        model etc

      - Need to ensure the user model **validity** – it is deriving from
        the model hence it needs to be valid

  - **User model application –** uses the user model to:

      - Make predictions and based on that you make decisions about User

**Discussion –** what is the most important?

  - **Information about the user** – gotta have the right information to
    start with, as everything is dependent on it

  - **User model acquisition** – bc you gotta collect and pick the right
    data

  - **Adapting to user** (interface)– when working with end users, this
    is what users see– HCI

  - **User model application** –

  - **User model** – user model gives meaning to the information by
    giving it a structure

  - By choosing what's the most important they compute differently – HCI or
    data processing or etc

  - Need to have confidence in the user model

**Examples – Jameson’s paper**

  - Summarized into 2 forms to adapting

  - **Supporting system use** – helps the user to use the system so they
    continue using it

      - Can take over parts of routine tasks

      - \*Adapt interface – smart menu

      - Helping w system use – simple guidance

      - Mediating interaction w the real world

      - Controlling dialogue

  - **Supporting information acquisition**

      - help them find info

      - recommend products

      - tailor information presentation

      - support collaboration

      - \*support learning – SQL tutor

**Adapting the interface - Smart menus**

  - We need to think about what info we have about user, diff views of
    the menu as user goes thru them

  - **General schema of smart menus**

<!-- end list -->

  - ![image](https://user-images.githubusercontent.com/33334078/95707718-47407880-0c95-11eb-9b1f-2a594a76eac2.png)


    1.  Collects info about menus that user clicks – this is the input
        of the algorithm (or how long user stays, what files etc)

    2.  Model aq – register the menus that user select

    3.  User model – need some way to process and come up w
        identification of if it is a frequently used actions

          - Frequency, recency

    4.  Reason about user’s option choices ?

    5.  Modified menu content – showing the smart options

**Supporting learning - SQL tutor**

  - Learning system - We have a digital info to read, a quiz, analyse
    then you decide if you are progressing

      - How confident they are with diff SQL commands – SELECT, ORDER BY

  - **General schema of SQL tutor**

    1.  User writes SQL queries

    2.  Application of **constraints** on Users solution – then it ticks
        how many constraints have been ticked. They write rules for each
        problem (constraints) to score it

    3.  Subset of constraints mastered/ missed by user - if the user is
        not good at SELECT, pull out more related problems. It decides
        what problem subset is appropriate for the user

    4.  Rule-based engine consulting the user model – how to generate
        the feedback and how to make a coherent piece

          - How constantly did you give a feedback?

          - And as they become better u’ll fade and give less feedback

    5.  Complexity and feedback – gives user feedback

**LILSYS – mediating interaction with the real world**

  - ![image](https://user-images.githubusercontent.com/33334078/95707733-53c4d100-0c95-11eb-8b59-c2f82540bd2a.png)


  - User model – want to find user’s **availability** and
    **interoperability**

  - System developed to help the user cope with the world itself, by
    acquiring and processing evidence about the user’s cognitive and
    emotional state, and take actions based on that

  - Function of the system

      - Protects people from flooding incoming messages, by blocking it
        depending on user availability and status

      - Adaptive assistant causes msgs to be discouraged, delayed and
        stuff

      - Availability is sensed automatically.

      - Models users changing cognitive or emotional state through
        automatic adaptation

  - Strategy

      - Provide potential initiators of the communication, the
        information about recipient state

  - Lilysys does this by

      - Updating a user model continuously, about users availability for
        communication

  - Cues – with sensors

      - Physical availability

      - Door open

      - Phone or computer keyboard and mouse

      - Events in calendar

      - thru motion detector, sound detector, phone, door and computer.
        Then through logic they set the availability \!\!

  - To come up with status – ML classifier algorithm. Decision tree.

      - Takes all metrics and decide to whtehter or not user is
        available

      - Or it may be knowledge based tree – coz it says its hand picked

  - Adaptation – show availability to the user

  - Goal is to create a **hand-crafted mode**l of user info and
    assessment of user availability

  - About when and how to present messages based on user model

Recognition of mental state of drivers

  - important coz of safety issues

  - Safety relevant issues such as drowsiness and stress.

      - Recognition of long or frequent eye closure

  - And to perform actions accordingly playing waking and soothing music

  - Problem

      - Users rely on the adaptation, hence less self-awareness of own
        safety

      - Expects assistant to do everything

  - Hence to not make the user reliant, appropriate measures have to be
    taken to keep the benefits. E.g. making unpleasant sounds

Application

  - Cognitive workload – might need to schedule users diary to indicate
    that user will not be interrupted

  - Safety driving

    - Mobile apps – user is not available and interrupt so you don’t need to
    pop up noti

**AGENT SALON – supporting collaboration**

  - ![image](https://user-images.githubusercontent.com/33334078/95707755-5c1d0c00-0c95-11eb-9293-fbcade6fdce8.png)


  - So these days, network and computers connected allow for easy
    collaboration by taking into account the ways in which user match or
    compliments each other (agree and disagreed POVs)

  - How

<!-- end list -->

1.  Collects information about the exhibits that users visited and rate
    them

2.  Agent salon gets the info and looks for topics on which they could
    hold convo – exhibits that they gave diff ratings or they both liked

    1.  Extracts interesting topic by comparing the records

3.  Generates scripts of conversation

4.  It shows two animated agents simulating a conversation, encouraging
    a real conversation.

**Compare and contrast of user model systems**

**Control dialogue and lilysis - common**

  - Uses information about not acting (passive state)

  - Both use decision trees, as a knowledge model

  - Adaptation is based on filtering/ focusing information

  -
differences

  - The way the external knowledge (decision tree) is obtained

  - Control diaglogue, speech is used as an input and listens to what
    they talk but lilsys listens if they talk

  - Controlling dialogue uses one modality for user input vs multiple
    modality

Lilys, the user is being observed without kowing that they are – privacy
issue. Although we are not processing the voice and not process it, we
are still stroing it.

Questions to ask are what are the incoming data, what Ai tech itsuing,

  -
## **General Schema of User adaptive systems II**

**Lecture**

  - Practical tasks to get deeper understanding of the general
    architecture of user adaptive systems

  - Based on the reading task for this lecture

**Applying the schema to Amazon**

  - We take info about the user and about external information

**Adaptative features**

  - Today’s recommendation for you

  - New experience to the shopping – injecting knowledge

  - Improve ur recommendation

  - All recommendation and a recommendation relating to ur order

**Amazon – today’s recommendation**

  - We need to implement the feature, then we needa sketch what it'll
    look like.

<!-- end list -->

1.  What info do we have and what can we get values of

      - User purchases, statements about ownerships, and ratings

          - Rating - Very small amt of users are rating. even if they
            rate they might rate it emotionally

          - Problem with purchases

              - Could’ve bought it as a present

              - Regular or occasional shopper – is ir reliable if thy
                only are an occasional?

2.  Processing algorithm

      - We look at user attention, and select what's important and
        **converting those clicks into interest** → extract into
        database format

3.  **User model** → additional information about all the other users,
    bc you look at what other people buy

      - Matrix of user by item – simple user model

4.  **User model application**

      - you choose item user is interested in from the **matrix**, and
        recommend user the items

          - And **outer knowledge** – other people’s interest

      - By categories of the item to fetch the most common category

          - **Metadata+ external knowledge** that tells you about the
            categories

      - in both cases you need outer knowledge

5.  **Recommendation**

<!-- end list -->

  - **Cold start –** if user hasn’t brought anything and you recommend
    trending products

**Amazon – recommendations for all products**

  - Same info coming about the user

  - Now they wanna surprise the user → in order to do that you need
    external knowledge about the user

**  
**

4.  ## **User models and profiles (representation)**

5.  ## **User models and profiles (representation) II**

**User models – three broad questions**
![image](https://user-images.githubusercontent.com/33334078/95707771-6808ce00-0c95-11eb-88f8-6af266cd7e40.png)

1.  \*What is being modelled?

    1.  The nature of information

2.  \*How is this information represented?

    1.  In what structure

3.  How to construct and maintain these user models?

first 2 is this lecture

**What can be modelled in a user model/ user profile**

1.  Knowledge

2.  Interests – came from recommender system, profile of the user

3.  Goals and tasks

4.  Background

5.  Individual traits

6.  Context of work more context adaptive

<!-- end list -->

1.  **Knowledge I**

<!-- end list -->

  - Most popular in learner modelling in adaptive education system, and
    could vary how we represent it.

  - We need to have a <span class="underline">domain of area</span> we
    want to map. Domain should be supplied to the system; as a list or
    **scalar** **models**

**Scalar models**

  - Scalar models – categories, numbers which is associated

  - e.g. in evaluating language proficiency

      - Categorical - Unix commands (novice - beginner -
        intermediate-expert) qualitative

      - Numeric – No.of years doing x (0,1,2,3,4) quantitative

  - Based on these values you can assume the proficiency / knowledge

**Structural models – graphs**
![image](https://user-images.githubusercontent.com/33334078/95707799-79ea7100-0c95-11eb-94b8-67993f2e5fcb.png)


  - In graphs, we have:

      - **Nodes** – key entities and concepts in the world

      - **Links** – relevant nodes, or can name the links

  - and create a graph based upon it

  - Have graphs from outside and check if user knows these concepts, and
    we **overlay** the graph model on top each other

      - We overlay user/ learner knowledge with the domain knowledge (or
        expected expertise)

  - Counting the relationship and checking it and based on how many we
    know we overlay on top of entities, and we count how many concepts
    each person know

  - E.g.

      - User knowledge - indicating something about the user and the info that
        user may know. So the fact that she's German

      - Expected knowledge – Since she is German, so she’d know BMW

**Exercise – User model of UoL**

  - Wikipedia has a vast amt of information. And wiki takes the
    knowledge and plots wikidata (as a model)

  - Steps

      - Build a graph model for domain knowledge (what are the nodes and
        how they are linked) structure

      - Your own model will be an overlay model over the domain model

  - Types of knowledge – declarative vs procedural

      - \* **Declarative** (what we do) – represented by networks of
        concepts (i.e. facts and their relationships)

      - Procedural – represented as a set of problem-solving rules

  - Knowledge model of UoL

  - ![image](https://user-images.githubusercontent.com/33334078/95707807-8242ac00-0c95-11eb-8c87-b9842a91f886.png)


      - Binary (do they know? Yes or no)

      - Categories (how well do you know (+++ know well, ++ some
        knowledge, - no)

<!-- end list -->

2.  **Interests**

<!-- end list -->

  - Most popular in information-oriented systems (e.g. recommendation
    system)

      - News rec, item rec, interesting travel guide

      - Could have shallow or deep level like user model

  - Interest is just a list of **keywords**. Can aggregate the list of
    keywords that indicates user’s interest

      - E.g. news - What kind of news user is reding; can look at title,
        metadata and gain list of words. user interest could be most
        frequent word\!\! **key word based**

  - Pull it further to **concept based**

      - Those keywords to be a concept, you need a knowledge beyond/
        behind, which comes from knowledge source. (wikidata, google)

      - Have external knowledge graph, you mark that word or phrase and
        map it to a concept; you have a lot around that concept gives
        richness around that word

      - It gives richness. So next time you read about oil crisis you can
        approximate and pull another news coz you know that user is
        interested

  - Concept level is more powerful in reasoning hence adaptation– if I
    have concept and relationship you can jump from to another

  - Can stay in keyword and look for **synonyms**, and could be
    integrated within that business

      - Either manually create the list of synonyms or use existing
        source of synonyms

**Interests II**

  - If we have concepts, we will overlay on top of concepts;

      - We don’t know if they know it or not, we know that these
        interests them

  - ![image](https://user-images.githubusercontent.com/33334078/95707821-8ec70480-0c95-11eb-8414-a7268de2dc63.png) concepts and knowledge

  - Using **overlay model** over a structure

      - **Knowledge** - Can have all the keywords of the system and
        overlay those with user’s interst

      - **Concepts** – have all the concepts and their relationships in
        the system and overlay

          - Smartness of having knowledge behind it is that, if I know
            user has interest in certain nodes, you can go up and
            approximate and if the users are interested

  - Challenge – you usually have a limited interaction with the user

      - Have short session w the system and very little detail about their
        interests **sparsity**

  - You may not have the exact items user are interested; hence you need
    some sort of **similarity** to provide to user

      - To overcome So in concept, connected node; for list of
        knowledge, similar words

      - Some form of categorization of the list

**Exercise – user model on interests in Leeds**

  - Taxonomy limits the knowledge to those that has **inheritance**
    (instances); but makes it easier to process

  - ![image](https://user-images.githubusercontent.com/33334078/95707846-a7371f00-0c95-11eb-9496-5f11f69f4d6f.png)


  - Problem with the model

      - Graphs are **complex** coz it has relationship + goes up. When u
        pull external taxonomy, it could be very rich. So you need to
        know how far up yoyou'll go

      - External source could be **noisy** and has **limited data**

      - Users don’t talk in terms of groups, and human settlement so if
        system starts using this it can be an **understanding
        challenging**

<!-- end list -->

3.  **Goals and tasks**

<!-- end list -->
  - ![image](https://user-images.githubusercontent.com/33334078/95707858-b1f1b400-0c95-11eb-832e-c40bb4375c3b.png)
  - Most challenging/ changeable as goal/ task recognition is difficult

  - Usually modelled with a ‘goal catalogue’
    approach (predefined list/ structure of user goals and tasks)

  - To mark users goal somewhere in the catalogue then activate
    appropriate adaption (e.g. a learning system, help system)

  - Have **goals** and **sub goals**, with a tree structure

  - Challenge is to <span class="underline">find where the user is in
    the goal map</span> and how far they’ve accomplished

  - **e.g. SQL tutor**

      - There's a simple goal on top and based on tasks users have
        accomplished, identify the user goal

**Goals and tasks II**
  - ![image](https://user-images.githubusercontent.com/33334078/95707878-c03fd000-0c95-11eb-8138-18aec2a4bd33.png)

  - Using an overlay model with predefined goals or tasks

  - How to approximate that they’ve accomplished the goal?

      - Graphs or lists

  - Goal system with Bayesian network – and use some probabilities to
    except to what extent users have gone over the goals and sub goals

**Exercise – transport guide**

  - Q - What will the user model look like if we want a ‘**transport
    guide’** software to adapt to the user when advising on
    <span class="underline">how to get around in Yorkshire</span>?

      - Goal – types of transport

          - Sub goal – tasks to use the transport

      - Goal – locations you wanna visit

          - Sub goal – how to get there

  - ![image](https://user-images.githubusercontent.com/33334078/95707895-cf268280-0c95-11eb-96cd-506d80e76ddd.png)

<!-- end list -->

4.  **Background**

<!-- end list -->

  - Relatively stable information about <span class="underline">their
    previous experiences</span>

      - Profession, experience of work in related areas, opinions

      - Demographic information – name, age, sex, nationality

      - To put it in some form of category

  - Common to use user’s background for stereotype modelling (not
    overlay)

  - Challenge? Privacy \!\! hence not popular

<!-- end list -->

5.  **Individual traits**

<!-- end list -->

  - Relatively stable characteristics of the user info which together
    <span class="underline">define a user as an individual</span>

      - Characteristics such as cognitive styles, learning styles,
        personality etc

      - Can be based on psychometric tests

  - E.g. If someone is intrinsically or extrinsically motivated

      - Intrinsically – turn on values, e.g. if I do well my fam will do
        well

      - Extrinsically – just wanting awards

  - Personality model

      - E.g. Introvert, extrovert, fast thinker, future thinker

      - Personality is useful when: you are trying to convince someone.
        If they are future/ present thinker you recommend it but tweak it.

<!-- end list -->

6.  **Context of work**

<!-- end list -->

  - Context awareness is paramount for mobile devices

  - Is more like a holistic model

  - User model is more individual, but to personalise we need to know
    the individual AND **the world**

      - Hence contextual awareness

  - Early work started from platform adaptation issues, then has grown
    to mobile and ubiquitous adaptive systems

  - Now extending to other dimensions of the context such as:

      - **User location** – where is the user and what do I know about
        that. i.e noise level

          - E.g. Delivering video-based lecture I a mobile device and
            how long students are gonna consume the video. In a café,
            room, etc. It’s not a desktop app so we need to change sth.
            One of the things is to break it down to a smaller entity

      - **Physical environment** - Is it a noisy environment? Lighting?

      - **Social context** – in Facebook recommendations based on what
        your friends are doing. Recommendation based on your social
        cloud. Could be used for movement, who’s nearby and who should
        it be directed to

      - **Affective s**tate – can we detect the mental state of the
        user. We can model with some approximation from i.e. user’s
        speech – positive and negative sentiment

          - Problem – what do we do after that. After we've found out if
            the user is happy or not, back to the application and how
            are we gonna change it?

  - You only bring one parameter of context each time

      - No social context and physical environment together, bc we don’t
        know how to deal with so many things

      - E.g. medicine – we don’t give handful of medicine we give pill
        by poll

      - We isolate parameter by parameter to see what works

  - \+ While not totally about the user, the addition of the context
    makes adaptation more effective

**Dimensions of context**

  - ![image](https://user-images.githubusercontent.com/33334078/95707906-d8afea80-0c95-11eb-90f0-fd17ce0355a0.png)

  - Can take it from the context of the user (right) and see how far you
    can stretch further

      - **Task/ goal**

      - **Personal context** – interesting coz it can bring issues like
        disability, mobility and vision

      - **Social context** – anything about the time, location

      - Overall platform/ ecosystem

          - **Time/ location** - when, where, how long they’ve got

          - **Physical env** – noise? Dim?

  - OR take it from the context of the device (left) and see how far you
    can stretch further

      - Capability of the **device** – we use the performance of the
        device

          - E.g. smart watches – very limited screen, so need to be aware
            of that

      - **Environment context** – noise, pollution, movement, crowd

      - **Human context** – what are the influences that may affect the
        person?

  - Can start with something that is easy to capture and handle
    (task/goal, device) and you stretch further

  - Q - Personalised travel assistant – which context dimensions will
    you use? Past exam Q

      - From the **user model** – some demographic, **INTEREST** about
        places\! main thing

      - Personal context – mobility problems? (imp in this case)

          - If they have respiratory problem, it can affect it Rec
            becomes useless if they’ve got problems and it could rather
            remind them

      - Social context – who they are with, as they exhibit diff
        behaviours if they are going museum alone and when they are with
        someone else

      - Time location – when, where, how long they’ve got

**An example of User model/ profile**

  - **Demographic -** Name, age, nationality, education level

  - **User interest -** List of key words, list of topics

  - **User preferences -** Disabilities, preferred interaction style,
    preferred media

**Summary on user model representation (about 2 lectures)**

  - User model can include a range of parameters:

      - Knowledge, interests, goals and tasks, background, individual
        traits, context of work

  - In class

      - Overlaying with existing / external knowledge base

      - Different ways of representing a model – taxonomy, graph, table

      - Easy to model goals but is hard to find out whereabouts the user
        is in achieving that goal

  - User model is for **ADAPTATION**\!

<!-- end list -->

6.  ## **User Models and Profiles (building)**

7.  ## **User models and profiles (building) II**

**User model – three broad questions**

3\. \*How to construct and maintain these user models?

  - Different user modelling approaches

**<span class="smallcaps">User Information Collection</span>**

**1. Explicit user information collection**

  - Information entered by the user, via HTML forms (self-report or
    self-assessment)

  - Data contains:

      - Demographics such as bday, marriage, hob, personal status

  - Explicit feedback

      - Rates some links on a page (e.g. Syskill \&Webert) it recommends
        other links which they might be interested in

<table>
<thead>
<tr class="header">
<th>Pros</th>
<th>Cons</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>More reliable information</p></li>
<li><p>Easy to process</p></li>
<li><p>Complies with privacy regulations</p></li>
<li><p>User is in control of what info they give out</p></li>
</ul></td>
<td><ul>
<li><p>Users have to voluntarily provide information; otherwise no profile can be built</p></li>
<li><p>Requires time and willingness to contribute</p></li>
<li><p>Places additional burden on the user and can take long hence can lower user experience</p></li>
<li><p>User may be confused or biased in information they give</p></li>
<li><p>There may be information outside of what user knows</p></li>
<li><p>Dynamic changes can be missed – people change and you have to ask multiple times inaccuracy overtime</p></li>
</ul></td>
</tr>
</tbody>
</table>

**2. Implicit user information collection**

  - Constructed based on implicitly collected information – implicit
    user feedback

  - Is collected by the system

      - Collected on user’s client machine or application server

  - Uses digital traces of UI – comments we write, news we read, items
    we click, video we watch

  - May add additional information about user device

  - user is not explicitly aware that we are collecting information

<table>
<thead>
<tr class="header">
<th><strong>Pros</strong></th>
<th><strong>Cons</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Not obtrusive - Does not require any additional intervention by the user</p></li>
<li><p>Doesn’t require new software to be developed and installed</p></li>
<li><p>Rich data about the user</p></li>
<li><p>Gather information quickly</p></li>
</ul></td>
<td><ul>
<li><p>Not all personalised sites are used frequently enough by any single user to allow them to create a useful profile</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Techniques for implicit user information collection**

  - The article explains well

<table>
<thead>
<tr class="header">
<th><strong>Technique</strong></th>
<th><strong>Information collected</strong></th>
<th><strong>Information breadth</strong></th>
<th><strong>Pros</strong></th>
<th><strong>Cons</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Browser cache</strong></td>
<td>Browsing history</td>
<td>Any Websites</td>
<td><ul>
<li><p>Unobtrusive – user doesn’t have to install anything</p></li>
<li><p>Captures history</p></li>
<li><p>Objective/ authentic</p></li>
</ul></td>
<td><ul>
<li><p>Privacy invasion</p></li>
<li><p>Noisy (more than one user using the device)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Interaction/ desktop agents</strong></td>
<td><p>Interaction and user activity</p>
<ul>
<li><p>All the steps within the app</p></li>
</ul></td>
<td>Any personalised application</td>
<td><ul>
<li><p>All user files and activity available</p></li>
<li><p>Options they click on, resources they are opening</p></li>
</ul></td>
<td><ul>
<li><p>Requires user to install software</p></li>
<li><p>Investment in development of the software</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Logs (web logs, search logs)</strong></td>
<td><p>Browsing/ search activity</p>
<ul>
<li><p>Pages user clicked</p></li>
<li><p>Keywords</p></li>
</ul></td>
<td>Websites/ search engine sites that are logged</td>
<td><ul>
<li><p>If you can link the word’s meanings to concept, it can be quite clever – knowledge graph of google (airport-travel)</p></li>
<li><p>Information about multiple users collected</p></li>
<li><p>Collection and use of information all at same time</p></li>
</ul></td>
<td><ul>
<li><p>May be very little information as it is from one site</p></li>
<li><p>Cookies must be turned on/ and or login to site</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>File transfer from one app to another</strong></td>
<td><p>Previously stored information</p>
<ul>
<li><p>Wishlist on YouTube/ Netflix</p></li>
</ul></td>
<td>Application/ organisation specific</td>
<td><ul>
<li></li>
</ul></td>
<td>Has to be something that already exists so could not be much</td>
</tr>
<tr class="odd">
<td><strong>Mobile/ wearable sensors</strong></td>
<td>Contextual such as GPS; physiological &amp; psychological states</td>
<td>Anywhere / anytime the user has the devices on</td>
<td><ul>
<li><p>Various information and real time data</p></li>
</ul></td>
<td><ul>
<li><p>User has to have the device on</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Emerging – <strong>speech/ comments on social media</strong></td>
<td>Sentiments, viewpoints, interests</td>
<td>Social media platforms</td>
<td><ul>
<li><p>Text, pitch, hmm kinda thing, pace, together with the language can be powerful</p></li>
<li><p>Language gives authoritative information / indication</p></li>
<li><p>Natural communication</p></li>
<li><p>Fairly robust technique – there are libraries that allow processing of speech reliably</p></li>
</ul></td>
<td><ul>
<li><p>Privacy and security</p></li>
</ul>
<p>Email dictation – emails now reside somewhere in the server</p>
<ul>
<li><p>Can disadvantage some people with handicap – need to offer another door</p></li>
<li><p>Some languages may not be well resourced</p></li>
<li><p>Environment restricted – noisy</p></li>
</ul></td>
</tr>
</tbody>
</table>

**<span class="smallcaps">Step 1. User identification</span>**

  - Once you decide the information collection method, who is the user?
    How do we identify the user we are building the model for?

  - Crucial for any system that constructs profiles that represent
    individual users

  - **Methods for user identification**

      - **Software agents**

          - Small programs that reside on the user’s computer

          - Collect information about the user and share with a server
            via some protocol

          - \+ 1<sup>st</sup> reliable - more control over the
            implementation and protocol used for identification

          - \- requires user participation to install the software

      - **Logins**

          - \+ Better accuracy and consistency – track across sessions
            and btwn computers

          - \+ Can access information from different computers

          - \+ Knows who the user is and can control who they are

          - \+ With user consent consented

          - 2<sup>nd</sup> reliable

          - \- user must create an account via registration, login and
            log out burden on user

      - **Cookies**

          - Easiest and most widely deployed – transparent to the user

          - \- Poor accuracy due to multiple users – then it becomes
            privacy violation

          - \- if user uses more than one computer, it will create
            separate user profile

          - \- if user clears cookie its reset

      - **Session IDs**

          - Activity during the visit is tracked

          - \+ All the browsers are using it

          - \+ Good for searches – look at the session for short time
            and start recommending (adapting)

          - \+ Doesn’t violate privacy – no need to record bc you are only
            looking at the current session

          - \- Not a long-term user model

      - **Enhanced proxy servers**

          - \- Require that users register their machines with proxy
            server

          - \- Generally only able to identify users connecting from
            only one location, unless they bother registering diff comps
            with same proxy

**<span class="smallcaps">Step 2. User model construction</span>**

  - Next step of constructing a user model Need to think about
    techniques we gonna use

<!-- end list -->

1.  We need to take input information about the user – data mining
    skills.

2.  Also need to take into account not only what comes in but
    <span class="underline">what you are going to look in the user
    model</span> (**user model representation**)– which part is related
    to my user model

      - E.g. modelling emotional state – what info I captured is related
        to this?

      - What's the model, what comes in, which of the info will give me
        the final info model?

3.  Conduct appropriate processing – taking the info and need to derive
    processing to come up with a model

      - If the model is binary, e.g. if the user is active or inactive –
        this could become a **classifier**

      - If you are looking for several parameters – might need to do
        other processing,

          - One way is to overlay the user model – aggregating user
            model – looking at frequencies or inferences

4.  Extract the user model\! Final outcome

<!-- end list -->

1.  **Building keyword-based user model**

![Picture 1](https://user-images.githubusercontent.com/33334078/95707971-085ef280-0c96-11eb-82bf-db74a152def6.png)
![Picture 12](https://user-images.githubusercontent.com/33334078/95707979-0b59e300-0c96-11eb-910b-73856dcf7ea9.png)

<!-- end list -->

1.  Initially created by extracting keywords from web pages collected
    from some information source (e.g. browsing history) - The user is
    browsing the web

2.  Through **browsing agent,** If the user is clicking the document,
    then you pull the document

3.  From these **positive feedback documents**, look at the text it has
    which is what user have possibly read

    1.  Positive feedback docu – represents user’s interest

4.  **From these documents, extract keywords** of the document and
    **weight** them using **TF\*IDF** (Term frequency inverse document
    frequency)

<!-- end list -->

  - **Input and output**

      - Input - Unpacking the documents, which is what user has read

      - What we want – **list of keywords** k1,k2,k3,…

  - Steps

    1.  **TF -** We unpack the documents then count the frequency for
        each word in each of the document

        1.  Some terms will only be in specialised documents more
            important\!

    2.  **IDF -** Inverse document frequency – count how many of these
        documents represent a particular term, for all terms in all
        documents

        1.  Which tells the **weight of this term** in the document
            space\!

    3.  **TFIDF** Multiply both to find TFIDF

        1.  Title and heading words are identified and weighed more
            highly

  - Term with highest TFIDF core terms. And we need smart ways of
    aggregating these core terms. i.e. based on similarities, based on
    overlap of the language

  - then there's a user model \!\!

<!-- end list -->

2.  **Building graph-based user model**
  - ![image](https://user-images.githubusercontent.com/33334078/95708001-20cf0d00-0c96-11eb-9cbd-2191515a7e0d.png)

<!-- end list -->

  - Built by collecting explicit positive and negative feedback from
    users

<!-- end list -->

  - **Input**: graph

  - What are the user interests from the documents that we pulled this
    is the POSTIVIE Example of user interests

      - We are reliant on having reliable enough method to identify that
        a document is a positive i.e. how long they stayed, if they’ve
        shared, etc

  - Reminder: entities to be the nodes, and we have relationships
    between the nodes. We want to extract this graph

  - **Graph overlay** – overlay the entities that users are interested
    in output

      - From the document, you need to be looking for **concepts** from
        the graph – world knowledge is usually given, so rather than
        counting the term, in here we look for concepts that are part of
        this graph need a diff approach \!\!

  - Approach we use is **semantic tagging**

      - There are libraries, and tools

      - Take world knowledge from the world model and map it, and go
        through textural documents, and identify which of the annotated
        tags/ concepts are mentioned in the document

  - Once semantic tagging is done, you have extracted in each document
    you are counting <span class="underline">how often a particular
    concept has appeared</span>**.**

  - Then you can decide on the overlay. This is the graph-based profile

  - First you need the **graph** as an **input,** and **smartness** is
    how you do the **tagging**

      - How? Looks through text and cuts it into words or phrases, (uni,
        bigrams) it maps to the graph. It may not be exact as what is in
        the graph, so we do **approximate tagging**. (similarities,
        synonyms, partial overlays)

<!-- end list -->

3.  **Building concept-based user model**

<!-- end list -->

  - Nodes represent abstract topics considered interesting to the user,
    rather than specific words or set of words

  - **First method**

      - ![image](https://user-images.githubusercontent.com/33334078/95708030-2d536580-0c96-11eb-85a6-11b055f3b65f.png)


      - We take each document and do semantic tagging to get the overlay

      - From then on, you need to come up with **aggregated list of
        concepts** – look for top concepts. May **overlay** the graph
        that are sparse or big.

          - Might need to do pre-processing on the graph.

              - E.g. Common categories, most frequent concepts to come
                up with list based the counting on the graph

  - **Second method**

  - ![image](https://user-images.githubusercontent.com/33334078/95708043-393f2780-0c96-11eb-8539-f205b14f5750.png)

  - Identified positive documents, then based on that you need to
    identify what are the common things in these documents

  - Can **cluster** the documents the most similar documents, then from
    this group, then **extract topics** for each of the clusters then
    come up with the **top concepts** as ur user model

  - User modelling component is the red bits

  - But the input needs to be reliable \!\! the positive examples

**Summary**

  - User Information Collection

      - Explicit: given by the user

      - Implicit: monitoring what the user is doing, collected by the
        system

  - If we do implicit information collection:

      - Step 1: Identify the user

          - Depends on the data collection

      - Step 2: Construct the model

          - Keyword-based

          - Graph-based

          - Concept-based

          - We ned to think about how the model is represented and what
            the input data is.

## **Example: User engagement modelling**

**Metrics, engagement and personalisation**

  - Is a talk from Mounia Lalmas – spotify’s Head of personalisation

<!-- end list -->

1.  **<span class="smallcaps">User engagement</span>**

**User engagement**

|                                                                                        |
| -------------------------------------------------------------------------------------- |
| The quality of the user experience that emphasizes the positive aspects of interaction |

  - How to measure the positive experience

  - In particular, the fact of **wanting** to stay on the side of the
    technology for **longer** and **often**; hence leading to loyal
    users

**Why is user engagement important?**

  - \+ Can make the user become loyal

  - \+ You can collect more data about the user and can improve on the
    service

  - \+ User paying for more services

  - \+ User advertising to other people if they have a positive
    experience

  - question to ask is why am I doing?

**Mounia’s answer; Why is user engagement important?**

  - Users have increasingly enhanced expectations about their
    interactions with technology

      - This leads to increase competition amongst the providers with
        other services

  - Utilitarian factors such as usability experiential factors of
    interactions (e.g. fun, fulfilment) user engagement

**User engagement lifecycle**

  - ![image](https://user-images.githubusercontent.com/33334078/95708056-41976280-0c96-11eb-930a-463b477502bd.png)
  - ![image](https://user-images.githubusercontent.com/33334078/95708067-49570700-0c96-11eb-947d-8cb840abab72.png)


  - **New** users

  - **Active** users

      - There's a period where the users are **active** – they can stay
        engaged or can be **disengaged**. Some of them can be
        **re-engaged**

      - With user’s behaviour, you can estimate if the person is likely
        to be engaged/ disengaged based on their interaction

  - **Dormant** user – can be re-engaged or churn

  - We need to understand the rectangle\!\! Of the active user in order
    to keep users engaged

<!-- end list -->

2.  **<span class="smallcaps">Metrics</span>**

**Measurements metrics performance indicators** key slide

<table>
<thead>
<tr class="header">
<th><strong>Measurement</strong></th>
<th><strong>Metric</strong></th>
<th><strong>Key Performance Indicator (KPI)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>process of obtaining one or more quantity values that can reasonably be attributed to a <strong>quantity</strong> (number)</td>
<td><p>Metric is a calculation of the measurement</p>
<ul>
<li><p>Can aggregate the values to get more meaningful values</p></li>
</ul></td>
<td><p>Quantifiable measure demonstrating how effectively key <strong>business</strong> objectives are being achieved</p>
<ul>
<li><p>What are the values that you wanna measure</p></li>
<li><p>How do I quantify this</p></li>
<li><p>Convert it into business value that you want</p></li>
</ul></td>
</tr>
<tr class="even">
<td>e.g. clicks on a link (number of clicks)</td>
<td>E.g. (clicks on a link / views of the link) <strong>click through rate</strong></td>
<td>E.g. conversion rate – downloads divided by total clicks</td>
</tr>
</tbody>
</table>

  - measurement and KPI lies \!\! parallel \!\!

###

**We need several metrics -** from what we measure to something meaningful/
clever

  - Games – users spend much time per visit

  - SNS – users come frequently and stay long

  - Service – metrics which captures once in a time and get job done –
    when needed

  - Search – frequent and short

  - Niche – once a week

  - News – come periodically

<!-- end list -->

3.  **<span class="smallcaps">Interpretations</span>**

**1. Abandonment in search –** when there is no click on the search
result page

  - Satisfied – user clicks and abandon; good abandonment

  - Dissatisfied – didn’t get what they want; bad abandonment

  - **Measuring abandonment**

      - **Cursor trail length** – total distance travelled by cursor on
        search result page

          - Short for good abandonment

      - **Movement time** – total time cursor moved on the search result
        page

          - Longer when answers in snippet

      - **Cursor speed –** average cursor speed

          - Slower when answer is in snippet – good abandonment

  - Total time spent on search result page

**2. Dwell time in search**

  - Better proxy for **user interest** on a news article than click

  - E.g. open a link and how long do you spend to look at the link; not
    moving the cursor but staying in the link

      - Indicates that user is engaged

**3. Dwell time in search: Eye tracking**

  - Since dwell time is so important they are combining w Eye tracking

      - Can determine bad or good abandonment

  - With the tracking can determine if the user is
    reading the article or if they got lost
  - ![image](https://user-images.githubusercontent.com/33334078/95708172-858a6780-0c96-11eb-8fe7-1a32dffae858.png)


  - **Relevant docu vs irrelevant docu**

      - Left - Engaged w particular document – positive abandonment

      - Right – lost – negative engagement

      - areas and duration of fixation

  - The **trajectory** **of the eye**
      - ![image](https://user-images.githubusercontent.com/33334078/95708183-8f13cf80-0c96-11eb-9a6c-f9beb5e8caff.png)

      - Allow us to know the sequence of the area user is focused on

      - Left – how much time user has spent in each area (e.g. menu,
        content etc)

      - Right – more engaged coz its more strategic

  - **WHERE they looked at + for HOW LONG + TRAJECTORY engagement of the
    user**

**Summary**

  - User engagement is applied to:

      - Advertisements

      - Office environment to monitor workers

  - Main points

      - User engagement has a lifecycle

          - By separating the lifecycle, the team knows where to improve
            and what to focus on and divide up the work

      - Metrics depend on the context – in terms of what you want to
        personalise

  - Detecting and understanding implicit signals of user satisfaction
    are essential for enhancing the quality of recommendations

**Applying to YouTube**

  - What measurements

      - Click time

      - Watch time

      - What is shown to the user and what the user clicks

      - Likes, watch history

      - \*Metadata about the videos

          - Topic, authors, likes

  - Performance indicators

      - Engagement (watch at least one video)

      - Click on at least one advertisement from video

      - Type of content user is interested in

  - Metrics

      - Attention – whenabouts people leave the vid

      - Click through rate

      - If they can predict how long people will stay in the vid

      -
<!-- end list -->

9.  ## **Stereotypes (User categories)**

10. ## **Stereotypes (User categories) II**

**Reading -** rich-stereotype.pdf

**The cold start problem**

  - It originated from user modelling problem – the cold start problem

  - **Cold star**t - If you have insufficient information about the user
    and cannot initiate the adaptation

      - classic issue in user modelling and adaptation

  - E,g, of insufficient info

      - Amazon – not enough info so it recommends you popular ones

      - When the information about the user is noisy and have to exclude
        info resulting in limited information diluted information

  - What do you do then?

      - Can narrow down to something that is most related; but how?

      - Can open up and have dialogue with them

      - To make them explicitly rate the item

      - Put user into broader category and assume what they’d like

  - Travel agent

      - Since you are a student and ask if you are venturer, then
        recommends you what other people in the same category likes

**Concept of a ‘stereotype’**

  - Was introduced in 1979 with what it si and how it is represented

  - Frame based representation – fundamental underneath

  - Quite intuitive – e.g. something is a seasoned traveller, teenager,
    venture, we categorize and recommend

  - Why?

      - Research challenge coz it hides individual traits and put it
        into category

      - Getting popular now coz we have better representation of the
        category – we have so many users so using category is the way to
        handle it

      - We don’t have time to learn about each individual

  - How to handle the stereotype

    1.  How to represent

    2.  How are we gonna build it – about the info about the user, how
        do we assign the category

    3.  How to maintain the category

**Stereotype: definition**

  - Stereotype is a knowledge structure that represents frequently
    occurring characteristics of users

      - The large amt of data about different users and past users, will
        allow us to mine that data and identify the frequency occurring
        characteristics

      - There is rating of possibilities

  - We can infer or assign plausible inferences – cannot be sure for
    100% but since they are common category, you are making plausible
    inference

  - We have small number of observations about the user – we know little
    about the user

  - E.g. about her lecture, she knows where people struggle and try to
    adapt to it

**Scenario: Travel information system**

  - Simple explicit user model –

  - **User registers** and tells very little about themselves about their
    demographic information

      - We are not asking about interest, destination, kind of hotels
        etc

      - small number of observations

  - Then, we will be looking at **categories**

      - Married with kids

      - Professional

      - Students

  - We will assume that our system has a way to adapt to each category –
    and how from this register information how we gonna assign and give
    users recommendation

**Stereotype: Structure**

  - **Body,** aka the frame

      - Information that is typically true for users to whom the
        stereotype applies

          - **Facets** - characteristics

          - **Values** – to quantify / qualify the facets

          - **Ratings** – degree of certainty for facet-value pairs

  - **Trigger**

      - **Logical** condition that has to be satisfied for the user to
        be in that category

          - E.g Age of \>20 \<60

      - Occurrence of events which signal appropriateness of particular
        stereotypes – i.e. can associate a user with a stereotype

      - Can add a **probability value against** it – if the user
        satisfies the trigger, what's the prob of user entering the
        stereotype

      - How the probability is defined:

          - Either ask an expert

          - Look at the dataset and calculate the frequency

  - **Relations**

      - Between the stereotype and other stereotypes in the system (for
        more complex models)

**Stereotype: Professional**

| **Trigger** (age\>20)and(age\<60)and(job in ListProfessionalJobs) **P=0.8** |                  |             |
| --------------------------------------------------------------------------- | ---------------- | ----------- |
| **Facets**                                                                  | **Values**       | **Ratings** |
| **distance**                                                                | long             | 0.5         |
| **exotic-place**                                                            | 8 (out of 10)    | 0.5         |
| **hotel-category**                                                          | ‘3\*’            | 0.6         |
|                                                                             | ‘4\*’            | 0.2         |
| **price**                                                                   | ‘medium’         | 0.8         |
| **entertainment**                                                           | ‘museums’        | 0.7         |
|                                                                             | ‘theatre’        | 0.6         |
|                                                                             | ‘bowling’        | 0.3         |
|                                                                             | ‘leisure-centre’ | 0.6         |
|                                                                             | ‘night-clubs’    | 0.5         |

  - It is a **frame-based** representation

  - The entire thing is the **body** – facets, values, ratings

    1.  **Facets** corresponds to items you are recommending

    2.  Each facet has **values** – can have one or more values that are
        relevant

          - Facet ‘entertainment’ will have lot of values – but you ONLY
            put values that are relevant your category

    3.  Third stereotype body is **rating**

          - Rating comes from frequency of the past users OR

          - If we talk about travel assistance, we can ask them

  - Trigger

      - **Logical condition** that has to be satisfied for the user to
        be in that category

      - Little about the user – demographics, and you want to pull out a
        lot to suggest plausible inferences

      - (age\>20) and age \<60, and job in ListProgessionalJobs)

      - Not a cold start anymore

      - P = 0.2 - **probability value against** it – if the user
        satisfies the trigger, what's the prob of user entering the
        stereotype

**  
**

**Stereotype: Married with kids Stereotype: Student**

| **Trigger** (age\>20)and(number-children\>=1) **P=0.7** |                  |             |
| ------------------------------------------------------- | ---------------- | ----------- |
| **Facets**                                              | **Values**       | **Ratings** |
| **distance**                                            | Short            | 0.8         |
| **exotic-place**                                        | 7 (out of 10)    | 0.7         |
| **hotel-category**                                      | 3 star           | 0.8         |
|                                                         | 4 star           | 0.3         |
| **price**                                               | ‘low             | 0.8         |
| **entertainment**                                       | ‘museums’        | 0.5         |
|                                                         | ‘theatre’        | 0.2         |
|                                                         | ‘bowling’        | 0.7         |
|                                                         | ‘leisure-centre’ | 0.8         |
|                                                         | ‘night-clubs’    | 0.1         |

| **Triggers** (age\>18)and(job=‘student’) **P=1** |                  |             |
| ------------------------------------------------ | ---------------- | ----------- |
| **Facets**                                       | **Values**       | **Ratings** |
| **distance**                                     | long             | 0.4         |
| **exotic-place**                                 | 8 (out of 10)    | 0.5         |
| **hotel-category**                               | 2 star           | 0.3         |
|                                                  | 3 star           | 0.8         |
| **price**                                        | ‘low             | 0.9         |
| **entertainment**                                | ‘museums’        | 0.2         |
|                                                  | ‘theatre’        | 0.2         |
|                                                  | ‘bowling’        | 0.4         |
|                                                  | ‘leisure-centre’ | 0.4         |
|                                                  | ‘night-clubs’    | 0.8         |

  - The facets are what we know from the data

  - Dependent on what audience wants we got plausible inference about
    the category and we only know they are 18+ and are students

**Limitations of stereotyping**

  - May fall in more than one stereotype and can **contradict** each
    other

  - Bc by putting it in the category, **individual users might not fit
    i**nto that category – fundamental challenge

  - Having predefined categories; user may not fit in any of it –
    **excludes subset of the user**

**Stereotype: Man Stereotype: Women**

<table>
<thead>
<tr class="header">
<th><p><strong>Trigger</strong> (gender=‘male’) <strong>P=1</strong></p>
<p><strong>OR Trigger</strong> (name-&gt;‘male name’) <strong>P=0.7</strong></p></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Facets</strong></td>
<td><strong>Values</strong></td>
<td><strong>Ratings</strong></td>
</tr>
<tr class="even">
<td><strong>distance</strong></td>
<td>long</td>
<td>0.8</td>
</tr>
<tr class="odd">
<td><strong>Sport-activities</strong></td>
<td>8 (out of 10)</td>
<td>0.6</td>
</tr>
<tr class="even">
<td><strong>facilities</strong></td>
<td>Rent-a-car</td>
<td>0.8</td>
</tr>
<tr class="odd">
<td></td>
<td>Tv</td>
<td>0.8</td>
</tr>
<tr class="even">
<td></td>
<td>bowling</td>
<td>0.2</td>
</tr>
<tr class="odd">
<td>Entertainment</td>
<td>Night clubs</td>
<td>0.3</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr class="header">
<th><p><strong>Trigger</strong> (gender=‘female’) <strong>P=1</strong></p>
<p><strong>OR Trigger</strong> (name-&gt;‘female name’) <strong>P=0.7</strong></p></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Facets</strong></td>
<td><strong>Values</strong></td>
<td><strong>Ratings</strong></td>
</tr>
<tr class="even">
<td><strong>distance</strong></td>
<td>long</td>
<td>0.2</td>
</tr>
<tr class="odd">
<td><strong>Entertainment</strong></td>
<td>Theme-park</td>
<td>0.4</td>
</tr>
<tr class="even">
<td>Facilities</td>
<td>Sauna</td>
<td>0.8</td>
</tr>
<tr class="odd">
<td></td>
<td>Massage</td>
<td>0.8</td>
</tr>
<tr class="even">
<td></td>
<td>Bowling</td>
<td>0.2</td>
</tr>
</tbody>
</table>

  - Subjectivity can come in

**Q - Test your understanding of stereotype structure**

  - What does the stereotype probability mean?

      - If the user satisfies the trigger, the probability that user
        will fall into that stereotype

  - How many probabilities can we assign to a stereotype?

      - Multiple – for different triggers etc

  - What to facet ratings mean?

      - How likely this facet to take that value

**Combining stereotypes inferring a user model**

  - **profile stereotypes inferred user model**

  - In our system about traveller system we have very little information
    about the user we decide which trigger decide stereotype from
    several stereo we combine and come up with an inferred user model

  - Assume we have a specific user: Charlie, 27, single, IT consultant.

      - He satisfied stereotype of: ‘professional’ and ‘male’

| **Professional**, **P = 0.8** |                  |     |
| ----------------------------- | ---------------- | --- |
| **distance**                  | long             | 0.5 |
| **exotic-place**              | 8 (out of 10)    | 0.5 |
| **hotel-category**            | ‘3\*’            | 0.6 |
|                               | ‘4\*’            | 0.2 |
| **price**                     | ‘medium’         | 0.8 |
| **entertainment**             | ‘museums’        | 0.7 |
|                               | ‘theatre’        | 0.6 |
|                               | ‘bowling’        | 0.3 |
|                               | ‘leisure-centre’ | 0.6 |
|                               | ‘night-clubs’    | 0.5 |

<table>
<thead>
<tr class="header">
<th><strong>Male</strong>, <strong>P = 0.7</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>distance</strong></td>
<td>‘long’</td>
<td>0.8</td>
</tr>
<tr class="even">
<td><p><strong>sport-</strong></p>
<p><strong>activities</strong></p></td>
<td>8</td>
<td>0.6</td>
</tr>
<tr class="odd">
<td><strong>facilities</strong></td>
<td>‘rent-a-car’</td>
<td>0.8</td>
</tr>
<tr class="even">
<td></td>
<td>‘tv’</td>
<td>0.8</td>
</tr>
<tr class="odd">
<td></td>
<td>‘bowling’</td>
<td>0.2</td>
</tr>
<tr class="even">
<td><strong>entertainment</strong></td>
<td>‘night-clubs’</td>
<td>0.3</td>
</tr>
</tbody>
</table>

  - We entered the prob of man with **0.7** & professional with **0.8**
    and falls into 2 stereotypes

  - What will be in the user model of Charlie?

  - Q - If the probability repeats in both stereotype, you have two
    data- i.e. distance and entertainment. So what value are we gonna
    put into the user model of Charlie?

      - what is the rating in the end, by combining the probability\!

**Example: Charlie’s model using male & professional**

  - yellow area we need to comnine

<table>
<thead>
<tr class="header">
<th><strong>Facet</strong></th>
<th><strong>Value</strong></th>
<th><strong>P</strong></th>
<th><strong>Justification</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>gender</strong></td>
<td><strong>‘male’</strong></td>
<td><strong>0.7</strong></td>
<td><strong>Male name</strong></td>
</tr>
<tr class="even">
<td><strong>age</strong></td>
<td><strong>26</strong></td>
<td><strong>1</strong></td>
<td><strong>Profile</strong></td>
</tr>
<tr class="odd">
<td><strong>profession</strong></td>
<td><strong>‘IT consultant’</strong></td>
<td><strong>1</strong></td>
<td><strong>Profile</strong></td>
</tr>
<tr class="even">
<td><strong>distance</strong></td>
<td>‘long’</td>
<td>0.4+0.56 – 0.24 = <strong>0.72</strong></td>
<td><p>MAN</p>
<p>PROFESSIONAL</p></td>
</tr>
<tr class="odd">
<td><strong>exotic-place</strong></td>
<td>8</td>
<td>0.8*0.5 =0.4</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="even">
<td><strong>hotel-category</strong></td>
<td>3*</td>
<td>0.48</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="odd">
<td></td>
<td>4*</td>
<td>0.16</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="even">
<td><strong>price</strong></td>
<td>‘medium’</td>
<td>0.64</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="odd">
<td><strong>facilities</strong></td>
<td>‘rent-a-car’</td>
<td>0.56</td>
<td>MAN</td>
</tr>
<tr class="even">
<td></td>
<td>‘tv’</td>
<td>0.56</td>
<td>MAN</td>
</tr>
<tr class="odd">
<td><strong>sport-activities</strong></td>
<td>8</td>
<td>0.42</td>
<td>MAN</td>
</tr>
<tr class="even">
<td><strong>Entertainment</strong></td>
<td>Museums</td>
<td>0.56</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="odd">
<td></td>
<td>Theatre</td>
<td>0.48</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="even">
<td></td>
<td>Bowling</td>
<td>0.24</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="odd">
<td></td>
<td>Leisure-centre</td>
<td>0.48</td>
<td>PROFESSIONAL</td>
</tr>
<tr class="even">
<td></td>
<td>Night clubs</td>
<td>0.4 + 0.21 – 0.084= <strong>0.526</strong></td>
<td>MAN<br />
PROFESSIONAL</td>
</tr>
</tbody>
</table>

  - Take into account stereotype they come from, and the actual rating.

**Probability when in one stereotype**

  - How we calculate the probability

  - If one stereotype – we cannot put it straight away bc there's a
    probability of user entering this feature

  - **Ps<sub>tereotype</sub>(feature=value) = P (feature =
    value|stereotype) \* P(stereotype)**

**Combining stereotypes**

  - Use probability of **union** rule \!\!

      - **P (A∪B) = P(A) + p(B) - p(A\*B) = union**

  - E.g. How likely does Charlie like to travel long distance?- distance
    ‘long’

      - Stereotype A = Man, B = Professional

      - P (distance = ‘long’) = P(distance=‘long’ | man) +
        P(distance=‘long’ | Professional) – P( man\*prof)

      - \= (0.5\*0.8) + (0.8\*0.7) – (0.4\*0.56) = 0.4+0.56 – 0.24 =
        **0.72**

  - In past paper, give the steps\!\!

**Building stereotypes**

  - But then where does this stereotype come from???????

  - What is the stereotype? The trigger w probability and the body.
    Initially this is how stereo was built.

<!-- end list -->

1.  **Asking experts**

      - Asking humans who have experienced these users – who have
        experience with the users

          - e.g. travel agents, teachers

      - Ask several diff experts

          - \- But the challenge here is they may come w diff facets,
            value and ratings

      - If they are suggesting diff facets, need to decide on which
        based on your

          - **Majority v**oting

          - **Priorities** – more experienced experts rated higher

      - Seek consensus if there are several diff experts

2.  **Obtaining stereotypes form media**

      - Use the data about the user that is available to build
        stereotypes

      - Decide the attributes to use – what can you measure about the
        user.

      - Identifies meaningful **clusters** based on the selected
        attributes

          - What stereotypes look like, is a cluster – a group of users
            form the data that exhibits similar behaviour - method used
            here is **clustering**

      - **Analyse the cluster – most crucial\!**

          - Within the cluster what are the characteristics of the
            people that fall into that cluster, that identifies the
            cluster? What may be the interesting things about the user?

          - Which of those variables differ across different clusters?

          - Then based on that define the characteristics of the
            cluster, find facets and values

      - Form the stereotypes need to bring in the human

          - To decide if it is meaningful or not cluster

          - To name the cluster based on the characteristics

**Obtaining stereotypes from data: News**

  - Need to obtain meaningful cluster so we can obtain stereotypes

  - Professional financial reader (identified the clusters by humans)

      - The machine extracted some parameters for a cluster, then humans
        named it

      - Based on their reading behaviour, they are interested in:
        economy – high of 1, medium 0. Low 0

| Facet   | Value  | Rating |
| ------- | ------ | ------ |
| Economy | High   | 1      |
|         | Medium | 0      |
|         | Low    | 0      |

  - Adult superior committed style

      - If age is part of the trigger, the probability is 0.6 for that
        trigger 35-55

      - Education level – university of 0.8 and secondary 0.2

      - If you are combining the two, need to take both prob into
        consideration

  - Can decide if these are going to be the facet in your stereotype or
    not


**Obtaining stereotypes from data: TV**
  - ![image](https://user-images.githubusercontent.com/33334078/95708262-bff40480-0c96-11eb-8012-7a9f14da5c38.png)

  - Identify the clusters, and derive what's meaningful

  - In terms of what program they were watching – fictional/ seriousness
    etc and plot probability on top of it

  - Which of the conditions are gonna be the part of the triggers – has
    to be limited

      - Then how many people from this cluster shows those conditions
        together to identify probability

  - If a new user comes you assign them based on the model

  - it shows diff domains; There could be overlaps, hierarchical cluster

**Apply stereotypes in a student ECoach – which is appropriate**

  - From the beginning of the module, enter the module, goals,
    motivation etc

  - Q - Asking experts or obtaining stereotypes from data? What would
    you choose could be a sub sub exam q

      - Asking experts

          - Can ask personal tutors and get the categories – student
            support, skills support can tell a lot about it

      - Obtaining from data

          - Privacy concern – due to data collection

          - \- won't be able to collect the data – availability

          - \- can't re-purpose the data – need consent to use the data
            for stereotyping

**Resolving stereotype contradictions**
  - ![image](https://user-images.githubusercontent.com/33334078/95708275-c97d6c80-0c96-11eb-8155-6123968789dd.png)
  - Can have general vs specific

      - E.g. Undergrad student and student

      - **Specific** can inherit from generic

  - BUT what if there's a **contradiction**?

      - If its specific, generic you take the **specific**. More insight
        for that group

  - E.g. How our stereotypes could be put into relationships -
    **contradictions**

      - Slightly to be <span class="underline">professional</span> and
        slightly to be <span class="underline">married with kids</span>

      - will produce same facet and value with two different rating

          - Rule of thumb: decide priority. Then exclude other

          - What is the necessary condition & default condition?

              - Default – if they are professional, they travel regular

              - Discrepancy – ask the users to see what the distinctive
                value that triggers both conditions

                  - Make the user select the condition and give info
                    accordingly - Choose btwn kids or professional

      - when there is contradiction esp if you are learning from data,
        you need to take a strategy

      - Not union?

          - By default you can, but you won't please either of them. Not
            relevant to nowhere

**Stereotype tuning**

  - We tune rating and the values

  - IF

      - If evidence shows that the predictions based on stereotypes were
        correct should be preserve for the future

      - NOT correct should be amended in the future

  - You are preserving what's happening, and you are constantly
    recommending something –

  - Need to think of what you are tuning

      - Have to tune trigger

      - Rating

      - Facet

  - How? Done by asking human AND data as you learn from historic data,
    so you can look at **new data**

**Summary of stereotypes**

<table>
<thead>
<tr class="header">
<th><strong>Advantages</strong></th>
<th><strong>Disadvantages</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Quick and fairly straightforward method for making assumptions based on limited observations</p></li>
<li><p>Applicable and used in a variety of domains</p></li>
<li><p>Quick and easy to implement</p></li>
<li><p>Allows dealing with cold start – broad user profile; direct connection with classification algorithms</p></li>
</ul></td>
<td><ul>
<li><p>Reliability – facet values and ratings are critical and are subjectively assigned tuning algorithms are crucial</p></li>
<li><p>Individual differences not properly catered for</p></li>
<li><p>Ad-hoc approach to resolving contradiction problems</p></li>
<li><p>Can lead to bias, if obtained from under-represented data</p></li>
</ul></td>
</tr>
</tbody>
</table>

11. ## **Recommender systems (Part 1) – Content-based Recommenders**

12. ## **Recommender systems (Part 1) – Content-based Recommenders II**

**Schema of user adaptive systems**
  - ![image](https://user-images.githubusercontent.com/33334078/95708291-d601c500-0c96-11eb-9b81-1c9ea7d4e561.png)

  - How to decide given this user model, what to give to user

  - Narrowing down the info space so that we can give it to the user

      - Not so much about the interface – but more of WHAT to give

  - \!\! Read the conference recommender sys

**Recommender systems: intro**

  - Problem: Too much **content** and **choices**

      - You want to direct the user and narrow to one or two arrows and
        to not overload the user the simple view of what the recommender
        system is doing

**Recommender systems**

  - Families of the recommender system – to give an overview of algorithms
    of the recommender sys

  - **Content-based recommenders**

      - Need to know about the content we are recommending Need
        representation of the content

      - Either have to obtain content and have an algo to analyse the
        content

      - E.g. email filer – need to know the content of the email,
        whether it should be filtered or starred

      - E.g. clipping services – how to cut the part of the content –
        just need to read about the simple things

  - **Knowledge based recommenders**

      - Also need to know where to direct the user to

      - Also brings in <span class="underline">external world
        knowledge</span> – so that you can be more precise about
        recommending

      - If I have additional knowledge of cars, that basis and the
        knowledge will become content and knowledge-based recommender

      - E.g. buying guides for houses - If in addition to that you bring
        the world knowledge of types of objects, proximity to public
        services and etc,

  - **Collaborative or social filtering**

      - It looks at social behaviours what other people has been doing –
        looks at attention of the others – and recommend what other ppl
        may like

      - E.g. amazon’s suggestion lists, top n offers and promotions

  - **Hybrid recommenders**

      - Clever way of hybridizing the algorithms

      - If you have social data, you combine with content

      - Combine content and knowledge etc

**Content-based Filtering**

  - So much content, and we want to narrow the choices of the user

  - If we want to develop content based filter, you need **two things**
    in advance to be existing so that you can develop

    1.  **Content**

          - Appropriate information about the content so that you can
            map to the content

    2.  **User** **profile**

          - Need to know who the user is – good description of the user
            so that you can map the content to the user

  - Then you can decide how each of the content is gonna map to the user

  - Not only the user model, it has to be related to the content I'm
    showing

      - E.g. cars – and if you have the user model about the student
        grade, its irrelevant\!\! Need to know what kind of car, what
        brans they are royal to etc

  - Correspondences between the user profile and what you know about the
    content

  - <span class="underline">Analogy: give me the content that I would
    like</span>

**Content-based filtering II**

  - Recommendations based on the correlation between the content of the
    items and the user’s preferences

      - E.g. recommend items similar to those I have bought or to my
        interests

  - **Connection w the prev lectures – user models/ profiles**

      - Need to know how to extract the **user models –** explicit and
        implicit methods

      - To come up with a more plausible **user profiles** or **user
        stereotypes**

  - **Description of the content**

      - It has metadata of the description of the content

      - Or think about ways of generating description from content
        information

          - AI algorithms – **classify the content based on key facts**
            – e.g. news about healthy living, politics, etc

          - May need to do that if the news don’t have predefined tags

      - Key challenge – what if you have **subjective opinions** in the
        content without the metadata. How do we classify them?

          - E.g. post on sns – no metadata that describes what's in the
            actual content. And you need to recommend the user the posts

          - E.g. how we book things – review – is subjective content.
            And recommend two or three reviews. Need to go into the
            reviews and see what makes a good review.

              - Processing that content and identifying textual
                features, then decide whether that’s a good review or
                not.

              - E.g. Amazon – how much do main content does the review
                has? Good rating coz good description of the product AND
                the helpfulness index.

                  - Challenge w helpfulness – very little people give this
                    info – skewed data

          - E.g. videos and podcasts – if no metadata, can I actually
            look into the content to bring in more?

  - Need to think these before you go into the algorithms core part

  - Correlation btwn the content and the user

**From the prev lectures**

  - How can we represent the user model?

      - Table with set of **keywords** – using TFIDF

      - **Facets, values, ratings** – stereotypes and categories

      - **Concepts** - list of concepts taken from graphs

      - A **graph** and overlaying graph models

  - Need to bare in mind that the input is one of those and how our alog
    will take these into account

**Architecture of CBF**
- ![image](https://user-images.githubusercontent.com/33334078/95708312-e31eb400-0c96-11eb-9825-98332f3a305c.png)

1.  When the user interacts through the interface,
    you have a clever way of **obtaining the user model** – through
    <span class="underline">explicit</span> by asking the user and
    <span class="underline">implicit</span> by analysing the interaction

2.  Then you have to have a **description of the content** – do I have
    the description? Is this reliable? Anything else I need?

3.  **Content filtering -** Do you have the areas of the content? There
    has to be a correspondence

4.  **Recommender** then takes the description of the content and the
    user model then starts **recommending** – identifies the one that is
    most relevant to the user

5.  May consider **user** **feedback** and to change it, and continue
    with the recommendation

<!-- end list -->

  - Q: HOW can we do the recommendation?

#### **CBF when user model is based on keywords**

  - **User model -** Assume that our user model is using the
    **keywords** (t1,t2,t3, … ) – have list of words from user profile
    that they are interested in, and we need to find the **weights** for
    each of the keywords

      - For each of the terms, what are the weights

      - ![image](https://user-images.githubusercontent.com/33334078/95708337-f03ba300-0c96-11eb-81f2-e491f4e33226.png)what we know about that **ONE** user in
        terms of term \#2?

          - Wishlist, clicking, etc then we have to identify the weights
            through TFIDF

      - Match u1 with t1 and so on

  - **Item vector**

      - For each **item in the content** we have to get a vector that
        corresponds to that term

      - ![image](https://user-images.githubusercontent.com/33334078/95708351-fc276500-0c96-11eb-987b-9c45122ef588.png) target terms, and how relevant those terms
        are to the item – for one

          - There are multiple items in one content

          - How close is this item form what the user wants
            **similarity**

      - item, we have w1, w2 etc – how relevant this item is to the term

  - How to identify the key terms and come up with numeric values for
    **users and for items** how we come up with the weights

  - The weights the input for the algo for the Content based filtering

  - **Calculating similarity**

      - The similarities between the two vectors of the same size

      - ![image](https://user-images.githubusercontent.com/33334078/95708372-09445400-0c97-11eb-9bc0-715543ac9303.png)How close two things are together

      - Remember cosine similarities

**CBF when user model is based on Keywords II**

  - ![image](https://user-images.githubusercontent.com/33334078/95708396-12cdbc00-0c97-11eb-98f3-5b686d90ffa4.png)

  - For the first term, it has weight w11, for second term, w12 etc

  - The items are now the input to the recommender

  - How close the user is to the items

  - **Items to recommend:** sort it by similarities and take top k items

**E.g. How can we personalize student news feed? - Keywords**

  - ratings

      - 0 – term not relevant

      - 1 – somehow relevant

      - 2 – highly related

<!-- end list -->

1.  Identify the **terms**

    1.  (study (t1), sport (t2), well-being(t3), volunteering (t4), IT
        Services(t5), union(t6), equality & inclusion(t7)

2.  **User** – how interested the student is, to mentioned ters

    1.  you = (1, 0, 1, 2, 1, 0, 1)

3.  **Item** – how related the news items are to the term; so we take
    **one item PER item for each item vector**

    1.  I1 = (1,0,2,0,0,1,1)

    2.  I2 = (2, 0, 1,0, 0, 0, 1,0)

    3.  I3 = ()

    4.  In

4.  So we do similarities between User you and I1, you and I2, you and I3.
    Then we sort it, take top items that are the most similar match up
    user with each item vector

<!-- end list -->

  - Q: how do you come up with the terms? How do you come up with the
    user preference?

      - A: we do **explicit profiling** – we ask the users to input the
        values

      - And **implicit profiling** – what news user is clicking on

      - You can improve the User preference that was given by the user,
        with results of implicit profiling

#### **CBF when user model is based on Facets, values, ratings**

  - We start with the simple stereotype, and combine several stereotypes
    to come up with an inferred user model

  - **User model**

      - User model is values, facets and ratings that are relevant to
        the content

      - With facets AND values, we can specify it more now

      - User model is obtained from stereotypes which gives some facets
        with values and ratings.

      - you = (\<u1v1r1\>, \<u2v2r1\>, ..) - values and ratings related to
        the content

      - **U = (\<study, UG, 0.7\>, \<study, full-time, 0.7\>, \<sport,
        team sport, 0.8\>, \<well-being, food, 0.5\>)**

  - **Item representation**

      - For the item, we need to know whether specific values hold for
        the facets

      - I = (\<f1v1i1\>, \<f2v2i2\>, …) - facet, values and item
        relevance

      - **I = (\<study, UG, 1\>, \<Study, MSc,0\>, \<study, phD,0\>,
        \<study, full-time,1\>)**

  - Q: Now I have the user profile and description of each of the item.
    How do I match up these two?

      - A: Relevance with user and item

  - **Calculate Relevance**

      - Need some mechanism to calculate the relevance between you and I

      - !![image](https://user-images.githubusercontent.com/33334078/95708414-1feaab00-0c97-11eb-964b-5301ed309a8f.png) rating \* item

      - So calculate 0.7 \*1 + 0.7\*1 + …

      - You have a representation of the user and the item, and you need
        a clever way of doing so

**E.g. How can we personalize student news feed? – Facet, Values and
ratings**

  - We need to decide what the facet and the values are

| **Facet**              | **Values**       | **Rating** |
| ---------------------- | ---------------- | ---------- |
| Study (f1)             | UG (v11)         | 0.7        |
|                        | MSc (v12)        | 0.7        |
|                        | PhD (v13)        |            |
|                        | Full time        |            |
|                        | Part time        |            |
| Sport                  | Team sports      | 0.8        |
|                        | Individual sport |            |
| Well being             | Food             | 0.5        |
|                        | Mindfulness      |            |
|                        | Activities       |            |
| Equality and inclusion | Gender           |            |
|                        | Ethnicity        |            |
|                        | Sexuality        |            |
|                        | Neuro diversity  |            |

**CBF when User Model is based on Facets, Values, Ratings (cont)**

  - ![image](https://user-images.githubusercontent.com/33334078/95708666-d2bb0900-0c97-11eb-856c-5243eb5dfb61.png)

  - We have the user, U, with user, value and ratings

  - We have items with facet, values and item relevance

  - Recommender calculates the relevance between the you and each of the
    items I1,I2, Im etc
  - Recommend top k


#### **CBF when user model is based on Graphs/ concepts**

  - **There's a graph representing the domain model**
  - ![image](https://user-images.githubusercontent.com/33334078/95708683-dc447100-0c97-11eb-932b-de9c4be26981.png)

      - Concepts and links related to the content

  - You can have more knowledge about the facets, more value tuned, it
    can be more spec

      - Team sport – what kind of team sport?

  - It is a taxonomy, explaining various relationships – which gives a
    hierarchy and it allows to connect things

  - **User model**

      - you = (u1,u2,un)

      - We would know what is relevant to the user blue is relevant

          - We have derived the positive hit of the user

  - **Item model**

      - I = (c1,c2,cn)

      - What I know about the content; What item is the most relevant

  - I have overlaid the user model on the content model (item model),
    and now I need to decide what that I overlaid on the graph is
    related

  - Cleverness comes in here

      - Can think about similarities, similarity could be the part in
        the graph – if they have the same parent, OR they are similar bc
        one is a parent and one is a child node

  - How similar the red dots are to the blue dots

**CBF when User Model is based on Graphs/Concepts II**

  - ![image](https://user-images.githubusercontent.com/33334078/95708736-f9793f80-0c97-11eb-8692-3c6c140e90f4.png)

  - Red – items with concepts

      - Could have overlaps between different items

  - Once you have both, calculate the relevance, sort it then recommend
    it

**Pros and cons of CBF**

  - **Pros**

      - It focuses on just the user

      - Fairly easy to implement – once you have managed to obtain user
        and content description, can easily compare

      - 매우 중요Can explain to the user why they are recommending this – bc
        I have this facet and value, and that it is related to the
        item’s ratings

      - Applicable in a range of contexts

          - News

          - YouTube – you watch one video and they show you more of them

          - Travel recommendations

  - **limitations**

      - Computationally complex - there are too many checks;
        similarity/relevance

      - Filter bubble – it might be too focused; it forces user into
        that one category

      - Cold start – you don’t have a user model to begin with

      - Reliability of user profiles – it relies on the user

      - Requires content description – facets, and have to do initial
        tagging; have to extract it automatically somehow

**Improve Efficiency: other factors**

  - **Novelty/ surprise** of an item

      - Existence of information that is new to the user (e.g. in
        learning, video streaming

  - **Proximity**

      - The number of links it takes to navigate from the current page
        to the page with the item

  - **Context relevance**

      - How relevant is the item to the current items the user is
        interacting with (e.g. in news recommender systems)

**Summary: content-based filtering**

  - CBF was the first recommender systems that is used in a number of
    practical applications

  - Focus on the user – builds on user profiling \&Need description of
    content

  - Main advantage – explanation of recommendations

  - Main limitation – filter bubble

## **Recommender systems (Part 1) – Knowledge-based recommenders**

**The CHIP Project - bridging the gap between virtual and physical
museum experience**

  - Rijksmuseum Amsterdam offers

      - 7000 artworks in the museum

      - 50000 artworks online

  - They have broad pool of users – schools, students, normal people
    have everything required for recommender system

**Vision: Personal museum guide in your pocket**

  - They decided to work together with the scientists and was looking at
    how people go through this massive

  - Need to come up with a vision when creating the project – what will
    you add to the user experience

      - Came out with the idea of **personal museum guid**e – When you
        go to a museum you can have a personal guide and the guide
        creates a narrower museum

      - \- But doesn’t scale and not tailored to various types of users

      - Take the metaphor of having a personal guide and develop a
        mobile guide

  - What will a guide be? What do they do? Features of guides

      - Personal guide knows about the artworks and paintings – has the
        domain knowledge

      - Ability to identify what user might be interested with, from
        limited interactions

      - Can recommend paintings and explain based on what they know
        about the world and the user

**CHIP tools**

  - What are the personalisation features?

  - When you are in the digital space, online mostly have recommender
    systems

      - **Art recommender -** You look at one painting and it shows
        other thing to see and recommends you painting and information

          - artworks and art concepts recommendations

      - **Tour wizard -** In the virtual space, they can give you a tour
        guide – not just one painting, but shows sequels of paintings

          - managing and visualising museum tours

      - **Mobile museum guide -** As a mobile museum tour guide –
        identifies where you are in the museum

          - guiding the user inside the museum

**Knowledge Graph: Semantically Enriched Museum Data**

  - ![image](https://user-images.githubusercontent.com/33334078/95708763-0f870000-0c98-11eb-990f-e134cfd54c58.png)

  - Behind this system – knowledge based.

  - First component before developing personalised app, is the
    **knowledge**

  - Snippet of the knowledge model – computer scientist together with
    curators worked together to identify the core knowledge required for
    painting rec

  - They used **concepts** – graph-based models – and concepts are
    linked with relationships and relationships are named

      - Creator has place – birthplace and deathplace

  - Have implicit relationships - Once you have the knowledge base, you
    can infer

      - Can infer style of the author, painting etc bc there's a
        connection

  - Powerful knowledge model that tells about the world but this is NOT
    the recommender. Now need to bring this to the recommender

**Discovering connections via reasoning**

  - How can you bring this external knowledge to help you to explore the
    paintings

  - Based on the metadata mapped with the external knowledge, you can
    bring other paintings bc they share some similarities with the same
    metadata

      - Having the knowledge model allows you to bring the content to
        filter what the most relevant is to the painting

  - Eg

      - Painting has relation to other 2 painters (teacher, student etc)

      - Painting showing portrait, military scenes etc

      - Exploring all different aspects by looking at one painting, due
        to the relationships

      - Not personalised, but it enriches the space

  - Can talk about much smaller pool to recommend to the user. Still
    need to evaluate what's relevant to the user user model comes in.

  - Then you need to think about mapping the content and the user model

**User profile building**

  - Problem with cold start – need to know about the user and map the
    user to the content

  - How you gonna create the user profile?

      - Can look at the browsing history of the user and rate the things

      - But in the first instance, when user enters the system, gotta
        know where – this case they ask **explicitly** to rate the
        paintings.

      - It is not random paintings; it is selected in a way that diff
        area of the knowledge graph is being identified

  - Gives user model and we think you’d be interested in these topics –
    all that is the top categories under the knowledge model

      - End up with showing the user a list of keywords that they are
        interested in

      - It can tell me **why**\! Based on which rating and why has it
        inferred that I might be interested in x

  - Cold start is solved by **explicit rating** ‼

  - Use model now has = graph of user interests + graphs with painting
    information - overlap

**Art recommender**

  - They are looking at similarity metrics

  - They have to decide if this painting is gonna interest the user –
    how similar this is to user parameter

      - How you map user model to the painting model for each of the
        painting

  - And based on that it decides how its gonna recommend – it shows the
    **relevance** of the painting

      - All the descriptions of the painting and some weight, to what
        extent it is related to the user (which user already approved)

      - You can map directly the user characteristics; but you can look
        further - How much you are propagating with thin the graph,
        given the concept about the painting within the graph

  - Also recommends other artwork that is related to the PAININTG not
    the user – give diversity but still relevance

**Artwork description**

  - Once you have the knowledge, can automatically generate description
    of the painting with the metadata

  - Then decide within the description, what to show as important and
    what to suppress another level of personalisation ‼

      - Knowledge model allows to do that as it identifies parameters
        and it amplifies the important info more

  - Knowledge allows:

      - To describe **why** something has been recommended

      - Allows you to diversify and to recommends other paintings

      - Allow you to automatically generate description that is tailored
        to the user (CBF won't allow this)

**Summary: Knowledge based filtering**

  - Need to get a good knowledge graph to implement the recommender

  - They build on content-based filtering – user profile and information
    about the content

  - But to bring in the **knowledge model of the world**

  - Content, user AND knowledge – powerful

  - Main advantage - reasoning\!\!

      - You can infer things – and user tend to trust the
        recommendations that way

      - Can diversify experience

  - Main limitation

      - We still have the cold start problem

      - Need to prepare the content and mapping

  - Without the knowledge, can't do the recommender\! Time to get the
    knowledge and to map the knowledge

      -
## **Recommender systems (Part 2) – Collaborative filtering**

10.3.20

  - Google - It assumes you are looking for the flight hotel and stuff

      - Uses location too

  - Spotify – content-based filtering – based on what you listen to, it
    gives you more of that

  - YouTube – content-based filtering – based on what you watch, gives
    more of that

**Collaborative filtering**

  - Same problem – too much content and user has too many choices – how
    do we narrow the choices and give users the right things

  - In collaborative filtering:

      - Need to look at **other people’s consumption.**

      - Also need to have what the **user rates and** likes as well

  - → give me what people similar to me would like

**Collaborative filtering CF**

  - Based on **user similarity** – it tries to find similar users and
    based on that recommends it.

      - You may also like this as well, people like you preferred this

  - Key challenge – the rating, where does this come from?

  - How to find the ratings or preferences of the user

      - Explicit methods - Can explicitly ask the user to rate –
        Netflix, amazon

      - Implicit method – observing what user is doing, e.g. what they
        buy, click, visit – gives additional info to user rating

  - We are observing **every user in the system** based on either
    explicit or implicit methods

      - This is the input of the system

**CF – how does it work?**
  - ![image](https://user-images.githubusercontent.com/33334078/95708791-20377600-0c98-11eb-919b-13e6161144f3.png)

  - Steps

    1.  Creating user profile and created ratings for items

    2.  User modelling component is, based on the user profile
        Identifying who are the users – who’s similar to my user

    3.  Take items which they liked – and recommends it

    4.  User gets the recommendation back

  - If we want to build a CF, which is based on user similarity →
    user-user filtering

      - How you process the input data to come up w the user

**Step 1 – Represent input data**
  - ![image](https://user-images.githubusercontent.com/33334078/95708811-2d546500-0c98-11eb-899b-012da6a0fed5.png)

  - First step is to **prepare the input data** – usually a matrix.

      - Have all the possible items and users of the system – matrix
        values that indicate the voting of user 1 and item 1

  - You end up with a large matrix where you indicate for the ones you
    know, whether they liked it or not

  - **Numerical values** in the matrix – can decide on the scale as
    well. i.e. 0-1 or 0-5

  - Biggest challenge

      - Creating the input matric in advance – identifying what data you
        have about the user to come up w the numbers – if you ask user
        to rate, a lot will be empty coz they don’t rate everything

      - Think about other ways of collecting info

**Example**

  - Identifying what we gonna recommend by rating each item for each
    user

  - I they’ve liked item 1, 5,7, hated 2,6 → which should I recommend?

  - How do we apply the user-user filtering to come up with the rating
    for an unknown cell\!\!\!\!

**Step 2 – Find nearest neighbours**

  - We need to find similarities across the users and then define the
    **neighbours** that are the most similar

  - How to find similarity → **cosine similarity**

  - Sometimes referred as: **K-nearest neighbour user-user collaborative
    filtering**

**Step 2.1 – Calculate similarity**
  - ![image](https://user-images.githubusercontent.com/33334078/95708903-70aed380-0c98-11eb-9bd7-e443b8b85451.png)

  - Similarity between our user and all the other user –

  - E.g.

      - U3 = (5,1,?,4,5,0,5)

      - U1 = (5,3,?,1,3,4,0)

      - We looking for the **? part**

      - Sim (u3,u1) = ![image](https://user-images.githubusercontent.com/33334078/95708869-5e349a00-0c98-11eb-9b5c-f3c80150a788.png)


      - Sim = 25+3+4+15+0+0 / (sqrt(25+1+16+25+0+25) \*
        sqrt(25+9+1+9+16+0))

  - Question – if u3 = (5,0,0,0,0) and u1 = (0,1,0,0,0,) what do we do?
    → neighbour


**Step 2.2. Define neighbourhood**
  - ![image](https://user-images.githubusercontent.com/33334078/95708911-79070e80-0c98-11eb-8756-e1ad7ce93959.png)

  - How to take neighbourhood given the users and similarities between
    them

  - **Centre-based neighbourhood (size n)**

<!-- end list -->

  - → Sort them and take top n

  - K = 3, so top 3 in this case.

      - 0.93, 0.71 and 0.63 is the most relevant, U6,U4,U1

  - Problem is when there's too many 0’s and there's no similarity

**Step 3: Predictions/ recommendations**

  - Now I know who the relevant user is, and we decide on the value.
    make predictions about the user

  - Q - I know we’ll take 0,2, and 4 (from prev. slide) do we take the
    weighted value or average?

  - **Weighted sum**
      - ![image](https://user-images.githubusercontent.com/33334078/95708926-82907680-0c98-11eb-8f7d-b6b29f482a24.png)

      - Scans the neighbourhood and calculates the frequency for each
        item

      - Can be combined with the rating value

      - we calculate the **weighted sum**. and we are dividing by the
        SUM of the 3\!\!\! So (0.63+0.71+0.93)

      - Based on this we decide if to recommend this or not

  - **Association rule recommendation**

      - Expands the number of items based on association rules upon what
        has been recommended by the neighbours

**Pros and cons of user-user CF**

  - **Limitation**

      - **Data sparsity** – with user that hasn’t stopped much with less
        indication, will have a lot of 0. We then have a very small user
        base

      - **Individual characteristics are not catered for** – the user is
        just vector of numbers

      - Tends to recommend **popular items** – the AI will be biased bc
        if the item has had a lot of attention, e.g. with unrepresented
        items, it will have a lot of zeros → Will be pushed away.

          - This way we end up converging around few items

      - **Privacy and trust** become important issue

          - Netflix uses user-user Collab filtering – they were testing
            their algo – by exposing data, you could guess who the user
            is, even if they are just numbers when it becomes niche data

          - We can mitigate this by getting rid of user and just doing
            items\! next topic

  - **Pros**

      - It allows diversifying user experience, by getting **out of
        filter bubble**

      - Fairly easy to implement

      - Widely applicable – popular in social media applications

      - Starts looking at social interaction data

      - Can recommend items that are not linked to the user’s earlier
        choices → Useful for promotion – promoting new things and
        surprises the user

      - Considers the opinions of wide spectrum of users


**Item-item collaborative filtering**
- ![image](https://user-images.githubusercontent.com/33334078/95708951-920fbf80-0c98-11eb-9816-4c132c165553.png)

1.  Get the users and other users.

2.  Look at the items and find similarities between the items (not about
    the users)

3.  Based on the items, find the neighbourhood of the items

4.  Then recommend

<!-- end list -->

  - Now we are looking for items, rather than the user

  - We prepare the matrix with user and item the
    same way.

**Item-Item collaborative filtering**
  - ![image](https://user-images.githubusercontent.com/33334078/95708975-a358cc00-0c98-11eb-8191-2228ba3c448d.png)

  - Item that I need to think about = I3 = (0,1,?,2,1,4)

      - I1 = (5,1,?,4,0,3)

      - Sim (I3,I1) = 0.62 → **cosine similarity**

      - We do this for item 3 and every other items – I1,I2,I3, etc

  - Find the most similar 3 items – then take the weighted sum

  - Most similar is I4, I5, I7 – then we come up with the **weighted
    sum**

      - ![image](https://user-images.githubusercontent.com/33334078/95709047-c5524e80-0c98-11eb-8147-215ca4fd324b.png)


**Discuss the results: 2.62 vs 4.62**

  - We got 2 diff values from **user-user** and **item-item**

  - Q - Which do you trust more?

      - Can't decide. Can have diff recommendations and you will come up
        with diff values.

          - If we change the neighbour k = 4, the value will be diff

          - If we don’t use cosine similarities, it will be different

  - Can we trust these values?? **evaluation** is important.

      - We take several algo and benchmark them to find out what gives
        the best result

  - Not just coming up the number, but we need to **evaluate** them we
    need hybridization of algorithms

      - Precision, recall etc

**Scalability problem**

  - Calculating similarities of one to every one another, is the most
    **computationally heavy.**

      - > Identify where the problem is over-calculation of similarity
        > in this case.

        1.  > **Reducing the space of calculation -** May try to
            > categorise the items and compute similarity

        2.  > **Offline calculation** – we pre-calculate these and store
            > it, and when user comes it uses that to compare.

              - > \- Problem is updating db. Could lose some data during
                > a week or so

              - > \+ when the user item is big, its very fast

**E.g. Amazon item-item collaborative filtering –
to address scalability**
  - ![image](https://user-images.githubusercontent.com/33334078/95709061-cdaa8980-0c98-11eb-8d91-b56041a3cc14.png)

  - With this sparse data, instead of doing the whole calculation

  - No need to do multiplications of 0.

**Step 1. Find customers who have purchased the items u3 has purchased**

  - We narrow down to other users who have bought that – THEN we
    calculate **THEIR them** (with 1’s) instead of all users

      - user 3 bought item 1 – u1 and u4 also bought this

      - user bought item 4, - u2, u4 bought this

  - → Algorithm is trying to reduce the item space

  - With thousands of items, we will **significantly reduce the items of
    interest** – in this e.g. not so shown coz i3 is the only irrelevant

**Step 2. Find items bought by these identified customers and register
pairs of items**
  - ![image](https://user-images.githubusercontent.com/33334078/95709100-e3b84a00-0c98-11eb-9645-7db7e3e2b1cf.png)

  - Now we start to look at similarities – we need
    to reduce the number of similarity calculation

      - We register pairs based on common purchases of items.

  - Register pair with regards to common items

  - Have user 3. Found that U3 has similarity with u1 as they bought one
    similar item → so by comparing u1 and u3, we calc:

      - ![image](https://user-images.githubusercontent.com/33334078/95709131-f763b080-0c98-11eb-8655-04091dfd6302.png)


  - By reducing the search space, only need to calc 4 to find the most
    similar

**Step 3. Calculate similarity between user items in pairs & recommend the most similar**
  - ![image](https://user-images.githubusercontent.com/33334078/95709147-0185af00-0c99-11eb-9eca-e545f164a5bd.png)

  - Sim between u3 and the rest of the item, and find out what's the
    most similar to that. Then calc the similarity from the pairs

  - We have reduced space

  - Cleve – we look at the user, narrow the search space AND narrow the
    comparison

      - Reduction in less **item** and less **pairs for comparison**\!

**Collaborative filtering summary**

  - Pros

      - Fairly simple to implement

      - Widely used in recommender systems

      - Works successfully if large dataset is used

      - Facilitates the exploration of long tail, which is not otherwise
        addressed

  - Challenges

      - New items, new users – **cold start**

      - If an item has 0000 it will never be recommended

      - **Sparsity** – space of data and ways of reducing

      - **Scalability** – large dataset, but we can reduce it

      - **Reliability of ratings** – it is prone to subjectivity\!\!
        **Bias\!\!**

      - **Lack of transparency** – how did you come up with this rating?
        Explaining to the user

      - **Lack of control** – limited user influence on the algorithms

**Apply collaborative filtering** → know how to apply \!\!\!\!\!\!\!

1.  Represent data

2.  Define neighbourhood

3.  Make predictions or recommendations

## **Recommender systems (Part 3): Hybrid Recommenders**

**Hybridization**

  - Several algos giving diff results – way to combine several algos

  - First part of the lecture

      - How to put it next to each other to decide how you gonna
        hybridize

      - Fundamental models behind the recommendations

  - Second part - Actual hybridization method

  - Group

      - We have individual model and how to decide what's the best for
        the group

      - Aggregation strategies

**Content based filtering**

  - You need to know about the user and the content – represented in
    some form

  - You are gibing the user what they might like

  - E.g. checking discovery modules

      - What topic, what students are interested etc

**Collaborative filtering**

  - Only if you have collected how other people have interacted and made
    choices

  - Based on how other people have chosen, It helps you recommend it –
    no need to know about the content

**Sources for recommendations**
  - ![image](https://user-images.githubusercontent.com/33334078/95709168-1104f800-0c99-11eb-84f2-4f31bf172e2c.png)

  - Now taking the decision which algo to use – its not straightforward
    what to choose.

  - Do you have enough as an input?

  - When thinking what sources you have – social, individual, and the
    content

  - Social

      - Rating, tags – what they’ve said

      - Reviews – what people liked and disliked

      - Behaviours – aspects of what the watched, voted liked etc

      - Demographics – age and where from, about the crowd

      - Context – where was the movie watched, as a group etc

  - **Bare minimum to run social filtering - is the opinion 여러번말함**

  - Individual – what do you know about individuals

      - Opinions – rate a few movies, and give more precise

      - Behaviour – on the weekends, they watch relaxin jazz

      - Demographics – age, nationalities, place

      - Requirements

          - Query - what they are looking for

          - Constraints - they have mobile and desktop etc

          - Preferences – customisable model

          - Context – how much do we know and how reliable is this

  - Content based filtering – **minimum is the behaviour or the
    demographic**

  - **Content**

      - Item – I need to haves some description – paper- where, by who,
        how long etc

      - Domain knowledge – about the world

          - What sources do I have and how reliable are they

          - Temporarily dependent data – like music taste etc, when
            you’ve been to the hotel and it still recommends you it

**Recommender algorithms – key**

  - Need to have a systematic approach on combining different ones

  - What are the key sources ??

  - When. I'm developing, what are the features I should bear in mind

      - **Background data** – before you start any of the processing –
        prev slide

      - **Input data** – when the user is interacting with the system,
        what data I capture about the user. What does user need to
        communicate in the system

      - **Algorithm** – combining that input data and background data to
        arrive at suggestions

  - Should be able to: describe what background data, input data and
    algorithms would you use??

      - In that context, before

      - Maybe like exam - In discovery module, HOW would you do content
        based it?

          - Background - what courses you've done in the past

          - User input -

          - Content based algorithm

      - No input, but past behaviour maybe

**Comparing recommender algorithms**

![image](https://user-images.githubusercontent.com/33334078/95709202-2417c800-0c99-11eb-9c59-382aa1dfc854.png)


  - Utility – what is the benefit for the user? And it recommends the
    most efficient or the best choice

      - Best decision – important for doctors in diagnosis

      - People be happy

**Pros and cons of recommender algorithms**

![image](https://user-images.githubusercontent.com/33334078/95709218-2c700300-0c99-11eb-9a6c-f924ad5a92e4.png)

  - Algo in particular context and you need to point out strength and
    weakness of algo

  - K - Gray sheep problem – user does not fall in any existing cliques
    of users

  - M – need to recalculate the thing again and again

**Hybrid filtering – netfiix video**

  - Netflix video - Target was precision – to fulfil that 10% gap

  - Everything can be reduced into data, which is turned into data and
    mathematical models to predict movies you like

  - System relies on collaborative filtering – user into mathematical
    models which spits out other things

  - 10% improvement over current thing

  - Method

      - Analysed the dataset – one rating pursuer?

      - Looking for patterns in the data – whole different techniques

      - Singular value decomposition- characterises each movie and user
        into vectors, in 2D

  - Applying many diff models and averaging it gave the best performance
    to reach the 10%, gotta collaborate with diff teams

  - One problem – with some movies have very polarising movies with diff
    variance of rating

      - Napoleon dynamite – 1 and 5 rating

  - **Average of 800 diff algorithms omG**

  - When you have massive population of algo, but if not it might not be
    suitable

  - They’ve analysed the strength and weaknesses of each algorithms to
    use it accordingly

**How to combine? Hybridisation algorithms**

  - For each algorithm, it produces different recommendation – so how do
    we combine them??

  - Netflix took 800 and took the average in the second round. In the
    first round they analysed all the algorithms

  - ![image](https://user-images.githubusercontent.com/33334078/95709236-3560d480-0c99-11eb-903b-93293e0ddf68.png)


<!-- end list -->

1.  **Weighted**

<!-- end list -->

  - **The scores (or votes) of several recommendation techniques are
    combined together to produce a single recommendation.**

  - Weight – gradually adjusts the weighing as predictions about user
    ratings are confirmed or disconfirmed

  - We have algorithms and for each of them we have weights attached to
    it. We need to examine which works in which conduction

  - If we have the weights, it simply computes the **weighted sum**

  - ![image](https://user-images.githubusercontent.com/33334078/95709270-47427780-0c99-11eb-9fec-272263472294.png)

  - Pro - All of the systems capabilities are brought to bear in an easy
    way

  - Con – relative value of diff techniques is uniform – so items with
    smaller raters will be weaker

<!-- end list -->

2.  **Switching**

<!-- end list -->

  - **The system switches between recommendation techniques depending on
    the current situation.**

  - Switching – you ask for an opinion and you decide to switch base on
    diff groups in diff context

  - Important to know what exactly is the context – what media, time,
    item user is using?

  - We have diff algos and depending on the user and the item, for one
    user we recommend R1 and for another item we recommend R2 or Rn.

  - Crucial is that we need a very good understanding of how each algos
    work and which is the best in the current context

  - ![image](https://user-images.githubusercontent.com/33334078/95709295-4f9ab280-0c99-11eb-897b-a9ce09bc83c9.png)

  - Cons – does not avoid the ramp up problem. Also for daily Learner’s
    model, the short term model is always used first and other comes in
    when it fails

      - Introduces additional complexity as switching criteria must be
        determined

  - Pro – system can be sensitive do diff algo’s strength and weaknesses

<!-- end list -->

3.  **Mixed**

<!-- end list -->

  - **Recommendations from several different recommenders are presented
    at the same time**

  - Users can make their own choice – they see recommendations from
    content based, knowledge based etc.

  - Diff algos return diff values, and for this user, we show R1 and R2

  - Crucial is to explain to the user, the results

  - Another crucial is that the recommendations shouldn’t be too controversial need
    coherence in the recs

  - ![image](https://user-images.githubusercontent.com/33334078/95709306-57f2ed80-0c99-11eb-8e14-df3cef41d5ea.png)


  - Pro – can avoid cold start problem, niche finding property

<!-- end list -->

4.  **Feature combination**

<!-- end list -->

  - **Features from different recommendation data sources are thrown
    together into a single recommendation algorithm.**

  - We are coming with one value, but we use diff data to come up with
    that one value

  - New algorithm which can combine features from all the outputs

      - One is weighted output.

      - More complicated to look at what feature is the strongest for
        that part. Algorithm

          - Click? Ratings?

      - Then you use the strongest feature from each one, and you put
        them in a one combined algo to come up with a better algo

  - ![image](https://user-images.githubusercontent.com/33334078/95709322-5fb29200-0c99-11eb-87c0-11a71173f5ee.png)


<!-- end list -->

5.  **Cascade**

<!-- end list -->

  - **One recommender refines the recommendations given by another.**

  - Run one algo, and get the output, then you take it and pass it to
    diff algos and so on, until you get the refined version

  - Run A1, then you get R1. Then put R1 to A2. Then R2 is put into A3
    etc

  - Usually works when we are considering all possible items, rather
    than one single item until we come up with most refined

  - ![image](https://user-images.githubusercontent.com/33334078/95709336-680acd00-0c99-11eb-91ae-8c62592e5694.png)

  - Pro – prioritizes the results of 2 recommenders → more efficient and
    tolerant to noise of low priority techniques

<!-- end list -->

6.  **Feature augmentation**

<!-- end list -->

  - **Output from one technique is used as an input feature to
    another.**![page7image50339712](media/image62.png)

  - Quite similar w/ cascade

  - We look at the features of each algo we gonna use

  - Take A1, and it gives R1. Then for second, we have diff features.
    But we still bring in R1 in addition to the feature \! so it acts as
    an additional feature so that A2 has **broader feature scope**

  - ![A screenshot of a cell phone Description automatically
    generated](media/image63.png)

  - Pro – offers a way to improve the performance of a core system
    without modifying it.

<!-- end list -->

7.  **Meta level**

<!-- end list -->

  - **The model learned by one recommender is used as input to another.
    Entire method becomes the input**

  - Taking output of one algo and put it to another

  - A1 gets R1. Also look at values from a set of items. Then you used
    that in some way as additional feature, input etc meta level, coz
    you need to think how the R1 is gonna be used cleverly as an input
    of A2

  - ![A screenshot of a cell phone Description automatically
    generated](media/image64.png)

  - Pro – the learned model is a compressed representation of a user’s
    interest and a collaborative mechanism that flows can operate o this
    info dense representation

**Summary**

  - **Comparison between methods** – identify pros and cons for each
    method in particular situations

  - **Key features of recommender algorithms**

      - Before you decide which algo to use, need to look at the input

      - Background data, input data, algorithm

  - **Hybridisation methods** – identify an appropriate hybridisation
    method to maximise the pros and minimise the cons of the combined
    methods given a particular app

      - Each of the hybridisation becomes a method on its own.

  - **Research trends**

      - Active research field

      - Research innovation route quite fast

## **Recommender Systems (Part 4): Evaluation**

  - How to evaluate recommendation algorithms

      - Mean truth square error, precision, recall etc

**Evaluation questions**

  - We need to decide the scope.

  - Single algorithm

      - Which parameter setting is better?

          - E.g. k-nearest neighbour. 2 or 10 neighbours?

      - What are the cases when the algo performs the best/ worst?

          - Netflix. And the gray sheep items movie napoleon dynamite.

          - very important when you analysing algo to know the strength and
            weaknesses to think of ways to hybridise or minimise

  - Several algorithms

      - Which algorithm performs best for the current circumstances? How
        to select/ hybridise based on strength and weaknesses?

  - Recommender system

      - What are the benefits and drawbacks of recommendations on user
        experience and business?

      - We look at the impact of the system on the user

          - E.g. for ecommerce – recommends, finds and leaves is good
            for the user, but not for the user bc it will be more
            profitable if the user is slightly confused if they buy
            items that they didn’t know they needed

  - Will focus on single and several

<!-- end list -->

1.  **Data driven evaluation – rating accuracy**

<!-- end list -->

  - For single or several, we use data-driven

      - ![](media/image65.png)Rec – p1 p2 p3

      - Actual – a1 a2 a3

  - If we look at the accuracy, we are looking at the difference between
    the two

  - **MAE** – mean absolute error

      - Diff between the actual and predicted and take **absolute**
        value. Then we take the average![](media/image66.png)

  - **RMSE** – root mean square error

      - Slightly more advantageous

      - Square of ai-pi – then we square root it

  - **Correlation coefficient**

      - Correlation between two vectors – p1 an da1

      - If we consider how close two vectors are correlation

      - Can rank the vectors within the items – for both vectors and
        find the difference between the ranking Pearson correlation

  - Would consider first two

**Calculate MAE and RMSE**

  - ![A close up of a white background Description automatically
    generated](media/image67.png)

  - How do we know if its good or bad?

      - A – we have a algorithm for baseline, and we are tryna get a
        value better than the baseline

      - Will be looking at diff metrics of the performance of the alog

**Compare recommender algorithms**

  - Compare more than one algos – metrics are becoming more meaningful

  - We’ve calculated the abs error and the MSE

  - Bad choice is when the prediction and actual differs by large

  - recommendation 1 \> rec2

  - recommendation 3 is not as bad as recommendation 2, but if we only look at abs error, R1
    and R3 performs the same. BUT if we have an extreme error, (a1-p1)
    \>4 this will impact the error bc we square it

      - This is why RMSE is higher

      - RMSE hence is preferred‼ bc it looks at the negative cases and
        considers it higher.

![](media/image68.png)

2.  **Data driven evaluation – usage prediction**

<!-- end list -->

  - Accuracy is a very crute measure of how well it worked – but it
    doesn’t tell us where it performed well. E.g what's the precision or
    recall?

      - We need to create a confusion matrix

      - TP – true positive

      - FP – false positive

      - TN – true negative – user and algorithm said no

      - FN – algorithm didn’t rec, but user used

  - ![A close up of text on a white background Description automatically
    generated](media/image69.png)

  - Given these values, it seemed to do better on precision

**Compare recommender algorithms**

  - How do we use these metrics to compare algorithm

  - Recall – it recommended everything it should recall – so 1 in recall

      - 0.5\<1

  - This is how we can compare – for many users, we can find the thing
    for individual users and take the average

**Beyond accuracy: coverage**

  - Beyond how algorithm could be – so we look at other values when
    assessing

  - Coverage – **what percentage of items can the recommender form
    predictions for**

  - **Coverage** is from WHOLE pool of item. If algorithm A does good
    but only recommends ‘easy-to-recommend’ items, it ain’t good bc its
    recommending popular items

  - Long tail – if it reaches the niche or stays in pop items

**Beyond accuracy: Novelty/ Serendipity**

  - Easy to recommend items that are common or what user is used to, but
    wat about something that user is not used to?

  - **Novelty** – something is not within the prediction, but is close to it
    hence will broaden the user experience

  - **Serendipity** – something new, but is a relevant and pleasant
    surprise

  - Collaborative filtering – novelty and serendipity is embedded bc its
    about broadening the user horizon with the use of the crowd

  - Is a Content based and knowledge based – can be calculated in
    algorithm by looking at similarities and differences in metrics.
    More sophisticated way bc it allows reasoning

  - → they are subjective metrics bc we need to see if the user was
    indeed pleasantly surprised

**Beyond accuracy: Diversity**

  - Data driven evaluation, **how diverse is the list of items we
    recommend?**

  - Variety – do we have from all content categories?

  - Balance – are the items from the categories proportional to the
    number of items in the categories

  - Disparity – how far are the items, note the relevance with
    clustering

**Experimental studies with users**

  - Evaluating the whole recommender system – we look at the impact of
    the system on user

  - AB testing – we have 2 systems with and without recommendations, and
    we compare them on pre-defined metrics

      - **Performance metric** based on user interaction – then we can
        use MSRE? Precision, recall, coverage, diversity etc as a
        performance metric

      - **Utility metric** – what was the benefit of the algorithm for
        the user/business

          - User satisfaction, how long user stayed, user loyalty,
            profit etc

  - Then we **compare** the values of the metrics – mean, median and
    mode

  - We also look at the **statistical significance** – it can perform
    better in some situation, which doesn’t mean that every time we have
    this test it'll perform better

      - Large dataset – can use parametric (t-test, ANova)

      - Not large – non-parametric methods

**Summary**

  - Evaluation is crucial

      - You need to think about this from the beginning, the evaluation

      - Consider the performance metrics and consider what you are
        evaluating (what aspect of system, whole system)

  - Data driven assessment

      - We mostly do data driven, hence do we have access to this
        appropriate data?

      - Careful, bc is there any potential bias or overfitting?

      - The data being small – which leads to overfitting

      - Similarity with evaluation of machine learning classifiers – can
        consider predicted value as a classifier

  - Experimental studies with users

      - To actually evaluate the system – AB testing

      - Can consider variations (e.g. one system but offers from two
        different recommender algorithms – check which performs better)

## **Group recommendations**

  - So far, we've studied about an individual user – how to acquire
    info, build user model and use this info to recommend appropriate
    items to the user

**What if the user is a group?**

  - We have to recommend for a group of people → one recommendation

  - Movie, tv program, restaurant, experience, house, TV, holiday to a
    GROUP

**Main steps**

1.  Obtain individual preferences – need a user profile/ model for each
    individual user

    1.  Content based – need to look at the parameters and put this
        within the user model

    2.  Social (collaborative) – we look for user’s interest and
        opinions about particular items

2.  **Aggregation strategies** – to aggregate and come up with one recommendation →
    focus of the lec

3.  Present the recommendations to the group with appropriate
    justification

**Example**

  - We have 4 users and 10 items

  - For each of the user, we have preferences for each item – 1 to 20

  -
  - Q - How would you select the best item?

      - A – with the highest score amongst many users

**Aggregation strategies: Average**

  - **Take the average for each item and take the item with the highest
    average**

  - If we want to recommend more than one, we take it in order

  - 10 /20 is a nice compromise for the group

  - Disadvantage – the users will be disadvantaged bc strong values tend
    to diminish the bad choices – like 15 and 20

**Aggregation strategies: Multiplicative**

  - **Multiple individual scores**

  - ![A close up of a street Description automatically
    generated](media/image71.png)

**Aggregation strategies: Approval voting**

  - **Counts scores above a certain threshold, seen as approval value**

  - Threshold value above \> and we count how many

  - So for item 1=1, item 2 = 0, item3 = 3

**Aggregation strategies: Plurality voting**

  - **Choose the item with highest number of votes. → per user\!\! So
    the item u1 voted the highest and so on**

      - And item 9 got 2 votes

  - Skewed - few users and few items. And also low scores are observed
    by the strong ones

  - ![A screenshot of a cell phone Description automatically
    generated](media/image72.png) → item 9 \!\!

**Aggregation strategies: Least Misery**

  - **Considers the minimum of scores for each item, and choses the item
    with the maximum value (least miserable)**

  - User will fall into disadvantage bc its with majority → but this
    kinda

  - LM looks at the lowest item, and out of those which is least
    miserable LOL

  - ![A screenshot of a cell phone Description automatically
    generated](media/image73.png) → 5 is the best choice

  - User 1 is the most unhappy, but won't be toooo bad

  - Can be combined with other strategies e.g. average – its easy but it
    can disadvantage people. However, if we do average without misery,
    then we take everything below 4, and item 5 will have stronger
    confidence now

**Aggregation strategies: Most pleasure**

  - **Considers the maximum of the scores for each item, and chooses the
    item with the maximum value – most pleasure**

  - So item 4

**Aggregation strategies: Borda**

  - To ignore actual values and start looking at the ranking

  - **Considers item ranking in the individual preferences, then
    calculates the item ranking for the group**

  - How can we consider users considering different schema? → ranking

  - First we calculate the ranking. For each user we normalise the
    scores by looking at the highest and lowest value

  - User 1 – item 9(10) and lowest item1(1)

  - ![A screenshot of a cell phone Description automatically
    generated](media/image74.png)

  - Ohhhh so we rank the item in order and give the value starting from
    1-10. Highest gets 10 and lowest gets 1

  - Then we add all the items and see what the highest is

**Aggregation strategies: Copeland Rule**

  - **Counts how often an item beats another item (majority voting) and
    how many time loses – takes the difference as the value**

  - Item 2 – 5,3,6,5. And we compare this to item 1 – 1,3,4,9

  - → we compare the item1 to each other of items –

  - Do beats – loses. It will be item 4\!\!

  - ![A screenshot of a cell phone Description automatically
    generated](media/image75.png)

  - 아 아이템 1이 2보다 3개이상 더 나은점수면 그걸 1 로침. 근데 아이템 1 이 다른거보다 나은게없어서 0

**Aggregation strategies: Heuristics**

  - So far, item 5 seems strongest as it was recommended by most of this

      - It won't make people too miserable, and it gives everybody a
        reasonable choice assuming that user 3 isn't the dominant user
        (**authority)**

  - **Fairness**: take best options for everyone

  - **Authority**: take the best option for the most influential user

**How do we know which is the best option → Evaluation**

  - You recommend and see how individual members of the group feels
    about it.

  - Reading – when people was given the recommendation for the group and asked how
    satisfied they were, and their friends thought

  - Two keys factor of people’s satisfaction with the group rec

      - **Affective state –** am I happy or grumpy – people take the
        recommendation based on their mood and like/ dislike

      - **Relationships with other users -**

**Impact of relationships on accepting group recommendations**

  - Several relationships that might affect

  - Yoyou'll suck it up

      - **Communal sharing** -Best friend – if you have to compromise
        for someone you like, you’d be happy

      - **Authority ranking -** High respect – if they’ve got given
        priority, they take it even though its not their choice

  - Unhappy and more sensitive about not being taken into account

      - **Market pricing -** Someone you compete with – will be fighting
        for fairness

      - **Equality matching** - If you think ur unequal –

  - → When you explain the choice, need to bear in mind the relationship
    between people

**Summary**

  - Obtain individual preferences

  - **Aggregation strategies → key \!\!**

      - Most system use **hybridisation** of these strategies

      - Evaluation is **important** and need to tune the strategies or
        heuristics → will be able to explain better

      - Opinions will be influenced by **affect** and **relationships**

  - Presenting the recommendations to the group

## **Adaptive content presentation**

  - **Reading for further clarification**

  - very important so strongly recommend

  - Decide what to show to the user – what to show and how to show is
    called adaptive content presentation

  - 2 methods

      - Static approach – content is already there. How do we show them
        on the screen

      - Dynamic approach – need to automatically decide what to show to
        the user

          - Complicated, but this is where AI comes in

**<span class="underline">Part 1 – Static approaches</span>**

**Adaptive content presentation – two steps**

1.  **Content adaption** – how to select most appropriate content for
    the current user in the current situation, based on the user model →
    **algorithmic component of selecting the content**

2.  **Content presentation** – once you know what you want to show, how
    to effectively present the information in the user interface →
    **interface**

**Page based approaches**

  - Could be a description of the item, page, video, news item, etc

  - Adaptation mechanism – selecting most appropriate page

  - Closet approach to recommender system – a lot of predefined item, we
    select most appop, and we show

  - Process

      - **Selection** – if content based, then we match the content,
        collaborative – we select based on what others have liked

      - **Presentation** – how we order them, how you render them on the
        page (layout)

  - ![A picture containing drawing Description automatically
    generated](media/image76.png)

**Example- KBS Hyperbook**

  - Eg which uses page-based adaptation to illustrate the approach

  - About particular aspects of programming – depending on who the user
    is, appropriate content is shown → **adaptive information
    resources**

  - **Adaptive navigational structure -** All the pages possible for
    showing is shown in the <span class="underline">navigation</span>

      - ![](media/image77.png)Colour – indicates the pages that are
        suitable for the user

  - Not shown features

      - **Adaptive trail generation** – need to see this page then this

      - **Adaptive project selection** – to select a particular problem
        for user to work on, and based on that user can study appop page
        → second way of showing a bundle of pages

      - **Adaptive goal selection** – more related to user model – user
        can have several goals, and the system decide which goal is the
        most appropriate based on the goal, and it can give resources or
        paths to study THEN it can give adaptive project selection

**  
**

**Page-based approaches advantages and disadvantages**

<table>
<thead>
<tr class="header">
<th><strong>Advantages – versatile!!</strong></th>
<th><strong>Disadvantages – static!!</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Widely used and is a mainstream approach – <strong>versatile</strong> approach</p></li>
<li><p><strong>Content ins pre-prepared</strong> → have a control of what the user will see, in businesses etc</p></li>
<li><p><strong>Easy to implement</strong> – you decide what to rec, and think how to order</p></li>
<li><p>Can be used with <strong>many user models</strong> - if we consider content pages being items you see a lot of models used</p></li>
</ul></td>
<td><ul>
<li><p><strong>Content authoring is expensive</strong> – need to have a dedicated team which will think what the best way to present the content is</p></li>
<li><p><strong>Efficiency of model being static</strong> – if new users come, they might not be catered for</p></li>
<li><p><strong>Content quality varies</strong> – depends on the authoring and the curation process. The curator might not know all contents → will cause deficiency of the problem</p></li>
</ul></td>
</tr>
</tbody>
</table>

  - So the next approach will challenge the staticness

**Fragment based approaches**

  - We have predefined fragments, and we select parts and we bring the
    pre-defined parts together

  - Two strategies below\!\!

**Optional fragments**

  - ![A screenshot of a cell phone Description automatically
    generated](media/image78.png)

  - Fragments could be anything – text, images, videos, etc – pieces of
    content that has been pre-prepared

  - **Selection -** Each fragment is associated with the **applicability
    conditions** (yellow little tag) \!\!\!\! the metadata that
    describes in which condition will be related so that we can pull the
    content

      - Red – selected, based on its applicability conditions

  - **Composition -** Once selected, we need algorithm which constructs
    a page from several diff fragments together

  - → Have composed a page by pulling what's available from the content
    pool

**Example- AVANTI**

  - Which uses optional fragment

  - Suited for elderly people, as it looks at vision impairments and
    attention span.

  - Pages are composed from **pre-defined fragments**.

      - Here fragments are the texts

      - Additional fragments – useful or further information,
        accessibility

  - Fragments are **selected based on user model**, which has
    <span class="underline">user knowledge, interest, but also the
    user’s cognitive and visual abilities</span>

      - If they have vision impairments, need to increase the size, more
        images for better grasp

  - Then when the fragments are selected, putting the page is the image
    first then the text.

**Optional fragments advantages and disadvantages**

<table>
<thead>
<tr class="header">
<th><strong>Advantages – flexible !!</strong></th>
<th><strong>Disadvantages – static!!</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>They are <strong>flexible</strong>. It gives element of dynamicity</p></li>
<li><p>Fragments are <strong>pre-prepared</strong>, so we still have the control of what the user sees</p></li>
<li><p><strong>Fragment authoring is easier</strong> – rather than creating a fully pledged page !!</p></li>
<li><p>Could be <strong>crowdsourced</strong> – since they are smaller pieces, it can be created by different authors → could speed up the process of content creation</p></li>
</ul></td>
<td><ul>
<li><p>Fragment <strong>quality may vary</strong> – as it is dependent on the author and how we've curated the content</p></li>
<li><p>The pre-<strong>defined conditions for each fragment</strong></p>
<ul>
<li><p>User may be missed – could be created when the user model isn't available yet</p></li>
<li><p>Expensive/ time consuming – for every fragment, to create all the conditions</p></li>
</ul></li>
<li><p>Combined fragments may <strong>not align with one another</strong>, as it is from diff authors</p></li>
</ul></td>
</tr>
</tbody>
</table>

**Altering fragments**

  - Page is constructed as a set of constituents → offsets some of the
    deficiency

  - We don’t define preconditions for every fragment, but for **group of
    fragments**

      - Content suitable for novice, intermediate or advanced

      - Blue, yellow and red is associated with the level \!\!

  - ![A close up of a sign Description automatically
    generated](media/image79.png)

  - Step – select, and put them together

  - **Selection -** We select the **group (constituents)** – and decide
    which group is appropriate for the user

      - After selecting the group, we go on fragments to find
        appropriate fragments

      - Called altering bc you can decide from the group, which to
        select

          - Can do it randomly, in order etc

  - **Composition**

      - Easier than optional, bc you can have layout of how you gonna
        put the constituents

      - In e.g. put the red first then yellow \!\!

![](media/image80.png)**Example – AHA**

  - **Navigation frame (**generated by the system**)–** gives the user
    all the possible types of contents they can see

  - **If they open particular page, it is composed on the fly**

  - **Content frame –** from the nav frame, composed of several
    fragments by different authors

      - First and second paragraph – fragments are related to the
        constituents, and pull together so user can see the page

  - → Pull existing pieces of pre-defined content with diff level of
    complexity and detail

  - Fragments are related to

**Altering fragments advantages and disadvantages**

<table>
<thead>
<tr class="header">
<th><strong>Advantages – flexible</strong></th>
<th><strong>Disadvantages</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Flexible coz fragments can be pre-prepared (same as option)</p></li>
<li><p>Easier than editing full content</p></li>
<li><p>Can be crowdsourced</p></li>
<li><p>Constituents allow control of <strong>coherence</strong></p></li>
</ul></td>
<td><ul>
<li><p>Continues to be <strong>static</strong>!! Coz content is pre-prepared</p></li>
<li><p><strong>Quality</strong> may vary</p></li>
<li><p><strong>Pre-defined constituents</strong></p>
<ul>
<li><p>Authors need to think of what group fragment will go to</p></li>
<li><p>Usually, the constituents are defined before the page composition or fragment definition → so definition of constituents narrow the condition for curators</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

→ even the most flexible approach, altering fragments, suffer from
having to define the conditions when content is used

**<span class="underline">Part 2 – Dynamic approaches</span>**

**Dynamic approaches– two steps**

1.  **Dynamic content adaptation**

    1.  Automatic selection of content

    2.  Automatic structuring of the content – decide which part is
        suitable and how to present

2.  **Dynamic content presentation**

    1.  Automatically define relevance and focus – how to show what to
        focus and what's in context

    2.  Automatic media adaptation – which devices used etc

→ much more complex, so will just illustrate the ideas

1.  **Dynamic content adaptation**

<!-- end list -->

  - Content **automatically selected** from:

      - **Knowledge base** – need to have some **relevance measure** to
        determine which of the objects from knowledge base is suitable
        (e.g museum example- need to decide which painting and what
        info, and other painting to bring)

      - **Bayesian network** – provides domain knowledge of what could
        be relevant to the user- gives a causal probabilistic
        relationship between the variables and can propagate from it,
        then decide which item is appropriate to show

      - **User preferences model –** match the preference model to what
        we know about the world and identify which preference has the
        most importance → weighted preferences

  - Content **automatically structured**

      - **Task accomplished planner**s – bringing several pages together
        according to task and goals

      - **Argumentation models** – you know what objects you want to
        show, and this model helps putting it together in a coherent
        manner to convince the user

      - **Conversation theories** – brings interaction (dialogue) with
        the user to convince, or can present one narrative

**Example – ILEX (natural language text generation)**

  - In terms of structuring the content, it uses conversational theory

  - ![](media/image81.png)Also uses knowledge-based approach to select
    the content

  - E.g. museum, gallery, exhibition

  - Title – concept for the knowledge base (**domain model)**

  - Image – linked with the concept

  - Text – brings in other objects, e.g. rounded stones, faceted stones,
    which are brought from the knowledge base

      - **Text / syntactic structure -** Have been put together in a
        coherent way. Each sentence is linked to the prev sentence, so
        it makes a story

  - **Representation of context -** Relevance to other concepts – bullet
    points - the links

  - None of this was pre-defined, it was automatically designed by the
    computer

**Example – GEA (generator of evaluative arguments)**

  - Using argumentative approach

  - First - Select what content is relevant

      - Based on **3. Preferences** – we identify which **parameters**
        are related

      - E.g. type of house, location, number of bedrooms

      - All the other parameters are suppressed

  - We need to **convince** the user that this is best for them – like a
    story line

      - ![](media/image82.png)Story is building an **argument** to
        convince them

      - E.g. convenient house location, and compromise for user
        preference, traffic is moderate (strength of the house to
        compensate for the deficiency)

      - → **adding more conditions** related to house preferences & are
        **generated automatically**

  - Convince that this house is best for them

  - Level of detail will differ for users or for same user at different
    stages

![](media/image83.png)**Example- RIA (responsive information
architect)**

  - System about recommending houses

  - It uses user preferences then looks at the characteristics of the
    houses to match the **user preferences**

  - All the information is automatically generated

  - Also, adding to the text, there is a speech narration why particular
    house is chosen

  - Based on the user preference, the selected parameter will be
    **brought forward →** it amplifies diff factors

<!-- end list -->

2.  **Dynamic content presentation**

<!-- end list -->

  - Key is to decide what is the focus in the user, and what is the
    context

  - **Focus** – emphasize the content that has been found most relevant
    to the user

  - **Context** – allow access to less relevant content to preserve
    context

      - Which user can go and stretch further

      - Stretch text – you have item in focus are stretched out, in full
        detail – page cursor close or stretch \!\!\!

          - Summary & purpose is stretched, but basic intro is closed

      - ![](media/image84.png)Scaling fragments, dimming fragments,
        summary thumbnail

**Scaling approach**

  - How we present the focus and context – scaling

  - The **fisheye** – visualisation technique

      - Is relevant but not the prime focus – is smaller and is blurred
        out.

      - The prime focus – shown with full size and highlights so they
        can read and grasp quickly

**Dynamic content presentation**

  - How to adapt to diff **media factors**

  - **User specific factors** – visual impairments (careful of size),
    dyslexia (more images), autism (no long list of bullet points)

  - **Information specific feature**

  - **Constraint from media** – if its speech, we need to take into
    account the user listening environment, video then bandwidth,
    textual, size of the screen and how much they can see

  - **Contextual information** – who else is around the user (other
    interactions)

  - **Limitations of technical resources**

  - → need to bring those when we **automatically generate and present**
    it. Need to identify which are the most important ones for adaptations

2 widely used approaches of dynamic content presentation

  - **Rule based approaches** – using rules to define how to combine
    /choose diff type of media in which condition

      - E.g. dyslexia – structured diagrams and illustrative images \>
        long text

      - Tell us how to combine more than one media

  - **Optimisation approaches** – allow which items to put together, but
    how to best optimise the screen space and environmental constraints
    so that you can present most optimal media and **media
    combinations**

**Example – RIA – Real Estate Agent (media adaptation – optimisation)**

  - Focusing the presentation on the screen

  - ![A screenshot of a cell phone Description automatically
    generated](media/image85.png)

  - How we **select the houses** and the characteristics of houses to
    show to the user

  - Then we need a **mechanism on algorithm** to tell us how to render
    the screen in a way media complements one another

      - LHS – combination of several houses. On the screen and info is
        rendered so it isn't overlapped

      - Top side - **complementary text** → Optimisation – timing, which
        part of the dialogue and how it will correspond to images

      - RHS - The $499000 is the key information now. Everything else is
        stripped out → **optimisation is the level of detail & timing**

**Summary**

  - The main adaption mechanism of the system – what to show and how to
    show

  - 2 main family

      - **Static** – predefined pages

      - **Semi dynamic** – predefined fragments

      - **Dynamic** – automatic content selection and presentation

  - Links to the recommendation algorithm, filtering and reordering of
    the contents

  -
## **Evaluation of user adaptive systems**

  - If I were to evaluate complex system how we gonna do this

  - 2 ways

      - Consider whether ur evaluating components/ prototype

          - Look at each of the components layered evaluation or
            component-based evaluation

          - Methods

**At what stage is the system that you are evaluating?**

  - System prototypes - **Formative evaluation**

      - Does the system work as intended? – algorithms and components of
        the system

      - Do the components perform adequately? – as expected?

      - Which design to choose (from several prototypes)? – if we have
        several options, which choice works the best?

  - Once we have a fully developed deployed system – **summative
    evaluation**

      - What are the benefits of personalisation?

      - Are there any potential drawbacks?

**Layered evaluation**

  - ![](media/image86.png)Consider each component of the system and see
    if each step works adequately → layered evaluation

  - Once all components are validated then we can evaluate the system as
    a whole

<!-- end list -->

1.  Collection of input data

2.  Interpretation of the collected data

3.  Modelling of the current state of the world

4.  Deciding upon adaptation

5.  Applying adaptation decisions

6.  Evaluating adaptation as a whole

**Example- 3Cixty app**

  - Main methods of evaluation → 3Cixty

  - App that offers personalised city guide – it uses information about
    events, places in the city in a form of **knowledge graph** . and
    the personalised city guide uses this to suggest to people

  - System collects info about the user in 2 way

      - **Explicit** – before visiting the city, they can browse through
        the suggestion and **add to Wishlist** for the places they want
        to go to → can set up the **user preference** beforehand

      - **Implicit** – during system usage, based on user profile it
        starts recommending – then system recommends nearby places of
        the Wishlist. As user uses the system, it is gradually filtered

          - Where the user is, the path from where they are (destination
            and arrival places)

          - Can get list of recommended items, in terms of distance or
            can put **important parameters** in the front

      - As user uses the system, based on their choice and their
        addition to the Wishlist, it is gradually updated

<!-- end list -->

1.  **Collection of input data – information about the user**

<!-- end list -->

  - Goal – check quality of raw input data

  - Criteria

      - **Accuracy** – is what we are creating about the user accurate
        on who they are and what they are interested in?

      - **Latency** – by the time we are using the user model, and then
        when we apply the model, there's a lime lapse – so need to
        consider how the timing is when we collect about the user

      - **Sampling rate** – when we evaluate the input of the data,
        rather that data is representative about the user

  - We don’t know if the user is alone → important data missing \! the
    **social aspect** of the user is missing → can identify though the
    **user test**

  - Implicit data collection methods

      - **Data mining** – if we have a lot of data, with this you can
        explore the input data to see whether you’re getting all the
        possible restos have been picked – or only the most popular
        places?

      - **Cross validation** – used when you try to predict (by
        combining to user interest) to see what ur picking matches the
        user interest

  - **Explicit data collection method**

      - Explicit – user selecting the Wishlist and filter

      - **\*User testing** – can show the prototype or with persona
        users, where we present persona

      - **\*Simulated user** - to test this persona method

  - In this case, yoyou'll be checking in regards to **accuracy** (what
    they entered is what they got), **latency** (app is used before they
    visit the city), is there any other data that we are missing

<!-- end list -->

2.  **User model acquisition**

<!-- end list -->

  - How you’re acquiring the user model

  - Goal – check that input data is interpreted correctly

  - Criteria

      - Validity – if interpretation is valid. If the click is indicated
        as user interest

      - Predictability – when we look at user model, to see if we will
        be predicting a particular parameter and how valid

      - Scrutability – the accountability and transparency of
        algorithms. People would like to know how user model acquisition
        is working and how particular it works → challenging but
        shouldn’t be ignored

  - Methods

      - \*\***Data mining** - most appropriate because we collect a lot
        of data- explore the data we capture

      - **Cross validation** – if we are predicting correctly what we
        want about the user

      - **Heuristic evaluation** – use for scrutability and validity –
        what we want this component to be doing, and ensure that the
        heuristics are met

          - **E**.g. heuristics = fairness. Have to make sure info is
            processed fairly so it doesn’t advantage certain people

      - **User test** – will be moving back to data mining, BUT with a
        clear indication of user is and the prediction

      - **Simulated users** – can hire users and give them several
        scenarios and ask them to perform the task. But is a good
        compromise before going into real world

<!-- end list -->

3.  **User model**

<!-- end list -->

  - Goal – check that the constructed user model represents the users

  - Of implicit user modelling

  - Prime criteria

      - **Validity**

      - **Predictability** – does this predict the user behaviour

      - **Scrutability** – will look at the user model – is it possible
        to open the user model and will they understand the user model
        to validate the parameters the system must use

  - Secondary criteria

      - Consciousness – are we collecting ethically appropriate data?
        Are these relevant for the user model? Are we doing anything
        useless?

      - Comprehensiveness – can the user understand that

      - Precision and sensitivity – close to validity, how accurate we
        are about the characteristics and are there any groups where our
        system doesn’t work very well

  - Methods

      - Bc we are looking at **implicit user modelling**, its about data
        collected about the user → hence **data driven evaluation** (lec
        16)

          - Predictability, and how accurate that is regarding what we
            predicted about them

      - **Cross validation** – allows us to reshuffle the data, and we
        train particular user and test diff users

      - **Heuristic evaluation** – bringing the user aspect of the user
        model – we will have some criteria and we inspect the user model

          - **E**.g. system will collect my choices for restos and
            destination – but if its collecting all my travel, it will
            evaluate my travel pattern which is unnecessary – with
            heuristic, yoyou'll identify that irrelevant data is collected

      - **User test** – need real user to test the comprehensiveness esp
        with user with impairments, if they are disadvantaged in any way

      - **Simulated users**

      - **Focus groups** – similar to heuristic, and this brings people
        together to see what people are thinking – scrutability,
        comprehensiveness etc

      - **User as wizard** – will help with more technical evaluation –
        user is imagining them as a system, and offering what the system
        should be doing in that situation.

          - Based on this it checks the actual system, or can use user
            suggestion to inspire the algorithm

<!-- end list -->

4.  **User model application (deciding upon adaptation)**

<!-- end list -->

  - Goal – determine whether the adaptation decisions made are optimal
    and appropriate

  - Criteria

      - **Appropriateness**– was it appropriate way to apply the user
        model

      - **Acceptance** – is this acceptable for the user

      - **Predictability** – will this adaptation predict how the user
        will respond?

      - **Scrutability** – is it easy to understand?

      - **Breadth of experience** – does it limit anything?

  - Methods

      - Data mining, Cross validation → check for appropriateness &
        predictability. In what cases adaptation worked?

  - To check for acceptance, scrutability and breadth of exp → nee human
    aspect

      - Heuristic evaluation/ walkthrough -

      - User tests, simulated users

  - Taking user perspective

      - Focus groups

      - User as wizard

<!-- end list -->

5.  **Applying adaptation decisions (user interface)**

<!-- end list -->

  - Goal – determine whether the implementation of the adaptation
    decisions is optimal

  - Will consider the wishlist, nearby events and places, paths from the
    place where the user is, list of places of interests that has been
    suggested

  - Criteria -more at the user perspective – choose 1 or 2

      - **Usability –** mainly this

      - Timeliness – how timely the path is etc

      - Obtrusiveness – task is interrupted, may find characters
        presented is obtrusive, language etc

      - Acceptance

      - Predictability

      - Breadth of experience

  - Methods

      - Heuristic evaluation, cognitive walkthrough – can be conducted
        by experts or developers, assuming they are users. Then they can
        go through the app to see what was given

          - Timeliness, obtrusiveness

          - Hard to evaluate acceptance

      - User test – usability and acceptance

      - Focus group – can evaluate obtrusiveness and breadth of
        experience

      - User as wizard – can ask they are the adaptation – the path, the
        best choice justification

<!-- end list -->

6.  **Evaluating the system as a whole**

<!-- end list -->

  - Goal – to evaluate the utility of the system (benefits to the user
    and businesses) AND drawbacks \!\!\!\!

  - Typical benefits

  - User perspective – through user driven evaluation – AB testing or
    same with added system

      - **\*Efficiency** (performing tasks quicker) – Whether they’ve
        found the resto quickly

      - **\* Effectiveness** (performing tasks better) - if they found
        the best choice

      - **User satisfaction** (users may be happier with personalised
        systems)

      - **Trust** (users may feel more valued) – do they trust what the
        system is offering

      - **Accessibility** (all categories of users catered for) – path,
        do we take into account movement impairments

  - Business perspective

      - **Improved revenue** (e.g. in e-commerce) – will this added
        feature improve, will this lead to better learning

      - **Customers’ loyalty** (e.g. in e-commerce) – will they come and
        use the system again, will they recommend it?

**Typical usability threats** ![A close up of a map Description
automatically generated](media/image87.png)

## **Wrap-up and future direction**

**Topics we covered**

![A close up of text on a white background Description automatically
generated](media/image88.png)

**Future direction 1 – Data**

  - Massive data, structured and unstructured – video, sensor, etc

  - More availability of link data – so that we can make connections w
    the real world

**Advantages**

  - Availability of massive amount of data – richer data allows for
    stronger user profiling methods – more test and trials

      - E.g Deep learning

  - Extending what is being modelled

      - Different culture variations – user behaviours in cultural
        clusters, groups user belong to,

      - Abilities – physical, cognitive abilities, and constraints on
        the user that can limit the ability.

      - Individual traits – personality, motivational and engagement
        patterns

  - Data integration – to have better understanding of what the users
    interests, motivation etc from several data source.

      - The ability to link the data and see the concepts of the data
        will be quite imp

**Challenges**

  - **More rigorous evaluation**

  - **Hybridisation** of the methods – to identify strength and
    weaknesses to find a way to hybridize them

  - **Bias and fairness** – can be buried into algorithms and data which
    leads to conclusion of the algos → how to take this into account to
    make sure that recommendations are done in a fair way

  - **Transparency and accountability** – being able to explain to the
    user and to be able to hold the system accountable for that its
    recommending

**Future direction 2 – Devices**

  - Wearable devices are becoming mainstream & we have more
    sophisticated wearables, embedded smartness in the device

      - E.g. smiling fridge – only opens when user smiles lol

  - Smart homes – they will detect behaviours of the users – e.g. for
    elderlies

**Advantages**

  - **Collecting meaningful data –** now we can sense more dimensions
    about the user

  - **Multimodal data –** processing of multimodal data – posture,
    movement, heartrate etc

  - **From data to proxy of the behaviour** – measurements that come
    from data to derive meaningful metrics, and linking the metrics to
    behaviour indicators

      - This will multimodal will be more prevalent

  - **Improve user experience –** more research on this of how
    adaptation improves the ux

**Challenges and opportunities**

  - Enter new domains – challenge and opportunity

      - Health and wellbeing domain

      - Opportunity bc we can enter that previously wasn’t established

      - Challenge – lot of responsibility bc ethics, privacy etc

  - New applications relying on data collection and personalisation

      - Smart home, smart appliances, driverless cars - how we can use
        all the sensors to suggest the best thing

      - Core values – right info to right person in a right way

**Future direction 3 – Interaction**

  - More augmented, extended, virtual system etc to mimic the
    interaction of the physical world

  - Conversational agent – siri, alexa, etc now is more qna but the
    interaction collected can adapt the interaction in a context

  - Interactive devices that allow **collaborations** – interactive
    table tops, which captures gesture and multimodal interaction
    between user and system

  - Robots – between the people and the robot

      - Will change the landscape of the system

Research

  - Strong emphasis on **multimodal data** and how this can be
    interpreted and lead to user model

  - **Context** is crucial – we now know about other users, env,
    interaction with the device etc

  - Individual differences

      - When you talk about interactive devices, **cognitive and
        physical abilities** will be imp

Challenges

  - Social interactions

      - Group interaction – within the digital world

      - Social robots – digital devices and with humans

  - The more users are exposed to new interactions, the higher the need
    for personalisation → more creative way of thinking

  - More emphasis on speech and capturing implicitly

## **QnA session - 28/4/2020**

  - They will be part of the exam

  - Exam would not deviate significantly from this and next year no
    confusion when prepping

      - Will be very similar from last time

      - This could possibly be related to the exam ‼\! so it WILL

<!-- end list -->

  - The way we answer will be different

      - We upload the answers

Q – will the online exam be part of the exam?

  - Yes. familiarise the content

  - She developed the example step by step

## **Module assessment and exams**

**Exam**

  - Exam will be similar to last 2 years

      - Quite a bit are similar to prev years

  - Take scenario, and within that thered be question

      - Questions are such that you’ll have to do more analytical
        thinking and discuss the answers ‼

  - 3 question and 20 marks each

  - Things will be shuffled fuckkkk – won't be like q1 is about lec 1-5

  - so go through all the lectures skksksks

  - Will be about

      - Key concepts and how you apply it for this specific concept ur
        judgement here. Particular methods will have to be this

      - Strength and pros – if you copy of the lecture, its not gonna
        help. ELABORATE with the right strength and weakness for this
        particular scenario

  - Topics covered in the module

      - Info about the user will be covered less bc cwk‼‼‼‼\!

      - Recommendations – will be more on how to filter, group and
        algorithms INCLUDING the hybrid and the evaluation and the group
        recommendation virtually

      - Adaptive content presentiaon part of the exam

      - something from evaluation of ev

  - If its been in the cwk – will be less.

  - Just write the answers

Ahhahaa we download it from the Minerva‼‼‼\! the questions. And prepare
the pdf

Say the point ‼\!

  - **Describe and justify \!**

  - 3 hours is the estimate of how long it might take

**How to revise for the exam**

  - Main concepts are in the lecture notes

  - Do watch the videos – the new ones

  - Use the main reading to complement the lecture – use it more
    targeted coz its too long

  - Make notes\!

  - There are practical examples ‼‼‼‼‼‼

**PUT IT IN THE CONTEXT OF THE SCENATIO**

**Coursework - Rubric**

1.  Introduction and scoping

<!-- end list -->

  - The purpose of the personalisation should be very clear – not clear
    what exactly what itd be doing

<!-- end list -->

2.  Scenario

<!-- end list -->

  - Two personalisation feature

  - Challenges of that group is addressed in the personalisation feature

  - Not full mark – bc uve only described one

<!-- end list -->

3.  User model representation

<!-- end list -->

  - Why certain things are in the model

  - How you gonna personalise when you don’t have the things

<!-- end list -->

4.  User model building

<!-- end list -->

  - description of what info and how it will be collected

  - Whether that’s implicit or implicit

  - Not good – didn’t look at the context. The suitable context for the
    application

  - How the info about the user is used to build the user profile most
    missed

      - Count the tags and frequencies to do the user interest etc

<!-- end list -->

5.  Overall architecture

<!-- end list -->

  - Also need external knowledge –

<!-- end list -->

6.  Critical review

<!-- end list -->

  - Limitation – only works if they regularly

  - Strength – what's the human factor that keeps them loyal? One need
    to elaborate on the computational method – can minimize the noise

**Past paper**

  - She wants to avoid direct yes or no – so we have to disCUSS

      - E.g. show an example from above problem with the stereotype -

1d

  - Scrutable user model

      - What is scrutable

      - What are the claimed benefits

      - How it could be implemented

1e

  - We have to suggest what we gonna add

  - E.g. social recommendation

  - Good question that we might have ‼‼‼‼‼

2 – city tourist – last lecture of evaluation lecture covers the tourism

2a - good question that we may get

  - Expect to take the city guide – what bg need to one

2b

3 – regional news paper

  - Things are shuffled

## **13/5/2020 Revision session**

Past paper 2019

  - Question will be one scenario

  - Maybe that sub questions are connected – 1a and 1b to critique 1a,
    suggest an alternative

**Question 1 – hypothetical personalised news reader**

  - Cold start as the info isn't enough.

  - Therefore, we need something else, which is a stereotype

  - ![A screenshot of a cell phone Description automatically
    generated](media/image89.png)

      - Facets are attributes/ variables related to news.

      - So this is content based filtering

1a

  - Explain the stereotype - simple

1c -

  - For that user, **high interest in business news and local news**

  - What to do

      - You are given the user profile. You take that profile then you
        check each of the 3 stereotype (male, age, job, interest) to see
        which of them satisfies the users trigger.

          - Age – satisfied

          - List of interest – fits into politic and financial reader

  - Facet is business use

  - Degree of interet – high

      - ![A screenshot of a cell phone Description automatically
        generated](media/image90.png)

      - So we consider this \!\!

      - OR LOCAL THERE'S 2 table\!\!\!\!\!\!\!\!\!\!\!\!\! → combine the
        two

      - ![](media/image91.png)

  - Solution

      - Identify whichs teorytpe it belongs to

      - Know that we have 1 table for buiz and 2 for local

  - There's p=0.7 that user may NOT enter the stereotype

      - Local – 0.9\*07 = 0.63 → business news

  - Local news – from both stereotype

      - First – 0.7\*0.7= 0.49

      - Second - 1\*0.9 = 0.9

  - Combine - ![](media/image92.png)→ **AND**

1e

  - Could get questions like this coz its open ended

  - Creativity

  - Could suggest filtering – knowledge, content

  - More information

  - Whatever ur suggesting that has to comply

  - E.g answer Collaborative filtering, that is based on other ppls
    behaviour. User model – we need ratings. We need to extend the sys
    to ask them to rate. We create a model to use user-user or
    item-tiemt

**Question 2**

3cixty – mainly used

But tis q is given the city thing – so 3city could apply

2a

  - Lecture 15 – hybridisaiton of recommenders

  - Take an eg, look at background data, input data and algorithm

      - Background - You need recommendation of users, geolocations

      - Input – rating from the visitor of items of interest gps
        location

      - Algorithm – similar

  - Content based

      - Background data – about the content – more detailed features of
        the item in the city

      - Input – explcitiy indicate the interest

      - Algorithm – classifier that firs the engquiring

2b

  - DEPENDS on a\!\!\! of background data you used → should be
    relatedddd

  - Collaborative filtering

  - Content based filtering

**Question 3**

3b

  - If we do collaborative, likely to get a matric

  - If you recognize what its about, \!\! like we know collaborative
    fileting, → we have the notes. So go to lecture

  - L13, l14 Within part 2 and par 3, there was a paper discussing the
    amazon\!\!\!\!\!\!\!\!\!\!\!\!

  - Step 1 – find cutomers who purchased that itme - nd reduce the space

  - Step 2 – find items that have been bought by the user

  - Step 3 - calculate similarity ONLy btwen them

Answer

  - Step 1 – r3 – a4,a7 etc → sc

  - Step 2 – paris of articles → we start by looking at the item user
    lieks, which are a4,a7. So we calculate pair ONLY for those item

      - A4 (a1,a4), (a3,a4), (a5,a4)

      - A7 – (a1,a7) (a2,a7\_(a5,a7)

  - Step 3 – multiply an

      - 4 comes from multiplying the norms of 2 vecotr

  - We don’t take a7 bc we already have (??)

3c

  - Reason for amazon was to target scalability – bc it reduces the
    search space

  - Scalability – excessive number of similarity comparison between
    items or users → amazon reduces the search space

  - Amazon also does offline searching

  - **→ reduced number of similarity comparison**

**3d**

  - Lecture 19

  - Discusse usability threat – towards the end – slide 20 – adapting
    system as a whole

      - ![A screenshot of text Description automatically
        generated](media/image93.png)

      - She described some in specific

      - And not all will apply -

  - Possible Q on slide 20\!\!\!\!\!\!==\> Describe some benfit of the
    system

answer

  - Add is to add some explanations – diminish

  - Reshuffling of crowd – you will have diminish controllability

      - Mitigating factors, and which yoyou'll apply

  - Obtrusive – user will feel obtrused, and what would happen

  - Diminished breath of exp – it is indeed possible coz it tend to rec
    popilat items – and this could breath

      - Very purpose of collab was to get out of the filter bubble

      - This is least applicable, but it can be but requires good
        justificaiton
