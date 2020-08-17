# ZKit-Framework [![Maintainability](https://api.codeclimate.com/v1/badges/00ca04339de7350a9f1f/maintainability)](https://codeclimate.com/github/000Zer000/ZKit-Framework/maintainability) [![Technical Debt](https://img.shields.io/codeclimate/tech-debt/000Zer000/ZKit-Framework)](https://codeclimate.com/github/000Zer000/ZKit-Framework/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Code Size](https://img.shields.io/github/languages/code-size/000Zer000/ZKit-Framework)](https://github.com/000Zer000/ZKit-Framework) [![Latest Release](https://img.shields.io/github/v/release/000Zer000/ZKit-Framework?label=Latest%20Release)](https://github.com/000Zer000/ZKit-Framework/releases/latest) [![Latest Commit](https://img.shields.io/github/last-commit/000Zer000/ZKit-Framework?label=Latest%20commit)](https://github.com/000Zer000/ZKit-Framework/commits/master) [![License](https://img.shields.io/github/license/000Zer000/ZKit-Framework)](https://github.com/000Zer000/ZKit-Framework/blob/LICENSE)

A lightweight framework written in pure python for payload generation and dosing . rootkit, ransomware, file transfer, keylogger all with ZKit-Framework . both available in TCP and UDP for transfering data . keylogger uses email for transfering key stroeks 
And with user payloads zkit helps you for generating your own payloads . **Everything a hacker needs**

It doesnt only encrypt a malware or your own malware  . it adds a special stub for every platform that hides the process and several encryption methods 
you have the power to choose which encryption method 

## What can it do

- It can support you for making a malware for a speciefied target . (With User-Payloads) 
  In several ways with encrypting your malware 
  and inserting a decode stub for decryption in runtime and some 
  special methods for hidding malware from user in windows and linux

- Payloads available in ZKit-Market so you can install it

- Building you own payload and publishing it. [Tutorial](https://github.com/000Zer000/ZKit-Framework/wiki/Creating-My-Own-Payload)

- Run dos attacks

- Build rootkit reverse shell

- Build file transfer payload (reverse shell rootkit features included too) both TCP and UDP

- Build Ransomware TCP and UDP

- Build KeyLogger TCP and UDP or even transfer using email

- Several encryption method . **but you have the power to choose which** 

- Payload uses an encryption method and random variable names random whitespaces to fool the AVs . Virus total result is : 0/59

No need for updating it manualy . zkit will check for updates everytime you run it . and will warn you about the new release 

and updating it is very easy . just go to the root directory of zkit and run `python updater.py update`

and if you modified your zkit or its just broken easily repair it using `python updater.py repair`

## Installing

installing it is easy . check out two methods below for installing it

### With Git
```
git clone https://github.com/000Zer000/ZKit-Framework.git
pip install -r requirements.txt
  Downloading colorama-0.4.3-py2.py3-none-any.whl (15 kB)
Collecting scapy
  ...
```

Done !

**Powerful framework with only 3 requirements ! Doenst sound great ?? i will be happy if you star it . and please watch it for getting notification for new release** 

> If any problem found . You can share it with me on issue tab .

### Without Git
Easily [download it](https://github.com/000Zer000/ZKit-Framework/archive/master.zip) .

Open CMD.exe on windows or terminal on linux

Unzip the `ZKit-Framework-master.zip` .

Make sure you have pip installed . Then run :

```batch
cd ZKit-Framework
pip install -r requirements.txt
```

> If any problem found . You can share it with me on issue tab .

Done !

## License
ZKit-Framework is licensed under Apache Software License 2.0 full license at [License](https://github.com/000Zer000/ZKit-Framework/blob/master/LICENSE)

## Using ZKit
Using ZKit is easy just `python zkit.py` . there is no argument everything work with menues.

Rootkits, Ransomwares, keylogger, User payloads generated all are in `\builded\` directory

If any issue found please open an issue to solve it

## Contact Author

You can contact me from my personal email : 000Zer000@pm.me

And i will reply you back with 000Zer000@protonmail.com

Or you can contact me from twitter . [000Zer000 On Twitter](https://twitter.com/__000Zer000__)

## Donating
Do you like ZKit ? Do you often use it ? ZKit-Framework is a solo work . Make a donate and be in the list of **Our HEROS** in readme _show your love to hack with supporting it._

My bitcoin address is : `1G8cHZc2kYPUfGVPtgGckemskmYcK6xayf`

Any other currency's available too . just open an issue and i will send you the address if its available

If addresses are broken let me know to update them .
