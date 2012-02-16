# DeathPhrase

My father and I have a fundamental disagreement on religion. He believes that there is an afterlife and I don't. I would love for there to be one, but I just don't see that there is any evidence that it is the case. That seems like an odd way to start a readme, but it's important for the motivation behind this.

So the motivation behind this is that my father is sure that he'll be able to communicate with me after he dies, so this essentially is a way of creating a longish phrase (the default is 5, 5 letter or more words), that can be emailed, yet leave the person who generates it not knowing anything about the phrase in question. This way my father can memorize the phrase, and if in fact he finds someway to communicate it to me posthumously, I'll have a way to make sure it's him and not bereaved hallucination.

To generate a phrase and email it, do:
    deathphrase.py EMAIL_ADDRESS

this will do several things:
- Create a phrase
- Email the phrase to the supplied email address
- Encrypt the phrase with SHA256 and ROT13
- Save the encrypted versions to separate files.

The reason for both SHA256 and ROT13 is that while I don't want to know what the phrase is now, I might at some point, so having one that is decryptable is nice. The SHA256 version is meant to be the primary way of checking if the phrase is correct.

To check a phrase against the encrypted version run testphrase.py, it'll ask for the phrase, just type it in and it'll give a True/False.
