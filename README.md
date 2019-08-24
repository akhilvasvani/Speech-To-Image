# Speech-To-Image
This final project was created during my Machine Learning for Signal Processing class, which is an end-to-end speech to image implementation using DeepSpeech and StackGAN. At this point in time, only birds images can be produced. More are coming.


# Requirements

Python 3.6+

TensorFlow 1.13+

Torch

Numpy

Runs on the GPU at the momemnt


# How to Run

Download the deepspeech package, and the download the DeepSpeech pretrained model

Download my pretrained model from [StackGAN](https://github.com/akhilvasvani/StackGAN)

If all the requirements are met, run ```birds_demo.sh``` and a few seconds later an image will output.


# Audio

In the Audio folder are couple examples of bird sentences used to generate the examples. If you want to create you own, all you need to do is record an audio file in the .wav format, convert it to 16000 Hz, and then enter the source destination in the birds_demo.sh file. 

The command to convert to 16000 Hz, using the ffpmeg package is: ```ffmpeg -i [source file] -vn -ar 16000 -ac 1 [destination file]```

If you want to use your own microphone, you can set up your own local [deepspeech server](https://github.com/MainRo/deepspeech-server) and you would have to modify the birds_demo.sh script. For this project, I did not want to do this but it can be done. 

I added in a script which can convert from .m4a file format to a .wav format for 16000 Hz.

# DeepSpeech
1) Follow the instructions on installing [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech) package, and then download the latest [pretrained model](https://github.com/mozilla/DeepSpeech/releases), as well as the checkpoints. However, note that you must edit their [client.py file](https://github.com/mozilla/DeepSpeech/blob/master/native_client/python/client.py) via adding the lines 

``` parser.add_argument('--outfile', required=False, help='Path to save the text') ``` --> in the main function.

And add the following at the end of the main function in client.py

```if args.outfile:
        if args.extended:
            with open(args.outfile, 'w') as outfile:
                outfile.write(metadata_to_string(ds.sttWithMetadata(audio, fs)))
        else:
            with open(args.outfile, 'w') as outfile:
                outfile.write(ds.stt(audio, fs))
```

when you install deepspeech on your own computer. If you do not do this, DeepSpeech will not write saved the outputted text. This is also included in my repo if you are confused where to add either of these statements.
    
2) Alternatively, after you have downloaded the deepspeech package on your computer, you can download the [pretrained DeeSpeech model](https://drive.google.com/open?id=1JOltcT06wR61YXMVZohbAJmA52Rpcjsv) I used when building this project. Regardless, you stil have to change the client.py file. 
Create and save all the contents to the folder name ``deepspeech-0.5.0-models`` 


# Text Segmenter and Punctuation

Added in two networks which will segment your sentences and add punctuation to them. This is done, so that the outputted images by the StackGAN will be cleaner and nicer. For weird reason, when given one sentence, the text encoder produces a small .t7 file and the image created from it is poor. Unfortunately, the only way around this is to increase the size of the .t7 file, so the user will have to speak more sentences. However, because DeepSpeech is literally Speech to Text (no puncutation), I had to add these two networks to separate and punctuate the sentences. This adds more time to the total runtime of Speech to Image, so I am looking for a way around this.


# Text Encoder

At the moment, I did not use an alternative way to extract the text embeddings. Basically, the get_embedding.lua file converts your example sentence into the specific text embedding needed to run for the StackGAN. You will need to download Torch and as well as the 
[embedding file](https://drive.google.com/open?id=1a11TUAQKrHxRWnzWBTLpK9FkZdZqhKlT) and save it to the folder ``text_encoder``.


# StackGAN

Download my pretrained [StackGAN](https://github.com/akhilvasvani/StackGAN), so there is nothing to worry about. Everything is updated from the original StackGAN code. Note: you cannot use the original pretrained model by Han Zhang.

# Issues

Please let me know of any issues and I am happy to correct them. Pull requests are always accepted!

# References

[StackGAN](https://github.com/hanzhanggit/StackGAN)

[Generative Adversarial Text-to-Image Synthesis](https://github.com/reedscot/icml2016)

[DeepPunct and DeepSegment](http://bpraneeth.com/projects/)


