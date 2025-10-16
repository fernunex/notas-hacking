https://play.picoctf.org/practice/challenge/284
## Description
[🥛](http://mercury.picoctf.net:29522/)

## Solution
1. Go to the website.
2. Download the image that appears with right click and download.
3. Search for embedded info using stenography, but first modify the buffer of Ruby to avoid memory overflow:
```
	export RUBY_THREAD_VM_STACK_SIZE=50000000
	
	zsteg concat_v.png
	
```

We get the flag: `picoCTF{imag3_m4n1pul4t10n_sl4p5}`
## Additional notes
## References

