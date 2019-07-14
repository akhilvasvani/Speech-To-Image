# Speech-To-Image
This final project was created during my Machine Learning for Signal Processing class, which is an end-to-end speech to image implementation using DeepSpeech and StackGAN. At this point in time, only birds images can be produced. More are coming.


# Requirements

Python3.6+

TensorFlow 1.13+

Torch

Numpy

Runs on the GPU at the momemnt


# How to Run

If all the requirements are met, run ```birds_demo.sh``` and a few seconds later an image will output.


# Audio

In the Audio folder are couple examples of bird sentences used to generate the examples. If you want to create you own, all you need to do is record an audio file in the .wav format, convert it to 16000 Hz, and then enter the source destination in the birds_demo.sh file. 

The command to convert to 16000 Hz, using the ffpmeg package is: ```ffmpeg -i [source file] -vn -ar 16000 -ac 1 [destination file]```

If you want to use your own microphone, you can set up your own local [deepspeech server](https://github.com/MainRo/deepspeech-server) and you would have to modify the birds_demo.sh script. For this project, I did not want to do this but it can be done. 

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
    
    2) Alternatively, I have provided the checkpoints and pretrained model I used when building this project. Regardless, you stil have to change the client.py file after you install the deepspeech package on your computer. 

Use my DeepSpeech file on github Repo. Download the pretrained model, but follow what I did with the client.py file.


# Text Encoder

At the moment, I did not use an alternative way to extract the text embeddings. Basically, the get_embedding.lua file converts your example sentence into the specific text embedding needed to run for the StackGAN. You will need to download Torch and the respective requirements.


# StackGAN

The model is already pretrained, so there is nothing to worry about. Everything is update from the original [StackGAN](https://github.com/hanzhanggit/StackGAN)

# Issues

Please let me know of any issues and I am happy to correct them. Pull requests are always accepted!

# References

[StackGAN](https://github.com/hanzhanggit/StackGAN)

[Generative Adversarial Text-to-Image Synthesis](https://github.com/reedscot/icml2016)


