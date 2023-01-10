import pandas as pd

leadername = ['Stanisław', 'Jan', 'Jan', 'Grzegorz', 'Jan']
leadersurname = ['Żółkiewski', 'Chodkiewicz', 'Sobieski', 'Chodkiewicz', 'Chodkiewicz']
battle = ['Kłuszyn 4.VII.1610', 'Kircholm 27.IX.1605', 'Wiedeń 12.IX.1683 | Chocim 11.XI.1673','Czaśniki 26.I.1564','Biały Kamień 25.IX.1604']
btype = ['land battle']*5
no = ['old slavic','hebrew','hebrew','greek','hebrew']
title = ['hetman wielki koronny','hetman wielki litewski','król','hetman wielki litewski','hetman wielki litewski']

ln = pd.Series(leadername)
ls = pd.Series(leadersurname)
b = pd.Series(battle)
bt = pd.Series(btype)
o = pd.Series(no)
t = pd.Series(title)

data = pd.DataFrame({'Leader Name': ln, 'Leader Surame': ls, 'Battle': b, 'Battle type': bt,
                     'Name origin': o, 'Title':t})

#1)

for index, row in data.iterrows():
    if '|' in row['Battle']:
        s = row['Battle'].find('|')
        newrow = row.copy()
        newrow['Battle']=row['Battle'][s+2:]
        row['Battle']=row['Battle'][0:s]

data = data.append(newrow)

print(data)

#2)

battles = pd.DataFrame({'Battle': list(data['Battle']), 'Battle type': list(data['Battle type']),
                       'Leader Name': list(data['Leader Name']), 'Leader Surame': list(data['Leader Surame'])})
battles = battles.drop_duplicates()
print(battles)

leaders = pd.DataFrame({'Leader Name': ln, 'Leader Surame': ls, 'Name origin': o, 'Title':t})
leaders = leaders.drop_duplicates()
print(leaders)

#3)
leader_name = pd.DataFrame({'Leader Name': ln, 'Name origin': o})
leader_name = leader_name.drop_duplicates()
print(leader_name)

leader_surname = pd.DataFrame({'Leader Surame': ls, 'Title':t})
leader_surname = leader_surname.drop_duplicates()
print(leader_surname)

## battles data frame is exactly the same as in #2)

#4)
newdata = pd.merge(leader_surname, battles, on = 'Leader Surame')
print(newdata)

newdata2 = pd.merge(leader_name, battles, on = 'Leader Name')
print(newdata2)

newdata3 = pd.merge(newdata, newdata2, on = ['Battle', 'Leader Name', 'Leader Surame'])
print(newdata3)

leaders2 = pd.DataFrame({'Leader Name': newdata3['Leader Name'], 'Leader Surame': newdata3['Leader Surame'],
                         'Name origin': newdata3['Name origin'], 'Title': newdata3['Title']})
leaders2 = leaders2.drop_duplicates()
print(leaders2)


