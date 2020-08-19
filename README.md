# ZKit-Framework 
[![Maintainability](https://api.codeclimate.com/v1/badges/00ca04339de7350a9f1f/maintainability)](https://codeclimate.com/github/000Zer000/ZKit-Framework/maintainability) [![Technical Debt](https://img.shields.io/codeclimate/tech-debt/000Zer000/ZKit-Framework)](https://codeclimate.com/github/000Zer000/ZKit-Framework/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Code Size](https://img.shields.io/github/languages/code-size/000Zer000/ZKit-Framework)](https://github.com/000Zer000/ZKit-Framework) [![Latest Release](https://img.shields.io/github/v/release/000Zer000/ZKit-Framework?label=Latest%20Release)](https://github.com/000Zer000/ZKit-Framework/releases/latest) [![Latest Commit](https://img.shields.io/github/last-commit/000Zer000/ZKit-Framework?label=Latest%20commit)](https://github.com/000Zer000/ZKit-Framework/commits/master) [![License](https://img.shields.io/github/license/000Zer000/ZKit-Framework)](https://github.com/000Zer000/ZKit-Framework/blob/LICENSE)

A lightweight framework written in pure python for payload generation and dosing. ZKit-Framework includes rootkits, ransomware, file transfers, and keyloggers. Both TCP and UDP are available for transfering data. Keylogger uses email for transferring key strokes.
ZKit also helps you to generate your own payloads. **Everything a hacker needs.**

It does not only encrypt malware or your own payload, but it adds a special stub for every platform that hides the process. You also have several encryption methods to choose from.

## Features

- Support for making malware for a specific target. (With User-Payloads)

- Several methods for encrypting malware and inserting a decode stub for decryption in runtime.

- Special methods for hiding malware from user in Windows and Linux.

- Payloads available to install in ZKit-Market.

- Building you own payload and publishing it. [Tutorial](https://github.com/000Zer000/ZKit-Framework/wiki/Creating-My-Own-Payload)

- Run DOS attacks.

- Build rootkit reverse shells.

- Build file transfer payloads (reverse shell rootkit features also included) for both TCP and UDP.

- Build ransomware for TCP and UDP.

- Build keyLoggers for TCP and UDP and also transfer logs by email.

- Payloads use random variable names and whitespaces to fool the AVs. Virus total scan result is: 0/59.

- Auto-updates and notifications about new releases.

To update, go to the root directory of zkit, and run: 
```bash
$ python updater.py update
```
If you modified zkit or it is broken, easily repair the installation using:
```bash
$ python updater.py repair
```

## Installation

Installation is straightforward. Run the following commands:

### With Git

```bash
$ git clone https://github.com/000Zer000/ZKit-Framework

$ pip install -r requirements.txt
```

### Without Git

Download the [archive](https://github.com/000Zer000/ZKit-Framework/archive/master.zip).

Open cmd/terminal on Windows or terminal on Linux

Unzip `ZKit-Framework-master.zip`.

Make sure you have pip installed. Then run:
```bash
$ cd ZKit-Framework

$ pip install -r requirements.txt
```

**Powerful framework with only 4 requirements! Doesn't that sound great? I will be happy if you star this project. You can also watch it to get notifications about future releases.** 

> If you encounter any problems, please submit an issue.

## Usage

Run ZKit with the following command: 
```bash
$ python zkit.py
```
No arguments neccessary.

Generated rootkits, ransomwares, keyloggers, and custom payloads are in the `\Output\builded\` directory.

## Contact Author

You can contact me from my personal email: `000Zer000@pm.me`

I will reply you back with: `000Zer000@protonmail.com`

Or you can contact me on twitter: [000Zer000 On Twitter](https://twitter.com/__000Zer000__) Or you can easily contact me on reddit : [000Zer000](https://reddit.com/u/0Zer0reZ0)

## Donating
Do you like ZKit? Do you use it often? ZKit-Framework is a solo work. Make a donation and be in the list of **Our HEROS** in the README. _Show how you love to hack by supporting it._

My bitcoin address is: `1G8cHZc2kYPUfGVPtgGckemskmYcK6xayf`

Any other currency is available too. Just open an issue and I will send you the address if it's available.

If any link or address is broken, let me know to update them.

## License
ZKit-Framework is licensed under Apache Software License 2.0 see [LICENSE](https://github.com/000Zer000/ZKit-Framework/blob/master/LICENSE).

