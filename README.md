# DSE 511 HW 6 Project
So the point of this is to see if theres correlation between major world events/US events and certain stocks going up immediately after.
That was the main goal. In the one file i wrote some strategies to just look at trends over some periods, they were not the most helpful without probably diving more deeply into it.
What i did notice, was at major events involving the wars, we saw the RTX and LMT stocks jump significantly right after, where the Tech stocks of NVDA and TSLA kinda remained on their same path, where the military contractors were going up due to this and everyone especially Wallstreet knowing it will give them a lot of government contracts. Even some of the strategies stayed with this trend where, for example, the tech stocks Short moving AVG and long both were trending down during the Russia/ukraine war start, where the exact opposite was true for the Mililtary industrial complex stocks went up in these

To see what I wanted, i went first by just scraping the 4 probably most prevelant stocks for tech and military contractors. Taking 2 and 2, Using Alpaca API i pulled data from 2020 to late november, which holds data for all these events. That was farily simple, MainP2.py however was a little annoying as the dates and times from alpaca are kinda of annoying to deal with and needing to convert them to dateTime objects and a plethora of other issues copming up I cannot remember at this point just took hours to toruble shoot. What idd help was having done stuff with alpaca for a persoanl project before that was fairly similar doing the moving averages and stuff like that as they are super simple to do and really youre just setting a day range. The R file tells me the percent change from each events start date over 30 days to see how they are affected right after this news is given. 

With this there is definitely, and not shoicking correlation between a War and Lockeheed Marting and Raytheon stock just skyrocketing (to an extent) the next day


The PNGs are all the graphs spat out by the `mainp2.py` file

# Code Overview
* `main.py`
Scrapes Alpaca API and writes the 4 stocks chosen based on their ticker and writes it all to a csv
* `mainP2.py`
Takes the CSVs and graphs the Short, long and exponential moving average and graphs them along with the start dates of these events to see the peaks of price, and SMA/LMA/EMA.
* `mainp3/r`
Reads in the 4 CSVs and takes the start date of these events and gives the price change as a percentage for the next 30 days.


# Data from `mainP3.r`
    "event: Ukraine/Russia"
 "NVDA change: 16.5894736842105"
 "TSLA change: 26.2101004046156"
 "LMT change: 14.6445629375048"
 "RTX change: 8.6790450928382"

 "event: Israel/Palestine"
 "NVDA change: 1.06030483764081"
 "TSLA change: -15.558208495398"
 "LMT change: 3.35143060041694"
 "RTX change: 12.8921770105494"

 "event: Election 2020"
 "NVDA change: -1.45048349449818"
 "TSLA change: 51.2203626220363"
 "LMT change: 7.19883817011794"
 "RTX change: -1.91981193678986"

 "event: Election 2024"
 "NVDA change: 27.1406058483628"
 "TSLA change: -5.63054559184444"
 "LMT change: -7.72461213743282"
 "RTX change: 6.48180648180649"

 "event: China/HongKong"
 "NVDA change: 11.7077279427248"
 "TSLA change: 37.7552437838589"
 "LMT change: 4.60374876685301"
 "RTX change: -6.75105485232067"

 "event: US Afghanistan"
 "NVDA change: 11.4786967418546"
 "TSLA change: 8.49947534102833"
 "LMT change: -4.41637751561416"
 "RTX change: -5.0493458801928"