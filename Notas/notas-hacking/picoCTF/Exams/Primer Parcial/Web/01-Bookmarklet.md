https://play.picoctf.org/practice/challenge/406
## Description
Why search for the flag when I can make a bookmarklet to print it for me?

Additional details will be available after launching your challenge instance.
Browse [here](http://titan.picoctf.net:60833/), and find the flag!
## Solution
1. Go to the website.
2. Run the script that it gives you:
	```
	        javascript:(function() {
            var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓ¨ÍÕÄ¦í";
            var key = "picoctf";
            var decryptedFlag = "";
            for (var i = 0; i < encryptedFlag.length; i++) {
                decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
            }
            alert(decryptedFlag);
        })();
    
	```
3. We get the flag: `picoCTF{p@g3_turn3r_18d2fa20}`
## Additional notes
## References

