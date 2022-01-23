#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time


# In[5]:


def loop():
    url = 'https://www.capital.gr/finance/el/allstocks/1'
    result =requests.get(url)

    soup = BeautifulSoup(result.text,'html.parser')
    page = soup.find('div',{'class':'cp__table'})

    quotes=[]

    for i in page.find_all('td'):
        try:
            z=(i.a.text)
            try:
                if int(z[0])>=0:
                    pass
            except:
                z=z.replace(' ','')
                quotes.append(z)
        except:
            pass 
    stock = []
    price = []
    change = []
    change_percentage = []
    open = []
    high = []
    low = []
    volume =[] 
    turnover =[]
    acts = []
    buyers = []
    sellers =[]
    capitalization = [] 
    ticker=[]
    market=[]
    tickerperc = []

    c=0
    for i in quotes:
        try:
            url1='https://www.capital.gr/finance/quote/'+i
            result2 = requests.get(url1)
            soup2 = BeautifulSoup(result2.text,'lxml')

            ticker.append(i)
            market.append('Athens Stock Market')
            try:
                stock.append(soup2.find('h1',{'class':'bold serif h1ash2'}).text)
            except: 
                stock.append(np.nan)

            try:
                price.append(soup2.find('h3',{'class':'price bold'}).span.text.replace(',','.'))
                
            except:
                price.append(np.nan)

            try:
                try:
                    changes = soup2.find('h4',{'class':'winner change'}).find_all('span')
                except:
                    changes = soup2.find('h4',{'class':'change'}).find_all('span')
            except:
                pass
            try:
                change.append(changes[0].text.replace(',','.'))
            except:
                change.append(np.nan)
            try:
                z=changes[1].text.replace('(','').replace(')','').replace(',','.').replace('%','')
                change_percentage.append(float((z)))
                tickerperc.append(str(str(i)+' \n'+str(float((z))))+'%')
            except: 
                change_percentage.append(np.nan)
                tickerperc.append(np.nan)
            try:
                financial_data = soup2.find('div',{'class':'finance__details__right'}).find_all('span')
            except:
                pass

            try:
                open.append(financial_data[0].text)
            except:
                open.append(np.nan)
            try:
                high.append(financial_data[1].text)
            except:
                high.append(np.nan)
            try:
                low.append(financial_data[2].text)
            except: 
                low.append(np.nan)
            try:
                volume.append(financial_data[3].text)
            except:
                volume.append(np.nan)
            try:    
                turnover.append(financial_data[4].text)
            except:
                turnover.append(np.nan)
            try:
                acts.append(financial_data[5].text)
            except:
                acts.append(np.nan)
            try:    
                buyers.append(financial_data[6].text)
            except:
                buyers.append(np.nan)
            try:    
                sellers.append(financial_data[7].text)
            except:
                sellers.append(np.nan)
            try:   
                capitalization.append(int(financial_data[8].text.replace('.','').replace(' €','')))
            except:
                capitalization.append(np.nan)

            c=c+1
        except:
            pass

    building_materials=['AKRIT','ΒΙΟΚΑ','ΙΚΤΙΝ','ΑΛΜΥ','ΜΑΘΙΟ','TITC']
    food_and_beverages_wine=['ΕΕΕ','ΜΠΟΠΑ','ΜΠΟΚΑ','ΚΤΗΛΑ','ΚΜΟΛ','ΕΒΡΟΦ','ΚΡΙ','ΣΑΡΑΝ','ΚΕΠΕΝ','ΛΟΥΛΗ','ΝΙΚΑΣ']
    insurance=['ΕΥΠΙΚ','ΜΠΡΙΚ']
    agriculture=['ΣΠΥΡ','ΚΡΕΚΑ']
    industry = ['ΜΥΤΙΛ','ΛΕΒΚ','ΛΕΒΠ','ΠΕΤΡΟ','ΣΑΤΟΚ','ΒΑΡΓ','ΔΡΟΜΕ',
                'CENER','ΜΕΝΤΙ','ΚΑΡΕΛ','ΦΛΕΞΟ','ΒΙΣ','ΠΑΙΡ']  
    industrial_manifacturers=['ΦΡΙΓΚΟ','ΒΙΟΣΚ','ΔΙΟΝ','ΒΟΣΥΣ','ΓΕΒΚΑ',
                              'ΕΛΤΟΝ','ΞΥΛΚ','ΞΥΛΠ','ΙΝΤΕΤ']
    construction = ['ΙΝΚΑΤ','ΑΒΑΞ','ΒΙΟΤ','ΓΕΚΤΕΡΝΑ','ΔΟΜΙΚ','ΕΚΤΕΡ','ΕΛΛΑΚΤΩΡ',
                   'ΚΛΜ','ΠΡΔ']
    real_estate = ['ΙΝΤΕΡΚΟ','ΤΡΑΣΤΟΡ','ΠΡΟΝΤΕΑ','ΛΑΜΨΑ','ΛΑΜΔΑ','ΠΡΕΜΑ',
                   'ΚΑΜΠ','ΕΛΒΙΟ','ΚΕΚΡ','ΑΣΤΑΚ','ΜΙΓΡΕ']
    financial = ['CNLCAP','ΜΙΓ','ΑΝΔΡΟ','ΕΧΑΕ','ΣΕΝΤΡ','ΑΛΦΑ','ΑΤΤ','ΕΥΡΩΒ',
                'ΕΤΕ','ΕΛΛ','ΠΕΙΡ']
    consumer_and_retail = ['ΠΛΑΙΣ','ΦΡΛΚ','ΣΑΡ','ΠΑΠ','ΑΤΕΚ','ΛΙΒΑΝ',
                           'ΛΑΝΑΚ','ΜΟΝΤΑ','ΑΣΚΟ','ΓΓΓΚΡΠ','ΜΟΤΟ','ΝΑΚΑΣ',
                           'ΕΛΓΕΚ','ΥΑΛΚΟ','ΓΕΔ','ΜΙΝ','ΕΛΒΕ','ΔΟΥΡΟ','ΜΠΕΛΑ','ΦΦΓΚΡΠ']
    energy_and_oil = ['ΕΛΙΝ','ΜΟΗ','ΡΕΒΟΙΛ','ΤΕΝΕΡΓ','ΕΛΠΕ','ΔΕΗ','ΑΔΜΗΕ']
    telematics = ['ΣΠΕΙΣ','ΟΤΕ']
    textiles = ['ΒΑΡΝΗ','ΜΟΥΖΚ','ΕΠΙΛΚ','ΝΑΥΠ','ΑΑΑΚ','ΑΑΑΠ','ΦΙΕΡ']
    technology = ['ΕΠΣΙΛ','ΛΟΓΟΣ','ΜΛΣ','ΕΝΤΕΡ','ΙΛΥΔΑ','ΣΠΙ','ΙΝΤΕΚ'
                 'ΒΥΤΕ','ΠΡΟΦ','ΚΟΥΑΛ','ΚΟΥΕΣ','ΙΝΤΚΑ']
    metalurgy_and_plastic = ['ΜΕΒΑ','ΒΙΟ','ΕΛΧΑ','ΔΑΙΟΣ','ΠΛΑΘ','ΠΛΑΚΡ',
                             'ΚΟΡΔΕ','ΕΛΣΤΡ','ΜΠΤΚ','ΣΙΔΜΑ','ΤΖΚΑ','ΜΕΡΚΟ',]
    travel_and_tourism = ['ΑΤΤΙΚΑ','ΑΝΕΠΟ','ΑΝΕΚ','ΑΝΕΠ','ΚΥΡΙΟ','ΑΡΑΙΓ','ΟΤΟΕΛ','ΜΙΝΟΑ']
    gambling = ['ΙΝΛΟΤ','ΟΠΑΠ']
    water = ['ΕΥΔΑΠ','ΕΥΑΠΣ']
    health = ['ΙΑΣΩ','ΙΑΤΡ','ΟΛΥΜΠ']
    not_active = ['TITK','ΑΤΕ','ΚΥΠΡ','ΜΕΤΚ','ΣΙΔΕ']


    group=[]
    for i in ticker:
        if i in building_materials:
            group.append('Building Materials')
        elif i in food_and_beverages_wine:
            group.append('Food and Drinks')
        elif i in insurance:
            group.append('Insurance')
        elif i in agriculture:
            group.append('Agriculture')
        elif i in industry:
            group.append('Industry')
        elif i in industrial_manifacturers:
            group.append('Industrial Manifacturers')
        elif i in construction:
            group.append('Construction')
        elif i in real_estate:
            group.append('Real Estate')
        elif i in financial:
            group.append('Financial')
        elif i in consumer_and_retail:
            group.append('Consumer and Retail')
        elif i in energy_and_oil:
            group.append('Energy and Oil')
        elif i in telematics:
            group.append('Telematics')
        elif i in textiles:
            group.append('Textiles')
        elif i in technology:
            group.append('Technology')
        elif i in metalurgy_and_plastic:
            group.append('Metalurgy and plastic')
        elif i in travel_and_tourism:
            group.append('Travel and Tourism')
        elif i in gambling:
            group.append('Gambling')
        elif i in water:
            group.append('Water')
        elif i in health:
            group.append('Health')
        else:
            group.append('Other')

    data=pd.DataFrame({
    'stock': stock,
    'ticker' : ticker,
    'price':price,
    'change': change,
    'change_percentage' : change_percentage,
    'group': group,
    'tickerperc': tickerperc,
    #'open' : open,
    #'high' : high,
    #'low' : low,
    #'volume' : volume,
    #'turnover' : turnover,
    #'acts' : acts,
    #'buyers' : buyers,
    #'sellers' : sellers,
    'capitalization' : capitalization
                      })
    data = data[data['stock'].notna()]
    data = data[data.change != '0.0000']
    return(data)


# In[3]:


while True:
    data=loop()
    data.to_csv('finvizdata.csv')
    time.sleep(900)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




