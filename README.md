### Features

- Setup the area where the Tesseract should read the code using your mouse and escape-key;
- Setup the input field for the key to be wrote in as well as a redeem and confirm button;
- Manually set the x and y values in the code by just setting `enable_manual_config = False` to `enable_manual_config = True` and editing those values;
- Automatically input the key into the redeem field on Epic, Steam, etc;
- Automatically checks the type of game-key using RegEx (Currently only Epic);


# OCRCodeSnatcher

Have you ever seen a Twitch Stream where they give out Game-Keys inside the Stream as a popup? No? I saw it just once happening. Everyone in the Chat was frustrated they aren't fast enough to type etc.
By doing a giveaway like this you are ignoring two major problems for your viewers! 1. Not everyone is a fast typer and 2. Everyone has different Stream latencies.
This script helps to get rid of the typing problem!

### How to install this script

1. Clone or Download this Repo and put it in a folder wherever you want.
2. Install Python 3 https://www.python.org/downloads/
3. For **Linux/Mac**, download [Googles Tesseract OCR](https://github.com/tesseract-ocr/tesseract#installing-tesseract "Googles Tesseract OCR") or **for Windows**, download the [prebuilt Windows binary](https://github.com/UB-Mannheim/tesseract/wiki) and install it to the default directory (C:\Program Files\Tesseract-OCR)
4. Open CMD or a Terminal inside of the folder and write
	`pip install -r requirements.txt`
5. Now everything should be working and you can run it inside the Terminal with
	`python3 codesnatch.py`
6. Now follow the instruction inside the Terminal and you're done!

### License

Copyright © 2022 crennis <contact@crennis.com>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.

<a href="http://www.wtfpl.net/"><img
       src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png"
       width="80" height="15" alt="WTFPL" /></a>


I can not guarantee for this code to work and i probably won't activle update or maintain it.
For a more Windows friendly and more likely up to date version [look at iCallH4x Fork](https://github.com/iCallH4x/thePyOCRCodeSnatcher "look at iCallH4x Fork") of this script. 
