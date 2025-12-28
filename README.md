# Tourist Feedback System

A **web-based feedback system for tourist attractions** that enables visitors to submit feedback, upload images, and view analytics. This system provides a simple and interactive way for tourists to share their experiences, while giving administrators actionable insights through a dashboard.

## Overview

The Tourist Feedback System allows tourists to provide ratings, comments, and photos for various attractions. Admins can monitor and analyze this feedback to improve services, understand visitor preferences, and identify areas for improvement.

## Key Features

* **Feedback Submission:** Visitors can submit ratings, comments, and suggestions.
* **Image Upload:** Add photos to provide context and enrich feedback.
* **Analytics Dashboard:** Admins can view statistics, trends, and summaries of user feedback.
* **User-Friendly Interface:** Simple design for both visitors and administrators.
* **Search & Filter Feedback:** Easily sort feedback by rating, date, or attraction.

## How It Works

1. Visitors navigate to the site and select the tourist attraction they want to review.
2. They fill out the feedback form, optionally upload images, and submit their review.
3. Feedback is stored in the **SQLite database** and displayed in the admin dashboard.
4. Admins can analyze the feedback, track visitor satisfaction, and identify trends.

## Tech Stack

* **Backend:** Python with Flask framework
* **Database:** SQLite for storing feedback and user data
* **Frontend:** HTML, CSS, JavaScript for interactive forms and dashboard
* **Analytics:** Basic charts and summaries for easy reporting

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/mrjawadd/tourist-Feedback.git
   cd tourist-Feedback
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the system:

   ```bash
   python app.py
   ```
4. Open your browser and go to:

   ```
   http://127.0.0.1:5000
   ```
5. Submit feedback as a visitor or log in as an admin to access analytics.

## Potential Improvements

* **Sentiment Analysis:** Automatically analyze user comments for positive, neutral, or negative sentiment.
* **Map-Based Visualization:** Display feedback geographically for better location-based insights.
* **Email Notifications:** Notify admins when new feedback is submitted.
* **User Accounts:** Allow users to track their own submissions and history.

## Use Cases

* Tourist attractions, museums, or parks looking to gather visitor feedback.
* Administrators needing actionable insights from visitor reviews.
* Educational projects for learning web development, data storage, and analytics dashboards.

## GitHub

[Tourist Feedback System](https://github.com/mrjawadd/tourist-Feedback)
