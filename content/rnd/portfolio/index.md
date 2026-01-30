---
title: "Portfolio: Reverse Engineering Adobe Portfolio"
date: 2026-01-11T23:25:00+01:00
draft: false
categories: ["R&D"]
tags: ["Hugo", "Static Site Generator", "Web Design", "AI Coding", "Antigravity"]
featured_image: "/favicon/favicon.png"
description: "Moving away from Adobe Portfolio by reverse engineering the design and structure using Hugo and the Antigravity AI assistant."
---

This project represents the transition of my professional portfolio from a proprietary platform (Adobe Portfolio) to a custom-built, static site generated with **Hugo**.

### The Motivation
Adobe Portfolio provided a convenient starting point, but I reached the limits of its customization. As a Technical Director and Professor, I wanted a site that offered full ownership and technical flexibility.

### Visual Evolution: From "Monolithic" to "Six Bars"
In these reference screenshots of the original Adobe design, we can see a **Monolithic Dark** approach:

![Original Projects View](projects_old.png)

The original site used a single background color throughout the entire page, relying purely on spacing and bold typography to separate the header, content, and footer.

![Original About Page](about_old.png)

For the new **Hugo** implementation, we have evolved this into a more structured **"Six Bars" Layout**. This new system introduces subtle background transitions and distinct horizontal strips to create a more cinematic and organized visual rhythm:
1.  **Nav Bar**: (Pitch Black)
2.  **Section Banner**: (Medium Grey)
3.  **Content Body**: (Dark Grey)
4.  **Imprint Segment**: (Footer Strip 1)
5.  **Social Icon Segment**: (Footer Strip 2)
6.  **Copyright Segment**: (Footer Strip 3)

### The Reverse Engineering Process
The goal is to capture the professional, high-density essence of the original site while using the power of **Hugo** and **Tailwind CSS** to implement this new "Six Bars" structural logic.
