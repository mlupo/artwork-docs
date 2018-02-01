# The Mansfield Reporter

<img src="./images/Mansfield_screen_off.JPG" width="600">

## Basic Info
**Year:** 2015  
**Materials:**   
**Dimensions:**  w 11", h 8", d 6"

## Description
The Mansfield Reporter is a simple device which can generate new text from some of history's greatest authors. By pressing the red button, you will be shown a new passage from either Friedrich Nietzsche, William Shakespeare, or Gertrude Stein. Or, press the black button to combine all of the authors into one super-author, and generate a unique passage from their combined corpus of text.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/pomt0gw3bvc?rel=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

The device pictured above is the main implementation of this artwork: the embedded screen shows the generated text one word at a time against a selected image. However, the process has been adapted to generate videos for live projection, or to post text and gifs to a [twitter feed](https://twitter.com/yupsurewhatever).

The authors used were selected both for the clarity of their voice, and because they have large bodies of work in the public domain.

### Tech Specs and Maintenance
The work includes a Raspberry Pi connected to a tft screen. To power down the Raspberry Pi, the switch on the device's left side needs to be flipped. Once the Pi has shutdown, unplug the device's power source from the wall. To turn the device on, simply plug the power supply back into the wall. Once plugged in, the Pi will  boot up, and the program will automatically start running. No other intervention is needed for the artwork to be usable.

As long as the outlined shutdown procedure is followed, there should be no other maintenance necessary. If the machine is not powered down correctly there is the small chance that the SD card running the device's software will become corrupted and need to be replaced. A pre-prepared replacement SD card will be provided, and its replacement just requires the removal of two roberston screws on the device's face to expose the Raspberry Pi's SD card slot.

## Additional Images

<img src="./images/Mansfield_Reporter_02.JPG" width="600">

<img src="./images/animated-decay.gif">

<img src="./images/animated-morality.gif">

## Further Reading
**Blog post:** <https://maxlupo.com/mansfield-reporter/>  
**Source files:** *forthcoming*  
**Full resolution images:** <https://drive.google.com/drive/folders/1PHH9C1Y3jwUbRDI2Ql60bMIWz6fIhCgK>  *note: the gifs in that folder will need to be downloaded to be viewed*