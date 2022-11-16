# SA DWI
Scraper and analysis scripts for looking at DWI misdemeanors and felonies in Bexar County between Jan. 2, 2009 and Jan. 13, 2022.

**["Getting Off Easy."](https://www.expressnews.com/news/local/article/DWI-cases-San-Antonio-17577179.php)**

# Questions

For the "Getting Off Easy" investigation, the San Antonio Express-News had several questions to answer:
* How many obstruction charges had occurred since 2009?
* How many of these obstruction charges were associated with an incident where the charged person had a BAC above .15?
* How many of these obstruction charges were associated with a crash?

Our work also led to an important additonal question: 
* How many charges labeled "obstruction passageway" involved alcohol? 

# Findings

In the end, our analysis yielded the **following results**: 

* Some 69,000 people were charged with a DWI-related offense during the 13-year-period in question.
* More than 19,000 of them — 28 percent — had their charges downgraded to obstructing a highway.
* Of those with downgraded charges, one in four — nearly 5,000 people — were granted that break even though their blood alcohol concentrations were higher than .15, the threshold for extreme intoxication.
* More than 1,900 people whose DWI charges were downgraded were later arrested again for drunken driving.
* By the end of 2021 — 14 months after DA Gonzales [clarified the DWI to obstruction of highway policy](https://www.expressnews.com/news/local/article/DWI-cases-San-Antonio-17577179.php?sid=5bbcfeda3f92a45e831e32f4&utm_source=newsletter&utm_medium=email&utm_content=news_a&utm_campaign=SAEN_TopStories#photo-23155916:~:text=Gonzales%20wrote%20that%20the%20reduced%20charge%20was%20appropriate%20when%3A) — DWI suspects in Bexar County had pleaded to obstructing a highway in 490 cases. In 169 of them — about 35 percent — the driver’s BAC was over .15.

**Related Findings**
* Alcohol-related crashes and fatalities in San Antonio have declined slightly on a per-capita basis over the last decade. Yet they continue to take a heavy toll, causing an average of 53 deaths per year since 2010, according to data from the Texas Department of Transportation.
* In 2021, drunken drivers caused nearly 2,000 crashes in San Antonio, killing 57 people and seriously injuring 107.

# How do we know this? 

The answers lie in the following files:

**Data point**: Some 69,000 people were charged with a DWI-related offense during the 13-year-period in question.<br> 
**Proof**: master-file, lines 415-421

**Data point**: More than 19,000 of them — 28 percent — had their charges downgraded to obstructing a highway.<br> 
**Proof**: master-file, lines 432-438

**Data point**: Of those with downgraded charges, one in four — nearly 5,000 people — were granted that break even though their blood alcohol concentrations were higher than .15, the threshold for extreme intoxication.<br> 
**Proof**: master-file, lines 675-686

**Data point**: More than 1,900 people whose DWI charges were downgraded were later arrested again for drunken driving.<br> 
**Proof**: previous-dwi-charges.Rmd, lines 284-289

**Data point**: The Express-News analysis identified more than 3,500 people who received that extra benefit. They made up 18 percent of all DWI defendants whose charges were downgraded to obstructing a highway from 2009-2022. <br> 
**Proof**: master-file, lines 565-570

**Data point**: By the end of 2021 — 14 months after DA Gonzales [clarified the DWI to obstruction of highway policy](https://www.expressnews.com/news/local/article/DWI-cases-San-Antonio-17577179.php?sid=5bbcfeda3f92a45e831e32f4&utm_source=newsletter&utm_medium=email&utm_content=news_a&utm_campaign=SAEN_TopStories#photo-23155916:~:text=Gonzales%20wrote%20that%20the%20reduced%20charge%20was%20appropriate%20when%3A) — DWI suspects in Bexar County had pleaded to obstructing a highway in 490 cases. In 169 of them — about 35 percent — the driver’s BAC was over .15. <br>
**Proof**: master-file, lines 734-739

**Data point**: Alcohol-related crashes and fatalities in San Antonio have declined slightly on a per-capita basis over the last decade. Yet they continue to take a heavy toll, causing an average of 53 deaths per year since 2010, according to data from the Texas Department of Transportation. <br>
**Proof**: graphs.Rmd, lines 224-230

**Data point**: In 2021, drunken drivers caused nearly 2,000 crashes in San Antonio, killing 57 people and seriously injuring 107.<br>
**Proof**: graphs.Rmd lines 234-239

# Actual Data
The data files we used for this project are not available to protect the privacy of the individuals in the dataset. Some data analysis is also restricted for that purpose. 

# Files Explained (in order they should be run)

**scrape-recrods.ipynb** <br>
How we scraped records from [Bexar County Misdemeanors](https://www.bexar.org/2923/Misdemeanor-Records) and [Bexar County Felonies](https://www.bexar.org/2988/Online-District-Clerk-Criminal-Records) <br>
<br>
Script by Alexandra Kanik

**ryan-scrape folder** <br>
Details on specific cases can be pulled from the [County and District Clerks website](https://search.bexar.org/) using a specially formatted URL that contains the case identifier. We compiled those URLs for each case in our datasheet and then scraped the detailed docket tables for each case. This scrape returned millions of rows of docket information. The following files accomplish this task.
* **geckodriver**: "essentially a puppet version of Firefox"
* **requirements.txt**: has all the tools needed for the project
* **app.py**: used for scraping the data from each individual's docket
* **mergeCSVs.py**: used to put together CSVs with all of the docket information <br>

Scripts by Ryan Serpico

**master-file.Rmd** <br>
This file goes through the bulk of the data analysis. Starting with After we clean the data acquired from Bexar County misdemeanors and felonies spreadsheets, we look at the docket data from Ryan's scraper so we are able to determine all of the alcohol-related obstructions. (Spoiler alert: it's most of them.) We then break down this analysis by looking at obstruction passageway charges and obstruction highway intoxication charges and eventually determine the number of people whose BAC was above .15. <br>
<br>
Script by Libby Seline

**previous-dwi-charges.Rmd** <br>
Using the Bexar County files, we make a dataset where one person equals one row and all of their charges can be found there. We use this file to determine how many people have their obstruction as their first charge and then reoffend. <br>
<br>
Script by Libby Seline

**graphs.Rmd** <br>
Analysis to talk about DWI crashes and how many people have died over the years. <br>
<br>
Script by Libby Seline

## [See our published methodology here](https://www.expressnews.com/news/local/article/DWI-investigation-San-Antonio-Express-News-17586446.php)

# Graphs

[Scrolly Slide 1](https://public.flourish.studio/visualisation/11247430/) <br>
[Scrolly Slide 2](https://public.flourish.studio/visualisation/11247485/) <br>
[Scrolly Slide 3](https://public.flourish.studio/visualisation/11248041/) <br>
<br>
[San Antonio drunk driving per capita, 2021](https://public.flourish.studio/visualisation/11250262/) <br>
[Bexar County reoffenders](https://www.datawrapper.de/_/Zm8co/) <br>
<br>
Graphs by Libby Seline
