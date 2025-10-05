https://play.picoctf.org/practice/challenge/355
## Description
BookShelf Pico, my premium online book-reading service. I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book! Here are the credentials to get you started:

- Username: "user"
- Password: "user"

Source code can be downloaded [here](https://artifacts.picoctf.net/c/482/bookshelf-pico.zip). Website can be accessed [here!](http://saturn.picoctf.net:53278/).
## Solution
1. We login using the credential it gives us.
2. We obtain our JWT token.
		![](../../../../images/Pasted%20image%2020251004160516.png)
3. We mangle it using the secret key: "1234"
		Found here:![](../../../../images/Pasted%20image%2020251004163820.png)
	
	![](../../../../images/Pasted%20image%2020251004170639.png)

	4. We craft a PATCH Request to this path to update our role. Here we have included our cracked token to have the authorization.
		![](../../../../images/Pasted%20image%2020251004163423.png)
		The role must be 'Admin' and have a different id than the logged user (we set it to 4). we are using the role = "Admin".
		![](../../../../images/Pasted%20image%2020251004163535.png)
		The payload of the PATCH must contain the fields "id" (id of the user to update his role) and "role" the id of the role:
		![](../../../../images/Pasted%20image%2020251004164006.png)
		![](../../../../images/Pasted%20image%2020251004170212.png)

5. Now we re-log in and we can see the change and read the flag:
		![](../../../../images/Pasted%20image%2020251004170358.png)
		![](../../../../images/Pasted%20image%2020251004170424.png)
		Flag: `picoCTF{w34k_jwt_n0t_g00d_d72df65e}`
## Additional notes
## References

