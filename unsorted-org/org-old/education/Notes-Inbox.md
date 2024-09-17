---
title: Notes-Inbox
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 09-29-55
reference: 
description: 
aliases: 
tags: 
---
# Notes-Inbox
Notes Inbox
 fleeting notes



How to Solve Problems

Use the scientific method! This is supremely important when reverse engineering.

Scientific Method

    Question
    Hypothesis
    Experiment
    Observation
    Analysis
    Conclusion


The Experiment & Analysis section are the most important for us to touch on.

Question
How do I access the ammo variable dynamically?

Hypothesis
Perhaps there is ammo variable inside the player class, if I can access the player object I can then access the ammo variable

Experiment
Find the player object, search for ammo variables inside of it. Compare and contrast the offsets and addresses of both the health variable and the ammo variable and how they are accessed.

Observation
We open cheat engine, find the health address and ammo address, use "find what accesses" to see how they are used. We discover that the offsets are not offset from the same object address for each of these variables. In addition, when we change guns, the ammo address changes.

We reform our hypothesis
Perhaps there is a weapon object which contains the ammo variable, perhaps there is a pointer to the current weapon object in the player class.

How do you form this hypothesis?
Pretend you are the developer and come up with your own logic for managing multiple weapons and weapon related variables. How do you keep track of the current weapon you're using so you decrease from the correct ammo variable? Come up with a couple different logical methods that might make sense, and then test them. This is indeed how I would do it when you consider Object Oriented Programming, I would create dynamic objects and keep track of them by using pointers and as the owner of the weapon is the player, I would put the pointer in the entity object.

Reformed Experiment:
Take the address of the ammo variable, subtract the offset, this will yield the address of the weapon object and then we will reverse engineer this structure from here.

Observation & Analysis
The structure which ammo is in, is indeed the weapon object. We find other variables related to the weapon in it. We also notice it is in an array of other weapon objects which have the same structure and act similarly. When we trace back each ammo address to a dynamic multilevel pointer for the current weapon, and then change this weapon, we notice a pointer in the player class which always points to the current weapon ammo.

Conclusion
The game keeps track of the ammo dynamically by using a pointer to the current weapon object which is inside an array of weapon objects. When you switch weapons, the pointer changes to point at the correct weapon. The ammo variable for this weapon and other weapon variables are accessed from this address by relative offset.

To access the ammo variable dynamically we need only calculate this multilevel pointer at run time and it will always point at the correct ammo address.

See that? We created a hypothesis, tested it and when it was wrong, we formed a new one and tested it. The second hypothesis was proven. But the scientific method holds that, all proven hypotheses require rigorous testing and re-testing as additional knowledge and evidence becomes available.

So next time you have a little problem like "can't find entity list, it's not like assault cube" don't come to GH begging for help, we're not your mommy. You need to use the scientific method to figure it out, form multiple hypotheses. If you can't solve the problem after a few days, then ask your question. If you can't form solid hypotheses to test, the reason is because you don't have enough knowledge and evidence to form the basis of your experiment, in which case you need to search the forum and watch some tutorials.

Constants
Now we need to talk about constant variables and unknown variables.

Our hypothesis tries to solve an equation. The equation in it's simplest form is something like this:

A * B = C

    A and B represent variables which the experiment seeks to define
    C represents the observed behavior.
    The goal of our hypothesis is to define A and B.


Well A * B is the most simplest form. This is not reality. In reality there are hundreds of variables. You need to define as many as possible and every time you change a variable, you must redo the test.

This is the most important part right here, this is a HUGE problem for people inexperienced with this thought process. When trying to solve a problem they have too many variables and not enough constants. You cannot solve problems like this.

The goal is to define as many variables as constants as possible, this way your experiment only has to test a hypothesis as it related to one unknown variable or a small set of variables. If you only have to solve A and B that's not so bad, maybe you can define both in one experiment. But if you had 20 variables like when you try to find the TraceLine() function you are going to reverse many things before you have enough constants to have a successful experiment.

For example, if you have some weird issue with a lib on one game on one computer, but it works fine on another computer in another game your variables might look like:

    Game
    Operating System
    Architecture
    Game Logic

You need to isolate Game, Operating System & Architecture and define them as constants. This way you are only testing for the definition of "Game Logic". If you only define Game, Architecture as constants, when you perform your observation, you will not be able to draw a conclusion which defines the cause and effect of the other two variables in the experiment.

With too many non-constant variables you cannot attribute the cause and effect to the correct variable.

We see this all too often with questions "dll won't inject, why?"

No one can solve this problem because there are too many unknowns, we need constants so we can hypothesize the potential causes of the problem:

    What OS are you on?
    What Injector are you using?
    What game are you injecting into?
    Does it have anticheat?
    Is the game x86 or x64?
    Is the injector x86 or x64?
    Is the DLL x86 or x64?
    What's the source code for the dll?
    Are you compiling in debug mode or release mode?
    etc...

If you use the scientific method, you can solve almost any problem with time and patience.


How to Be Successful & Achieve Goals
No one becomes a 1337 game hacker by just playing around in Cheat engine a couple minutes month or by watching a couple videos.

To achieve success in anything in life you need to be able to set and achieve goals and give yourself realistic expectations.

Most importantly you need to be serious, if you're not serious and you're just doing this on a whim you will not be successful. Henry Ford and Elon Musk weren't laying in bed going "yeah I guess I'll open a car company maybe... or smth"

Before you can be successful at anything you must:

    Define your goal
    Research what is required to achieve your goal
    Come up with an action plan & timeline
    Assess your ability to achieve the goal
    Commit to achieving the goal
    Perform the Action Plan
    Achieve the goal and declare victory

Define your goal
"I want to learn how to hack games."

Research
DuckDuckGo "Learn Game Hacking"
Go to GuidedHacking.com, #1 link of course (not :()
Read the "Start Here Guide"

Action Plan

    Do not skip any tutorials until I understand it 100%
    Spend 2-8 hours a day, 5 days a week learning game hacking
    For 2 months: Complete the Start Here Guide
    For 2 months: practice what I learned, writing C++ apps and making boring trainers
    For 2 months: Do the Reverse Engineering Guide
    For 2 months: practice reversing various apps and making kewl trainers
    For 2 months: Do the Intermediate Game Hackers Guide


Wow in 1 year I will be able to hack any game I want without anticheat, this is very realistic and I'm not retarded at all. Thanks Rake.

Assess
Can I really do this? Do I really want to do this? Is it this important to me? Am I smart enough and mature enough to do this? This is the biggest thing I've ever tried to do, am I up to the challenge? Do I really want to waste my time doing this? Does this have any long term benefits for me? Are they worth it?

My mom stills dresses me and I can't count to 10, maybe this will take me 2 years instead of 1 year...

Assess and revise your action plan!

Commit
I'm doing this, there is nothing that will stop me because I am the divine offspring of Lord Rake himself. No petty king or vile beast will claim my soul on this harrowing journey, for my steadfastness grants me immunity from the frivolous ignorance of the masses. Armed with the Holy Scripture and the Lamenter's Crown I will rain down hellfire upon the heathens, climb to the pinnacle of righteousness and declare myself a fellow God of Game Hacking.

Perform
Do the start here guide for the love of god

Achieve & Declare
Hack a new game using all your knowledge and experienced gained from your action plan.
Declare victory.
