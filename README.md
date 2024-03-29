# ita

Decrypting the Two-Time Pad (hard!)


You have intercepted two encrypted messages, ciphertext-1 and ciphertext-2, encoded in the following 46-character alphabet:

[space]ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-:;'()

The messages were encrypted with a one-time pad - a sequence of randomly drawn characters of the same length and alphabet as the plaintexts. The encryption algorithm is to add the code of a plaintext character with the code of the corresponding pad character, modulo 46. To illustrate, if the plaintext is "ITA SOFTWARE" and the pad is "9KS;UENFN068" then the ciphertext is ")4T;-TTZ.1E-".

plaintext: ITA SOFTWARE = 9 20 1 0 19 15 6 20 23 1 18 5
pad: 9KS;UENFN068 = 36 11 19 42 21 5 14 6 14 27 33 35
ciphertext: )4T;-TTZ.1E- = 45 31 20 42 40 20 20 26 37 28 5 40

However, the sender made the critical mistake of using the same one-time pad for both messages, compromising their security. Write a program that takes the two ciphertexts and produces a guess at the two plaintexts. It should produce two plaintext messages of the same length as the ciphertexts, hopefully containing many of the correct words in the correct positions. It is unlikely your program will get all of the words correct, since there is not enough information in the ciphertexts to uniquely determine the plaintexts. Strive for a quality of decryption sufficient for a human reader--perhaps with the aid of a web search--to identify the original texts, which happen to be excerpts from classic works of English literature.

Your program may use English text or word lists or dictionaries of your choice to train on, for example to gather tables of letter or word frequencies, but you should not rely on any portion of the messages being in your training material.

This puzzle was created September '04 and retired December '06.
