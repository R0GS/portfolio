import csv
films =[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open('films.csv', 'w') as f:
    write = csv.writer(f, delimiter=',')
    for film_list in films:
        write.writerow(film_list)
