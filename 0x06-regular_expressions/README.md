0x06. Regular expression

Background Context
Build your regular expression using Oniguruma, a regular expression
library that which is used by Ruby by default. Note that other regular
expression libraries sometimes have different properties.

The focus is to play with regular expressions (regex), here is the Ruby
code that you should use, just replace the regexp part, meaning the code
in between the //:

sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2

Tasks
0. Simply matching School

Requirements:

The regular expression must match School
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method

1. Repetition Token #0

Requirements:

Find the regular expression that will match the cases provided
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method

2. Repetition Token #1

Find the regular expression that will match the cases provided
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method

3. Repetition Token #2

Find the regular expression that will match the cases provided
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method

4. Repetition Token #3

Find the regular expression that will match the cases provided
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method
Your regex should not contain square brackets

5. Not quite HBTN yet

Requirements:

The regular expression must be exactly matching a string that starts
with h ends with n and can have any single character in between
Using the project instructions, create a Ruby script that accepts one
argument and pass it to a regular expression matching method

6. Call me maybe

Task is brought to you by a professional advisor Neha Jain, Senior
Software Engineer at LinkedIn.

Requirement:

The regular expression must match a 10 digit phone number

7. OMG WHY ARE YOU SHOUTING?

Requirement:

The regular expression must be only matching: capital letters

8. Textme

Requirements:

The script should output: [SENDER],[RECEIVER],[FLAGS]
The sender phone number or name (including country code if present)
The receiver phone number or name (including country code if present)
The flags that were used
