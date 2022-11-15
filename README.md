# SA DWI
Scraper and analysis scripts for looking at DWI misdemeanors and felonies in Bexar County between Jan. 2, 2009 and Jan. 13, 2022.

**["Getting Off Easy."](https://wcm.hearstnp.com/expressnews.com/news/local/article/DWI-cases-San-Antonio-17577179.php)**

# Questions

For the "Getting Off Easy" investigation, the San Antonio Express-News had several questions to answer:
* How many obstruction charges had occurred since 2009?
* How many of these obstruction charges also was associated with an incident where a person had a BAC above 0.15?
* How many of these obstruction charges were also associated with a crash?

Our work also led to an important additonal question: 
* How many of any charge labeled "obstruction passageway" involved alcohol and how many did not? 

# Findings

In the end, we came up with the **following conclusions**: 

* Some 69,000 people were charged with a DWI-related offense during that 13-year-period, the records show.
* More than 19,000 of them — 28 percent — had their charges downgraded to obstructing a highway.
* Of that lucky group, one in four — nearly 5,000 people — were granted that break even though their blood alcohol concentrations were higher than.15, the threshold for extreme intoxication.
* More than 1,900 people whose DWI charges were downgraded were later arrested again for drunken driving. <br>
* By the end of 2021 — 14 months after Gonzales clarified his policy — DWI suspects in Bexar County had pleaded to obstructing a highway in 490 cases. In 169 of them — about 35 percent — the driver’s BAC was over.15, court records show.

**Related Findings**
* Alcohol-related crashes and fatalities in San Antonio have declined slightly on a per-capita basis over the last decade. Yet they continue to take a heavy toll, causing an average of 53 deaths per year since 2010, according to data from the Texas Department of Transportation.
* In 2021, drunken drivers caused nearly 2,000 crashes in San Antonio, killing 57 people and seriously injuring 107.

# How do we know this? 

The answers lie in the following files:

**Data point**: Some 69,000 people were charged with a DWI-related offense during that 13-year-period, the records show. <br> 
**Proof**: master-file, lines 415-421

**Data point**: More than 19,000 of them — 28 percent — had their charges downgraded to obstructing a highway. <br> 
**Proof**: master-file, lines 432-438

**Data point**: Of that lucky group, one in four — nearly 5,000 people — were granted that break even though their blood alcohol concentrations were higher than.15, the threshold for extreme intoxication. <br> 
**Proof**: master-file, lines 675-686

**Data point**: More than 1,900 people whose DWI charges were downgraded were later arrested again for drunken driving. <br> 
**Proof**: previous-dwi-charges.Rmd, lines 284-289

**Data point**: The Express-News analysis identified more than 3,500 people who received that extra benefit. They made up 18 percent of all DWI defendants whose charges were downgraded to obstructing a highway from 2009-2022. <br> 
**Proof**: master-file, lines 565-570

**Data point**: By the end of 2021 — 14 months after Gonzales clarified his policy — DWI suspects in Bexar County had pleaded to obstructing a highway in 490 cases. In 169 of them — about 35 percent — the driver’s BAC was over.15, court records show. <br>
**Proof**: master-file, lines 734-739

**Data point**: Alcohol-related crashes and fatalities in San Antonio have declined slightly on a per-capita basis over the last decade. Yet they continue to take a heavy toll, causing an average of 53 deaths per year since 2010, according to data from the Texas Department of Transportation. <br>
**Proof**: graphs.Rmd, lines 224-230

**Data point**: In 2021, drunken drivers caused nearly 2,000 crashes in San Antonio, killing 57 people and seriously injuring 107.<br>
**Proof**: graphs.Rmd lines 234-239

# Actual Data
The data files we used for this project is not available to protect the privacy of the individuals in the dataset. Some data analysis is also restricted for that purpose. 

# Files Explained (in order they should be run)

**scrape-recrods.ipynb** <br>
How we scraped records from [Bexar County Misdemeanors](https://www.bexar.org/2923/Misdemeanor-Records) and [Bexar County Felonies](https://www.bexar.org/2988/Online-District-Clerk-Criminal-Records) <br>
<br>
Script by Alexandra Kanik

**ryan-scrape folder** <br>
After we patched together URLs for people in our datasheet, we scraped the table on the page and exported millions of rows of data. The following files accomplish this task.
* **geckodriver**: "essentially a puppet version of Firefox"
* **requirements.txt**: has all the tools needed for the project
* **app.py**: used for scraping the data from each individual's docket
* **mergeCSVs.py**: used to put together CSVs with all of the docket information <br>

Scripts by Ryan Serpico

**master-file.Rmd** <br>
This file goes through the bulk of the data analysis. Starting with data acquired from Bexar County misdemeanors and felonies. After we clean that up, we look at the docket data from Ryan's scraper so we are able to determine all of the alcohol related obstructions. (Spoiler alert: it's most of them.) We then break down this analysis by looking at obstruction passageway charges and obstruction highway intoxication charges and eventually determining the number of people whose BAC was above 0.15. <br>
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

# Methodology

**About our analysis** <br>
The Express-News studied Bexar County court records on alcohol-related driving offenses from January  2009 to January 2022 to gain insight into how the criminal justice system handles DWI cases. Our data analysis provided the backbone for the Express-News project ["Getting Off Easy."](https://wcm.hearstnp.com/expressnews.com/news/local/article/DWI-cases-San-Antonio-17577179.php)

**Why that time period?**

We began in 2009 because that was the first full year of then-District Attorney Susan Reed’s “Take Responsibility” program, which allowed first-time DWI offenders to serve probationary sentences and emerge with no DWI conviction on their records. 

**What did we do?**

We wrote a script to download and filter misdemeanor and felony court records. The records are updated daily and were last downloaded by our script on Jan. 13, 2022.

We captured relevant cases by filtering misdemeanor records for those that included one of the charges listed here:

[Datawrapper table](https://www.datawrapper.de/_/Vx8hj/)

Our initial scrape captured 80,937 records. We did additional filtering and analysis to answer two key questions.

Under the “Take responsibility” program, DWI charges are often downgraded to “obstructing a highway,” a lesser offense with lighter penalties and no social stigma. We wanted to identify cases that had been pleaded down to that charge. To pinpoint those instances, we separated out  “obstructing-a-highway” cases that involved alcohol, as opposed to cases in which a motorist was cited simply for blocking a road or sidewalk.

We also wanted to identify cases where defendants were allowed to plead to  obstructing a highway even though their blood alcohol concentration  (BAC) was above .15. That’s more  than twice the legal limit – an extreme level of intoxication at which a person’s reflexes, judgment and motor coordination are severely impaired. Defendants with BACs above .15 were supposed to be barred from the “Take Responsibility” program.

To answer these questions, we created a script to pull case information from Bexar County court records. The script singled out cases where people were charged with obstructing a highway or had their charges reduced to that.

Using that information, we compiled all cases with offense codes or other information that indicated alcohol was involved and that included  a BAC above .15. That gave us a list of all obstructing-a-highway cases that involved drinking and driving, including those where the motorist was in the “extreme intoxication” zone.

**What we found**

From January 2009 to January 2022,  Bexar County authorities charged 69,242 people with either a DWI-related offense or with alcohol-related obstructing a highway. Based on interviews with current and former prosecutors and a review of a sample of hard-copy case files at the Bexar County courthouse, we determined that all cases of alcohol-related obstructing a highway began as DWIs and were plea-bargained down to the lesser charge.   

Based on the above, we determined that 19,444 people charged with a DWI-related offense had their charges reduced to obstructing a highway.
 
Of those, 4,942 were granted that break even though their BAC was higher than .15.

We identified another way in which the rules for “Take Responsibility” were undermined. Reed wanted participants in the program to plead to “obstructing a highway-intoxication” — a charge she devised by adding the word “intoxication.” That way, the defendants’ records would reflect an offense involving alcohol, even if not one with the career-wrecking gravity of a DWI.

But prosecutors began to bargain that away in plea negotiations, allowing offenders to plead to obstructing a highway, minus the “intoxication.”

Our analysis identified 3,562 people who received that extra benefit. They made up 18 percent of all DWI defendants whose charges were downgraded to obstructing a highway.

Finally, we determined that more than 1,919 people whose DWI charges were downgraded were later arrested again for drunken driving. 

Ryan Serpico and Alexandra Kanik contributed to this analysis.

# Graphs

[Scrolly Slide 1](https://public.flourish.studio/visualisation/11247430/) <br>
[Scrolly Slide 2](https://public.flourish.studio/visualisation/11247485/) <br>
[Scrolly Slide 3](https://public.flourish.studio/visualisation/11248041/) <br>
<br>
[San Antonio drunk driving per capita, 2021](https://public.flourish.studio/visualisation/11250262/) <br>
[Bexar County reoffenders](https://www.datawrapper.de/_/Zm8co/) <br>
<br>
Graphs by Libby Seline
