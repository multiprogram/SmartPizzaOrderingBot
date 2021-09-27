# pizzawit - Talks to wit.ai for speech recognition and analysis in order
# to make a pizza-ordering chatbot. No actual phone call is made.
#
# See here for details: https://hackaday.com/?p=312908
#
# Copyright (c) 2018 - Steven Dufresne
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject 
# to the following conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import os
from wit import Wit

# Put your access token from wit here. Get this from your App's Settings on
# https://wit.ai. The Server Access Token works.
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' 

client = Wit(access_token)

def do_wit_natural_language_processing(audio_file):
    # do_wit_natural_language_processing - Have Wit.ai process the given
    # .wav file to convert the speech to text as well as analyse it and
    # map it to entities which we've trained Wit.ai for and extract any
    # data where appropriate.
    with open(audio_file, 'rb') as f:
        resp = client.speech(f, None, {'Content-Type': 'audio/wav'})
  