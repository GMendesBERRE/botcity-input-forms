<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://alexia.vc/wp-content/uploads/2021/12/Botcity2.png" alt="Bot logo"></a>
</p>

<h3 align="center">BotCity Input Forms</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 This bot opens the RPA Challenge Input Forms, downloads a excel file and inputs each customer in the application.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

I wrote this bot to get a taste for how is the development experience with BotCity and loved it!

## 🎥 Demo / Working <a name = "demo"></a>

![Working](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDVkNjZjdTBpa3U3bnVxMjF4cDJ5bGpudHl5d21ua284MnZsbWpqNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eFvKBcLVD8lf2FTJUu/giphy.gif)

## 💭 How it works <a name = "working"></a>

The bot first downloads the excel file containing all the clients to be inputted. It then starts the challenge and goes trough each row in this file. Once a client data has been inputted, it clicks on submit and then goes to the next line

After all data has been inputted, the bot takes a screenshot with the score of the challenge

## 🎈 Usage <a name = "usage"></a>

With python installed, type:

```
pip install -r requirements.txt
```

Once all packages have been installed, you can run the bot in the bot.py file:

```
python bot.py
```




<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](https://www.linkedin.com/in/guigomeebr/)</sup>

<sup>Want to make a similar bot? Check out: [GitHub](https://github.com/botcity-dev)</sup>

## ⛏️ Built Using <a name = "built_using"></a>

- [BotCity](https://www.botcity.dev/) - Build Python RPA with Enterprise-level orchestration.
- [Pydantic](https://docs.pydantic.dev/latest/) - Pydantic is the most widely used data validation library for Python.
- [Selenium](https://www.selenium.dev/) - Selenium automates browsers. 
- [Pandas](https://pandas.pydata.org/) - Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool

## ✍️ Authors <a name = "authors"></a>

- [@GMendesBR](https://github.com/GuiMendes-BR) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- TBD
