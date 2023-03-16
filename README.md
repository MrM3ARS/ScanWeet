
# ScanWeet

Twitter OSINT tool. It detects the posts containing the keywords you specify and saves them to the database.

It is a tool that aims to quickly scan the given keywords with the algorithm I developed and get the most accurate result. It can be used in Cyber Intelligence or OSINT fields.

![Uygulama Ekran Görüntüsü](https://github.com/MrM3ARS/ScanWeet/blob/main/ScanWeet-logo.png)

## Features

- It searches by filtering the given keywords.
- It takes a screenshot of the content it finds.
- It saves many data such as the ID of the content, the sender, the screenshot to the SQL database.
- Reaches at least 100 content.


## Setup




## Yükleme 

Clone the project

```bash 
  git clone https://github.com/MrM3ARS/Scanweet.git
```

Go to the project directory
```bash 
  cd Scanweet
```

Install required packages

```bash 
  pip install tweepy
  pip install pyautogui
```

Run

```bash 
  python3 Scanweet-v1.py
```

## Test

| App  | Min. Scan/pcs  | Productivity %  | Result %  |
|---|---|---|---|
| Scanweet  | 100 pcs  | %71  | %75  |


## Road Map

- [x]  Speed improvements
- [x]  Database operations
- [ ]  Bot account filtering
- [ ]  Incorrect content filtering
- [ ]  Spam Protection


## Support

Send mail emir@tiprocd.com for support.

