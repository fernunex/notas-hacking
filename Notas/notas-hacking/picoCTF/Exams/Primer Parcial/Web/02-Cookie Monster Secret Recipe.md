https://play.picoctf.org/practice/challenge/469
## Description
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe? You can access the Cookie Monster [here](http://verbal-sleep.picoctf.net:57444/) and good luck
## Solution
1. Go to the website.
2. Check the cookies.
3. Decode in base 64 the cookie:
	`echo cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzX0E2RkEwN0Q4fQ%3D%3D | base64 -d`
4. We get the cookie: `picoCTF{c00k1e_m0nster_l0ves_c00kies_A6FA07D8}`
## Additional notes
## References

