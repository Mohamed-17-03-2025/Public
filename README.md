This is a very very very simple program that runs "வணக்கம் உலகம்", meaning "Hello world." in the Ezhil programming language. 
However as development for this language was stopped quite a while ago, it is fair to say that it's more of an esoteric language now.

Here's a step by step process of running it:

Step 01: Install Python 3.7 or older. This is due to the fact that Ezhil uses the "clock" function in the "time moduel".
				 This module has been deprecated since Python 3.8, I believe, so you'll have to install 3.7 or older. You can download
		 		 Python 3.7 or older from the official Python website.
			
Step 02: Double check the Python version you're running.
				 Open the command prompt and pass in "python --version".

Step 03: Install Ezhil.
				 In the command prompt, type in "pip install ezhil".

Step 04: Check details on installed 'ezhil' package.
				 In the command prompt, type in "pip show ezhil".You would see something like this in the 8th line [Do make sure to copy it]:
		 
	 			 Location C:\Users\<Username>\AppData\Local\Programs\Python\Lib\site-packages

Step 05: Right click "This PC" -> Properties -> Advanced system settings -> Environment variables -> System variables -> Path (Double click it) -> New -> Paste the "C:\Users\......\site-packages" path.

Step 06: Open a folder anywhere you like. Open a text editor of your choice and type: பதிப்பி "வணக்கம் உலகம்" . When you save, make sure you save it as "<filename>.n". You can also save it as a .py file as well.
				 However ".n" is what I've gathered to be Ezhil's defacto extension.

Step 07: Right click on your Ezhil file. Click "Properties". Cope the Location, which would look something like: "C:\Users\<Yours username>\OneDrive\.....\<Folder where the Ezhil file is stored>".

Step 08: Now open the command prompt. Enter "cd <the path you copied in step 07>".

Step 09: Enter the following after: "ezhil_env\Scripts\activate" . Once you enter you'll see "(ezhil_env)" prepended to your prompt. The command prompt ought to look like this: "(ezhil_env) C:\Users\<Your username>\...\<Folder where the Ezhil file is stored>".

Step 10: Enter "chcp 65001"

Step 11: Enter "ezhili <Ezhil_file_name>.n".

Step 12: You would see a really weird "வணக்கம் உலகம்". But it's the right output. You can copy the result onto something else and it'll render properly. Command prompt isn't that great at displayiin Thamizh texts.

For more information do give this fascinating paper a read: https://arxiv.org/abs/0907.4960
If you can read Thamizh do give this a read as well: https://ta.wikipedia.org/wiki/%E0%AE%8E%E0%AE%B4%E0%AE%BF%E0%AE%B2%E0%AF%8D_(%E0%AE%A8%E0%AE%BF%E0%AE%B0%E0%AE%B2%E0%AE%BE%E0%AE%95%E0%AF%8D%E0%AE%95_%E0%AE%AE%E0%AF%8A%E0%AE%B4%E0%AE%BF)

I intend on doing more with this niche language if time permits.
