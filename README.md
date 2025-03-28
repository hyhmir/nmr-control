# NMR CONTROL APP

This app was created for the needs of NMR users at Institut "Jožef Štefan". It is an extension of Tecmag's proprietary software that comes packaged with thier Redstone hardware. The app's purpose is to emulate the old software they used at the Institute with the old hardware. It also integrates the control of Oxford Instrument's MercuryITC and MercuryIPS, this part is slightly unstable but the app functions even without them.

## installing 💻

### Prerequisities 

- Python 3.8+
- pip 20.0+
- TNMR by Tecmag

### Set-up

'''bash
git clone https://github.com/hyhmir/nmr-control.git
cd nmr-control
pip install -r requirements.txt
'''

To run navigate to the nmr-control folder and run

'''bash
python main.py
'''

or alternatively open the folder in VS Code and run the main.py from there.


## license 🔐

This software was licensed under the MIT license but it had to be changed to GNU GENERAL PUBLIC LICENSE. Read more at [LICENSE](LICENSE).

## cooperation

If you want to cooperate, reach out via email @ samo.krejan@gmail.com or just open a pull request. The repository is not meant to be activelly maintained, rather just improved for the needs of the scientists here, so for major changes I recommend forking the repository 🍴

## acknowledgments

- pytnt module was inspired and mostly copied from Chris Kerr
- Mercury control is mainly copied from [Mercury_control](https://github.com/jnejc/Mercury_control) - check it out if you only requre ITC and IPS control app.

## last notes

We are amateur programmers so keep that in mind when your head starts hurting when looking at our code. It was written to the best of our capabilities 🤗.