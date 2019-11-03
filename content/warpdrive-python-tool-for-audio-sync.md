Title: Warpdrive: Python audio sync tool using Dynamic Time Warping
Date: 2019-12-31 23:00
Tags: portfolio, python, signal-processing, music
image_url: /images/warpdrive_splash.png

<!-- PELICAN_BEGIN_SUMMARY -->
I developed a command line tool, `warpdrive` for syncing and aligning audio recorded from multiple sources. The tool leverages the Dynamic Time Warping (DTW) implementation found in the `librosa` library. I used this tool while recording a demo album with four upcycled smarphones.
<!-- PELICAN_END_SUMMARY -->

I use the output from the DTW to build a psuedo-histogram of time offsets between chroma features of the various recordings. I then choose a base signal and pad the rest of the signals with the appropriate time delay to align all signals. See the source code [here](https://github.com/dsholes/python-warpdrive).

See an example below:

<video style="border-radius:15px;"muted width="100%" controls>
  <source src="{static}images/warpdrive_example.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

<br>

