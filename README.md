# EyeOfSentinel2
### Hackathon project

## Inspiration

We often hear about floods, smog, deforestation, heat waves, etc. in the news.
And the reasons for this are clear, climate change, air pollution, etc. but also the distribution of buildings in a city as well as the amount of green spaces play a role.
And then I wondered how to check the distribution of buildings and green spaces in an area. So I came up with an idea: satellite images.

## What it does

Using the channels from the satellite image, the program calculates the NDVI, NDWI, NDSI, NDBI[^1] and NDBSI of the satellite image. And creates plots from it.

[^1]: Normalized Difference Vegetation Index, Normalized Difference Water Index, Normalized Difference Snow Index, Normalized Difference Built-up Index, Normalized Difference Bare Soil

## How I built it

I programmed this GUI with Python. 
I used vscode and google colab as editor.
For my program I used these libraries because of these reasons:
* tkinker & customtkinter --> create and style GUI
* matplotlib --> create plots
* rasterio --> open file(channel) and reshape it
* cv2 --> resize the channels 
* (not necessary) time --> checked how long it takes to finish 
* os & random --> create a new folder every time the program is used

## Challenges I ran into
The design was a bit of a challenge. 
The code takes too long for large satellite images so I resized the satellite images.

## Accomplishments that I'm proud of
I am proud that my project works at all.

## What I learned
I learned a lot about satellites. How they work and what NDVI, NDWI, etc. are. I also learned about the problems with our cities today.

## What's next for EyeOfSentinel2

## How it works
First you need a satellite image. You can get this in Copernicus Browser from easa. After you have downloaded a satellite image, you will get different folders with different files. The files we need are in:

downloaded folder --> GRANULE --> click on the only folder --> IMG_DATA --> R20m or R60m (your choice)

There you will see these files, these are the channels:
![Screenshot 2025-02-16 193200](https://github.com/user-attachments/assets/77f84fb1-3948-41be-803b-c0c43ea5c1a5)
![Sentinel-2-band-characteristics](https://github.com/user-attachments/assets/bb92bb69-508d-443d-8d96-790d9ec40d02)

You simply upload them into the program and then you will get the results.
