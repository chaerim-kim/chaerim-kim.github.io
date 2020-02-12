---
title: "Secure Computing: Introduction"
tags: [Secure Computing]
categories:
  - Secure Computing
date: 2020-02-01
---


## 1.  **Introduction**

**Questions**

-   How big of an issue is security?-- will be looking at recent
    examples
-   What we want to achieve in securing a system?
-   Who are the bad guys that trying to break in
-   Is there a perfectly secure? -- there isn't, it is immeasurable

**c.s.1 - Security flaw in Tory app**

-   Tory party conference has an app- last year's app didn't have any
    authentication, so the delegates could change all the details e.g.
    photos and position.
    -   E.g changed Boris Johnson's to Alexander Johnson

**c.s.2 - Blog of Nadine Dorries**  

-   She had a blog - someone didn't like it, so hacked it and changed it
    to some dumb content for posts of span of 2 years
-   She used a very easy password __web defacement__: attack
    on a website that changes the visual appearance of the site or a
    webpage

**c.s.3 - Data breaches in 2019**  

-   Been happening a lot more recently. In August, 4000 data breaches
    -   __Data breach__: when users and records of those
        users are leaked e.g Email addresses, passwords, credit card
        details
    -   Probably more that haven't been reported either
-   The impact of data breach in business is enormous!!!! in terms of
    reputation, finance etc

**Vulnerability of our daily lives**

-   In terms of devices we carry - how vulnerable those are - lots of
    software, data, etc
-   When the issue becomes public, its probably after the patches has
    been released so update security firmware diligently!!

**c.s.4 - Manchester bus travel app**

-   The hackers normally have knowledge on how to develop it securely
    BUT they gave out free bus travels
-   security is always affecting - business, organisations, devices etc
    hence it is important!!

**Security goals -- p16**

__Q: What is the goal of security?__
-   Class suggestions : Privacy, safe, data, confidentiality,
    authenticity, unbreachable
1.  __Data Confidentiality__ -- users should be given only
    enough __privilege__ to perform their duties.
2.  __Integrity__ -- trust of data at transit to ensure no
    insertion, deletion, replay (e.g. no replay - withdraw \$411242424
    -- don't wanna do that twice)
3.  __Authenticity__ - about who or what source of that data
    is, can we trust the msg from someone that claims to send it, about
    system users when they are accessing the server
    a.  Authenticity of the file- has not been corrupted since creation
    b.  System user authenticity -- who is it that are accessing the server, do they have the right to?
4.  __Access control__ - what to authorise when they have
    access - different level of access

5.  __High availability__ -- keeps data and resources
    available for authorized use ONLY at all times, even during
    emergency

    a.  Challenges = DoS (Denial of service) attacks.

6.  __Trustworthy system logs__ - can we trust the logging

    a.  The attackers could erase their presence from system logs

--> We use cryptography to save all that!

**Is there a perfect security?**  
Q - what would you do to protect data on my pc?  
-   Disconnect from internet
-   Back up the data -- prevents from entirely losing it
-   Password
-   Encrypt the data - will talk about the vulnerability of encryption
-   No such thing as 100% secure!! - all to do with what you tryna
    protect, who the user is, who has access
-   dissaving the tracker from thinking its not worthwhile hacking yours
    (if its too time consuming)

**Why is security hard?**

-   Software is so complicated - more complex than physical computers
-   Problem is that human beings make mistakes!! could lead to
    **vulnerabilities**
-   Can't __quantify__ the security - like yours is 79, mine
    is 23,
    -   a lot has to do with security being an __emergent
        property__
    -   Depends on the value asset, target, how you use it daily, who
        has access to your data.
    -   hence u can't easily measure it

**Human factor in security**

-   PEBKAC (problem exists btwn keyboard and chair) problem lies in the
    user!
-   But is it fair to blame it all on users tho?
    -   NO. From developer's perspective!!!

**Software Engineers perspective NCSE** \<CYBERUK in practice\>

-   If it can't be used well by the users blame the developer!
-   the point is, when we build a secure system, we gotta think about
    how humans think and its psychology, and gotta design accordingly!
-   Build software that can be used securely BY the user!!

**Hackers**

-   Hackers: was more of a neutral term for them to decompile and
    understand how the app
-   There are dual meanings -- depends all on the context we use!
    -   White Hat -- uses their skills ethically
    -   Black hat -- bad guy
    -   Both white and black hat - ppl both have sufficient knowledge
        about security

**Bellovin's Threat Matrix of Hackers** -- (P) \[1 pdf 22\]

-   Degree of focus and skills needed x and y axis
1.  Joy hackers: who experiment without an intent - let the curiosity be
    gone
2.  Opportunistic hackers: no purpose, but skills required so more
    dangerous
    a.  Botnet, is done thru opportunistic hacks
        i.  Botnet: number of internet connected devices, each of which
            is running one or more bots (from computers that lost its
            security permission). Used for DDoS attacks, spam, etc
3.  Targeted attacks - very specific goals, could get paid
4.  Advanced persistent threats- very skilled, targeted, and persistent!

**Advanced persistent threats**

-   Very sophisticated threats -- multidimensional, complex and tight
-   Malware that attacks systems in multitude of ways **Cyber warfare**
    -   E.g. **Stuxnet** -- malware that caused substantial damage to
        Iran's nuclear program.
    -   Goal was to prevent Iran from developing nuclear weapon
-   could even attack and destroy industry programs

\<CYBERUK in practice\> -
https://www.youtube.com/watch?v=u6x9C7t\_41s&feature=youtu.be
https://www.youtube.com/watch?v=u6x9C7t_41s&feature=youtu.be

-   it is impossible for users to NOT fall into phishing at all!!
-   The password strategy with long and frequent change aint working
-   We understand the technology better than we understand the people need to teach technology so that its closer to how ppl actually think
-   Security that understands and supports normal human behaviour!
