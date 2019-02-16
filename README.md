# Tacotron 

An implementation of Tacotron speech synthesis in TensorFlow. with support for android


### Audio Samples

  * **[Audio Samples](https://keithito.github.io/audio-samples/)** from models trained using this repo.
    * The first set was trained for 441K steps on the [LJ Speech Dataset](https://keithito.com/LJ-Speech-Dataset/)
      * Speech started to become intelligble around 20K steps.
    * The second set was trained by [@MXGray](https://github.com/MXGray) for 140K steps on the [Nancy Corpus](http://www.cstr.ed.ac.uk/projects/blizzard/2011/lessac_blizzard2011/).



## Background

In April 2017, Google published a paper, [Tacotron: Towards End-to-End Speech Synthesis](https://arxiv.org/pdf/1703.10135.pdf),
where they present a neural text-to-speech model that learns to synthesize speech directly from
(text, audio) pairs. However, they didn't release their source code or training data. This is an
independent attempt to provide an open-source implementation of the model described in their paper.

The quality isn't as good as Google's demo yet, but hopefully it will get there someday :-).
Pull requests are welcome!



## Quick Start

### Installing dependencies

1. Install Python 3.

2. Install the latest version of [TensorFlow](https://www.tensorflow.org/install/) for your platform. For better
   performance, install with GPU support if it's available. This code works with TensorFlow 1.3 and later.

3. Install requirements:
   ```
   pip install -r requirements.txt
   ```


### Using a pre-trained model

1. **Download and unpack a model**:
   ```
   curl http://data.keithito.com/data/speech/tacotron-20180906.tar.gz | tar xzC /tmp
   ```

2. **Run the demo server**:
   ```
   python3 TacotronServer.py --checkpoint /tmp/tacotron-20180906/model.ckpt
   ```

3. **now go to the android applicaton**:
   * Type what you want to synthesize and the ip address of your computer 
   * Note: your computer and mobile device should connect to the same network



  
