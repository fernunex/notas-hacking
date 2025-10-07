https://play.picoctf.org/practice/challenge/26
## Description
Decode this [message](https://jupiter.challenges.picoctf.org/static/d6fcea5e3c6433680ea4f914e24fab61/message.wav) from the moon.
## Solution
1. Download the audio file.
2. Install the sstv decoder: sudo git clone https://github.com/colaclanth/sstv
3. Decode the image: `sstv -d message.wav -o flag.png`
![](../../../images/flag%202.png)
The flag is: `picoCTF{beep_boop_im_in_space}`

## Additional notes
## References

