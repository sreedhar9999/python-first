list=['a','e','i','o','u','A','E','I','O','U']
ksc=raw_input()
if((ksc>='a' and ksc<='z') or (ksc>='A' and ksc<='Z')):
	if(ksc in list):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
