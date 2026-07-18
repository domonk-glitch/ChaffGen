# ChaffGen

First part of a larger project to disrupt bad actors using wireless sniffing technologies to steal valuable information by filling their collector with garbage data. 

This program will be producing the garbage or 'chaff'.

Steps:
Accept input text file from user
Break text down into smaller chunks
Run chunks through hashing algorithm(s)
Write results to final file.

Planning to use a random generator in python to determine size of chunks and then size of chunk will detrmine the hash. Goal is to return similar length hash to input. 

The randomized chunk size will chew through the file and will end when the size of the chunk is less than the expected size due to being at the end of the total file. 

MD5 - 128 bits - 16 bytes
SHA1 - 160 bits - 20 bytes
SHA256 - 256 bits - 32 bytes
SHA512 - 512 bits - 64 bytes

Logic that anything 16 characters or less will go through MD5. 
Greater than 16 and up to 20 will go through SHA1.
greater than 20 and up to 32 will go through SHA256.
Greater than 32 will go through SHA512.

Project extension idea:
offer instead of using cryptographic algorhithms, run through simple cypher used for SFA: Dinosaur planet.
This entire project is meant to mess with the heads of people who wish to do harm, so have fun with it.
