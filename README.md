# Weather Telegram Bot

A Python-based Telegram bot that provides real-time weather updates for any city using the OpenWeatherMap API[span_1](start_span)[span_1](end_span).

## 🚀 Overview
This bot allows users to simply type a city name and receive current temperature and weather conditions[span_2](start_span)[span_2](end_span). It uses the `telebot` library for interaction and `requests` for fetching data from the weather API[span_3](start_span)[span_3](end_span).

## ⚙️ Features
- **Real-time Data:** Fetches live weather updates including temperature and weather descriptions[span_4](start_span)[span_4](end_span).
- **Interactive:** Simple command-based interaction using `/start`[span_5](start_span)[span_5](end_span).
- **Error Handling:** Provides feedback if the city is not found or if there is an API issue[span_6](start_span)[span_6](end_span).

## 🛠 Prerequisites
- Python 3.x
- Required libraries:
  ```bash
  pip install pyTelegramBotAPI requests
