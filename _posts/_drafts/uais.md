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

**<span style="text-decoration:underline">Part 1 – Static approaches</span>**

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
    showing is shown in the <span style="text-decoration:underline">navigation</span>

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
    <span style="text-decoration:underline">user knowledge, interest, but also the
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

**<span style="text-decoration:underline">Part 2 – Dynamic approaches</span>**

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
