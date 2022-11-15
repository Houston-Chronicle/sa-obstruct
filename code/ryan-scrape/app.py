import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from dwiCases import (drivingWhileIntoxicated, dwiBAC015OrHigher,
                      everythingElse, fixedURLs, obstructHighwayIntoxication,
                      obstructPassageway, timeoutFolks)

caseEventList = []

print('Starting...')

def getRecords(i, category, driver):
    caseEvents = driver.find_elements(by=By.TAG_NAME, value="tr")[1:]
    

    for event in caseEvents:
        eventDate, eventDescription = event.find_elements(by=By.TAG_NAME, value="td")
        caseEventList.append(
            {
                "full_name": category[i]['full_name'],
                "url": category[i]['url'],
                "birthDate": category[i]['birthdate'],
                "sex": category[i]["sex"],
                "race": category[i]["race"],
                "offense_description": category[i]["offense_description"],
                "reduced_offense_desc": category[i]["reduced_offense_desc"],
                "court": category[i]["court"],
                "case_cause_nbr": category[i]["case_cause_nbr"],
                "sid": category[i]["sid"],
                "judicial_nbr": category[i]["judicial_nbr"],
                "character_cnt": category[i]["character_cnt"],
                "eventDate": eventDate.text,
                "eventDescription": eventDescription.text
            }
        )

def getCaseEvents(category):
    for i in range(0,len(category)):
        print('Scraping {}/{} | Case URL: {}'.format(i+1, len(category), category[i]['url']))
        options = Options()
        options.headless = True
        try: 
            driver = webdriver.Firefox(options=options, service=Service(executable_path="/Users/ryan/dev/playground/selenium/geckodriver"))
            driver.get(category[i]['url'])
            WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.TAG_NAME, "h2"))
        )
            getRecords(i, category, driver)
            driver.close()
            # time.sleep(1)
        except:
            print("Timed out waiting for page to load")
            caseEventList.append(
                {
                    "full_name": category[i]['full_name'],
                    "url": category[i]['url'],
                    "birthDate": category[i]['birthdate'],
                    "sex": category[i]["sex"],
                    "race": category[i]["race"],
                    "offense_description": category[i]["offense_description"],
                    "reduced_offense_desc": category[i]["reduced_offense_desc"],
                    "court": category[i]["court"],
                    "case_cause_nbr": category[i]["case_cause_nbr"],
                    "sid": category[i]["sid"],
                    "judicial_nbr": category[i]["judicial_nbr"],
                    "character_cnt": category[i]["character_cnt"],
                    "eventDate": "Timeout error",
                    "eventDescription": "Timeout error"
                })
            driver.close()
            # time.sleep(1)
        else:
            df = pd.DataFrame(caseEventList)
            df.to_csv('timeoutsPartial.csv', index=False)
            continue

getCaseEvents(timeoutFolks)

df = pd.DataFrame(caseEventList)
df.to_csv('timeouts.csv', index=False)

print('Done!')
