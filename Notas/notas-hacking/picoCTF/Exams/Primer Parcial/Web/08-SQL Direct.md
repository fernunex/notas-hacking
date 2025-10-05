https://play.picoctf.org/practice/challenge/303
## Description
Connect to this PostgreSQL server and find the flag! `psql -h saturn.picoctf.net -p 60443 -U postgres pico` Password is `postgres`
## Solution

1. Connect to the server.
2. List all its table and information: `\dt`
3. View all the content of the unique table that exists: ` SELECT * FROM FLAGS;`
4. We found the flag: `picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}`
## Additional notes
## References

